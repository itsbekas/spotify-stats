from datetime import datetime
from os import environ
from typing import Any, Dict, List

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
        """
        Authenticates the user using the SpotifyPKCE flow and returns a Spotipy client instance
        with the necessary access token for making API calls.

        Args:
            scope: The required scope(s) for the API call(s). Can be a string or list of strings.
                See the Spotify documentation for available scopes.

        Raises:
            Exception: If the required credentials are not set in the environment variables.

        Returns:
            A Spotipy client instance with the necessary access token for making API calls.
        """
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
                "Make sure SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET and SPOTIPY_REDIRECT_URI are defined in your environment!"
            )

        cache_handler = CacheFileHandler(cache_path=environ["SPOTIPY_CACHE_PATH"])
        auth = SpotifyPKCE(scope=scope, open_browser=False, cache_handler=cache_handler)
        auth.get_access_token()
        return Spotify(auth_manager=auth)

    def get_user_history(self, after: datetime):
        """
        Retrieves the user's listening history after the specified timestamp.

        Args:
            after (datetime or str): The timestamp after which to retrieve listening history. This can be either a
                datetime object or a string in ISO format (e.g. '2022-01-01T00:00:00Z').

        Returns:
            A list of dictionaries representing the user's listening history.
            Each dictionary has information about a single play, including its track and its timestamp

        Raises:
            ValueError: If the 'after' argument is not a valid datetime object or ISO string.
        """
        # Retrieve the user's listening history using the Spotify API
        timestamp = util.datetime_to_int(after)
        result = self._sp.current_user_recently_played(after=timestamp)

        return result.get("items", []) if result else {}

    def get_user_top_artists(self, range_type: str) -> List[Dict[str, Any]]:
        """
        Retrieves the user's top artists for a specified time range.

        Args:
            range_type: The time range for which to retrieve the user's top artists.
                Must be one of 'short_term', 'medium_term', or 'long_term'.

        Returns:
            A list of dictionaries containing the user's top artists for the specified time range.
            Each dictionary has information about a single artist, including its name, Spotify ID, and popularity.
        """
        result = self._sp.current_user_top_artists(time_range=range_type)

        return result.get("items", []) if result else []

    def get_user_top_tracks(self, range_type: str) -> List[Dict[str, Any]]:
        """
        Retrieves the user's top tracks for a specified time range.

        Args:
            range_type: The time range for which to retrieve the user's top tracks.
                Must be one of 'short_term', 'medium_term', or 'long_term'.

        Returns:
            A list of dictionaries containing the user's top tracks for the specified time range.
            Each dictionary has information about a single track, including its name, artist, Spotify ID, and popularity.
        """
        result = self._sp.current_user_top_tracks(limit=50, time_range=range_type)

        return result.get("items", []) if result else []
