from math import floor
from os import environ
from time import sleep, time

import spotipy
from dateutil.parser import parse
from spotipy.oauth2 import SpotifyPKCE

import spotifystats.database as database

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

class SpotifyStats:

    def __init__(self):
        scope = ["user-top-read", "user-read-recently-played"]
        self.__timestamp = 0
        self.__sp = self.__auth(scope)
        self.__db = database.Database("spotify-stats")

    def __auth(self, scope):
        # Make sure credentials are set
        if not all(env in environ for env in ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIPY_REDIRECT_URI"]):
            raise Exception("Make sure SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET and SPOTIPY_REDIRECT_URI are defined in your environment!")

        auth = SpotifyPKCE(scope=scope, open_browser=False)
        auth.get_access_token()
        return spotipy.Spotify(auth_manager=auth)

    def __get_top_tracks(self, range):
        tracks = self.__sp.current_user_top_tracks(limit=50, offset=0, time_range=range)["items"]
        return [_extract_track(track) for track in tracks]

    def __get_top_artists(self, range):
        artists = self.__sp.current_user_top_artists(limit=50, offset=0, time_range=range)["items"]
        return [_extract_artist(artist) for artist in artists]

    def __get_recently_played(self):
        timestamp = self.__timestamp*1000 # Timestamp must be in milliseconds
        tracks = self.__sp.current_user_recently_played(limit=50, after=timestamp)["items"]
        return [{
                "track": _extract_track(track["track"]),
                "last_listened": track["played_at"]
            } for track in tracks]

    def __create_ranking(self):
        self.__db.create_ranking(self.__timestamp)

    def __update_track(self, track, timestamp=0):
        artists = [artist["id"] for artist in track["artists"]]
        self.__db.add_track(track["id"], track["name"], artists)
        if (timestamp):
            self.__db.update_track(track["id"], timestamp)

    def __update_artist(self, artist):
        self.__db.add_artist(artist["id"], artist["name"])

    def __update_ranking(self, items, collection, range):
        ids = [item["id"] for item in items]
        self.__db.add_ranking(self.__timestamp, ids, collection, range)

    def __update_tracks(self):
        for range in ranges:
            top_tracks = self.__get_top_tracks(range)
            self.__update_ranking(top_tracks, "tracks", range)
            for track in top_tracks:
                self.__update_track(track)
                for artist in track["artists"]:
                    self.__update_artist(artist)

    def __update_artists(self):
        for range in ranges:
            top_artists = self.__get_top_artists(range)
            self.__update_ranking(top_artists, "artists", range)
            for artist in top_artists:
                self.__update_artist(artist)

    def __update_play_count(self):
        tracks = self.__get_recently_played()
        for track in tracks:
            last_listened = floor(parse(track["last_listened"], "").timestamp())
            self.__update_track(track["track"], track["last_listened"])

    def update(self):
        # check connection and skip+log if unavailable
        
        #self.__update_play_count()
        
        self.__timestamp = floor(time())
        self.__create_ranking()
        self.__update_tracks()
        self.__update_artists()
