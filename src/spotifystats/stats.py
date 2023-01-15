from math import floor
from os import environ
from time import sleep, time

import spotipy
from dateutil.parser import parse
from spotipy.oauth2 import SpotifyPKCE
from spotipy.cache_handler import CacheFileHandler

from spotifystats.database import Database, Collection
from spotifystats.model.artist import Artist
from spotifystats.model.track import Track
from spotifystats.model.play import Play
from spotifystats.model.history import History

ranges = ["short_term", "medium_term", "long_term"]

def _extract_track(track: dict) -> Track:
    """Extracts the relevant info from a track"""
    return {
        "id": track["id"],
        "name": track["name"],
        "artists": [{"id": artist["id"], "name": artist["name"]} for artist in track["artists"]]
    }

def _extract_artist(artist: dict) -> dict:
    """Extracts the relevant info from an artist"""
    return {
        "id": artist["id"],
        "name": artist["name"]
    }

def _extract_play(play: dict) -> Play:
    """Creates a Play object from a Spotify response dictionary"""
    return {
        "track": _extract_track(play["track"]),
        "artists": [_extract_artist(artist) for artist in play["track"]["artists"]],
        "played_at": _timestamp_to_int(play["played_at"]),
        "popularity": play["track"]["popularity"]
    }

def _plays_to_history(plays: list[Play]) -> History:
    """Converts plays created by _extract_play to an history array"""
    return [{
        "track": play["track"]["id"],
        "artists": [artist["id"] for artist in play["artists"]],
        "played_at": play["played_at"],
        "popularity": play["popularity"]
    } for play in plays]

def _timestamp_to_int(timestamp: str) -> int:
    return floor(parse(timestamp, "").timestamp())

class SpotifyStats:

    def __init__(self) -> None:
        scope = ["user-top-read", "user-read-recently-played"]
        self._timestamp = 0
        self._sp = self._auth(scope)
        self._db = Database(environ["SPOTIFYSTATS_MONGODB_DB_NAME"])

    def _auth(self, scope: list[str] | str) -> None:
        # Make sure credentials are set
        if not all(env in environ for env in ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIPY_REDIRECT_URI"]):
            raise Exception("Make sure SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET and SPOTIPY_REDIRECT_URI are defined in your environment!")

        cache_handler = CacheFileHandler(cache_path=environ["SPOTIPY_CACHE_PATH"])
        auth = SpotifyPKCE(scope=scope, open_browser=False, cache_handler=cache_handler)
        auth.get_access_token()
        return spotipy.Spotify(auth_manager=auth)

    def _get_top_tracks(self, range) -> None:
        tracks = self._sp.current_user_top_tracks(limit=50, offset=0, time_range=range)["items"]
        return [_extract_track(track) for track in tracks]

    def _get_top_artists(self, range) -> None:
        artists = self._sp.current_user_top_artists(limit=50, offset=0, time_range=range)["items"]
        return [_extract_artist(artist) for artist in artists]

    def _get_recently_played(self) -> None:
        timestamp = self._db.get_timestamp()*1000 # Timestamp must be in milliseconds
        tracks = self._sp.current_user_recently_played(limit=50, after=timestamp)["items"]
        return list(reversed([_extract_play(track) for track in tracks]))

    def _create_ranking(self) -> None:
        self._db.create_ranking(self._timestamp)

    def _add_track(self, track: Track, timestamp: int = 0) -> None:
        artists = [artist["id"] for artist in track["artists"]]
        self._db.add_track(track["id"], track["name"], artists)

    def _add_tracks(self, tracks: list[Track]) -> None:
        for track in tracks:
            self._add_track(track)
            for artist in track["artists"]:
                self._add_artist(artist)

    def _add_artist(self, artist: Artist) -> None:
        self._db.add_artist(artist["id"], artist["name"])

    def _add_artists(self, artists: Artist) -> None:
        for artist in artists:
            self._add_artist(artist)

    def _update_artist(self, artist: Artist, timestamp) -> None:
        self._db.update_artist(artist["id"], timestamp)

    def _update_track(self, track: Track, timestamp) -> None:
        self._db.update_track(track["id"], timestamp)

    def _update_track_rankings(self) -> None:
        for range in ranges:
            top_tracks = self._get_top_tracks(range)
            self._update_ranking(top_tracks, Collection.TRACKS.value, range)
            self._add_tracks(top_tracks)

    def _update_ranking(self, items, collection, range) -> None:
        ids = [item["id"] for item in items]
        self._db.add_ranking(self._timestamp, ids, collection, range)

    def _update_artist_rankings(self) -> None:
        for range in ranges:
            top_artists = self._get_top_artists(range)
            self._update_ranking(top_artists, Collection.ARTISTS.value, range)
            self._add_artists(top_artists)

    def _update_play(self, play: Play) -> None:
        track = play["track"]
        timestamp = play["played_at"]
        self._add_track(track)
        self._update_track(track, timestamp)
        for artist in play["artists"]:
            self._add_artist(artist)
            self._update_artist(artist, timestamp)

    def _add_history(self, history) -> None:
        self._db.add_history(history, self._timestamp)

    def _update_recently_played(self) -> None:
        recently_played = self._get_recently_played()
        history = _plays_to_history(recently_played)
        self._add_history(history)
        for play in recently_played:
            self._update_play(play)

    def _update_timestamp(self) -> None:
        self._db.set_timestamp(self._timestamp)

    def update(self) -> None:
        # check connection and skip+log if unavailable
        
        self._timestamp = floor(time())
        self._create_ranking()
        self._update_track_rankings()
        self._update_artist_rankings()
        self._update_recently_played()
        self._update_timestamp()
