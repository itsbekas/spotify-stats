import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from google.cloud import firestore
import config as *

# Global variables

def spotify_test():
    results = sp.current_user_top_tracks(limit=50)

    for idx, item in enumerate(results['items']):
        artist = item['artists'][0]['name']
        track = item['name']
        trackid = item['id']
        print(idx+1, ':', artist, '-', track, '(' + trackid + ')')


if __name__ == '__main__':
    
    # Load environment variables stored in .env
    load_dotenv()
    print("Credentials loaded.")

    # Connect to Firestore
    db = firestore.Client(project=firebase_project)
    print("Connected to Firestore.")

    # Connect to Spotify
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=spotify_scopes))
    print("Connected to Spotify.")

