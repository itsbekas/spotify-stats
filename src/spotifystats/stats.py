from math import floor
from os import environ
from time import sleep, time

import spotipy
from dateutil.parser import parse
from spotipy.oauth2 import SpotifyPKCE

from spotifystats.database import Database, Collection


ranges = ["short_term", "medium_term", "long_term"]

def _extract_track(track):
    '''Extracts the relevant info from a track'''
    return {
        "id": track["id"],
        "name": track["name"],
        "artists": [{"id": artist["id"], "name": artist["name"]} for artist in track["artists"]]
    }

def _extract_artist(artist):
    '''Extracts the relevant info from an artist'''
    return {
        "id": artist["id"],
        "name": artist["name"]
    }

def _timestamp_to_int(timestamp):
    return floor(parse(timestamp, "").timestamp())

class SpotifyStats:

    def __init__(self):
        scope = ["user-top-read", "user-read-recently-played"]
        self._timestamp = 0
        self._sp = self._auth(scope)
        self._db = Database("spotify-stats")

    def _auth(self, scope):
        # Make sure credentials are set
        if not all(env in environ for env in ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIPY_REDIRECT_URI"]):
            raise Exception("Make sure SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET and SPOTIPY_REDIRECT_URI are defined in your environment!")

        auth = SpotifyPKCE(scope=scope, open_browser=False)
        auth.get_access_token()
        return spotipy.Spotify(auth_manager=auth)

    def _get_top_tracks(self, range):
        tracks = self._sp.current_user_top_tracks(limit=50, offset=0, time_range=range)["items"]
        return [_extract_track(track) for track in tracks]

    def _get_top_artists(self, range):
        artists = self._sp.current_user_top_artists(limit=50, offset=0, time_range=range)["items"]
        return [_extract_artist(artist) for artist in artists]

    def _get_recently_played(self):
        timestamp = self._db.get_timestamp()*1000 # Timestamp must be in milliseconds
        tracks = self._sp.current_user_recently_played(limit=50, after=timestamp)["items"]
        return [{
                "track": _extract_track(track["track"]),
                "last_listened": track["played_at"]
            } for track in tracks]

    def _create_ranking(self):
        self._db.create_ranking(self._timestamp)

    def _add_track(self, track, timestamp=0):
        artists = [artist["id"] for artist in track["artists"]]
        self._db.add_track(track["id"], track["name"], artists)

    def _add_artist(self, artist):
        self._db.add_artist(artist["id"], artist["name"])

    def _update_artist(self, artist, timestamp):
        self._db.update_artist(artist["id"], timestamp)

    def _update_ranking(self, items, collection, range):
        ids = [item["id"] for item in items]
        self._db.add_ranking(self._timestamp, ids, collection, range)

    def _update_track_rankings(self):
        for range in ranges:
            top_tracks = self._get_top_tracks(range)
            self._update_ranking(top_tracks, Collection.TRACKS.value, range)
            for track in top_tracks:
                self._add_track(track)
                for artist in track["artists"]:
                    self._add_artist(artist)

    def _update_artist_rankings(self):
        for range in ranges:
            top_artists = self._get_top_artists(range)
            self._update_ranking(top_artists, Collection.ARTISTS.value, range)
            for artist in top_artists:
                self._add_artist(artist)

    def _update_recently_played(self):
        recently_played = reversed(self._get_recently_played())
        
        for play in recently_played:
            track = play["track"]
            timestamp = _timestamp_to_int(play["last_listened"])
            self._add_track(track)
            print(track["name"])
            for artist in track["artists"]:
                self._add_artist(artist)
                self._update_artist(artist, timestamp)
            self._db.update_track(track["id"], timestamp)

    def _update_timestamp(self):
        self._db.set_timestamp(self._timestamp)

    def update(self):
        # check connection and skip+log if unavailable
        
        self._timestamp = floor(time())
        self._create_ranking()
        self._update_track_rankings()
        self._update_artist_rankings()
        self._update_recently_played()
        self._update_timestamp()
