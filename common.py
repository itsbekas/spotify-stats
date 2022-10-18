import os 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyStats():

    def __init__(self):
        __client = self.get_client()
        __db = self.get_db()

    def get_client(self):
        if not all(env in os.environ for env in ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIPY_REDIRECT_URI"]):
            raise Exception("Make sure SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET and SPOTIPY_REDIRECT_URI are defined in your environment!")
        return spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    def get_db(self):
        pass
