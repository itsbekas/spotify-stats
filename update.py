import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

scope = 'user-top-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_top_tracks(limit=50)

for idx, item in enumerate(results['items']):
    artist = item['artists'][0]['name']
    track = item['name']
    trackid = item['id']
    print(idx+1, ':', artist, '-', track, '(' + trackid + ')')
