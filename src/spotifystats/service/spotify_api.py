from datetime import datetime
from os import environ
from typing import Any, Dict

from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.cache_handler import CacheFileHandler
from spotipy.oauth2 import SpotifyPKCE

import spotifystats.util as util


class SpotifyAPI:
    def __init__(self):
        scope = ["user-top-read", "user-read-recently-played"]
        self._sp = self._auth(scope)

    def _auth(self, scope: list[str] | str) -> Spotify:
        load_dotenv()
        if not all(
            env in environ
            for env in [
                "SPOTIPY_CLIENT_ID",
                "SPOTIPY_CLIENT_SECRET",
                "SPOTIPY_REDIRECT_URI",
            ]
        ):
            raise Exception(
                (
                    "Make sure SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET"
                    "and SPOTIPY_REDIRECT_URI are defined in your environment!"
                )
            )

        cache_handler = CacheFileHandler(cache_path=environ["SPOTIPY_CACHE_PATH"])
        auth = SpotifyPKCE(scope=scope, open_browser=False, cache_handler=cache_handler)
        auth.get_access_token()
        return Spotify(auth_manager=auth)

    def get_user_history(self, after: datetime) -> Dict[str, Any]:
        # Retrieve the user's listening history using the Spotify API
        timestamp = util.datetime_to_int(after)
        result = self._sp.current_user_recently_played(limit=50, after=timestamp)

        return result.get("items", []) if result else {}

    def get_user_top_artists(self, range_type: str) -> Dict[str, Any] | None:
        result = self._sp.current_user_top_artists(limit=50, time_range=range_type)

        return result.get("items", []) if result else {}

    def get_user_top_tracks(self, range_type: str) -> Dict[str, Any] | None:
        result = self._sp.current_user_top_tracks(limit=50, time_range=range_type)

        return result.get("items", []) if result else {}

    def search_track(self, track: str, artist: str) -> Dict[str, Any] | None:

        query = f"track:{track} artist:{artist}"

        result = self._sp.search(
            q=query, limit=1, type="track"
        )

        return {
            "track": result.get("tracks", {}).get("items", []),
            "next": result.get("tracks", {}).get("next")
        }

    
    def get_next(self, result) -> Dict[str, Any] | None:
        result = self._sp.next(result)

        return {
            "track": result.get("tracks", {}).get("items", []),
            "next": result.get("tracks", {}).get("next")
        }
