import os 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_client():
    if not (os.getenv("SPOTIPY_CLIENT_ID") and os.getenv("SPOTIPY_CLIENT_SECRET")):
        raise("Make sure SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET are defined in your environment!")
    return spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
