from os import environ
from typing import Any, Optional, Union

from spotipy import Spotify
from spotipy.cache_handler import CacheFileHandler
from spotipy.oauth2 import SpotifyPKCE


class SpotifyAPI:
    def __init__(self, scope):
        self.sp = self._auth(scope)

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

    def get_user_history(self, after: int) -> Optional[dict[str, str]]:
        """
        Retrieves the user's listening history after the specified timestamp.

        Args:
            after: The timestamp (in milliseconds) from which to retrieve the listening history.

        Returns:
            A dictionary containing the user's listening history after the specified timestamp.
            The dictionary has the following keys: 'items', 'next', 'cursors', and 'limit'.
        """
        pass  # TODO: Implement this method

    def get_user_top_artists(self, range_type: str) -> Optional[dict[str, str]]:
        """
        Retrieves the user's top artists for a specified time range.

        Args:
            range_type: The time range for which to retrieve the user's top artists.
                Must be one of 'short_term', 'medium_term', or 'long_term'.

        Returns:
            A dictionary containing the user's top artists for the specified time range.
            The dictionary has the following keys: 'items', 'total', 'limit', 'offset',
            'previous', and 'next'.
        """
        return self.sp.current_user_top_artists(time_range=range_type)

    def get_user_top_tracks(self, range_type: str) -> Union[dict[str, Any], None]:
        """
        Retrieves the user's top tracks for a specified time range.

        Args:
            range_type: The time range for which to retrieve the user's top tracks.
                Must be one of 'short_term', 'medium_term', or 'long_term'.

        Returns:
            A dictionary containing the user's top tracks for the specified time range.
            The dictionary has the following keys: 'items', 'total', 'limit', 'offset',
            'previous', and 'next'.
        """
        return self.sp.current_user_top_tracks(time_range=range_type)
