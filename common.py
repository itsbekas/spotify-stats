import os 
import spotipy
import database
from spotipy.oauth2 import SpotifyPKCE

ranges = ["short_term", "medium_term", "long_term"]

def __extract_track(track):
    '''Extracts the relevant info from a track'''
    return {
        "id": track["id"],
        "name": track["name"],
        "artists": [artist["id"] for artist in track["artists"]]
    }

class SpotifyStats:

    def __init__(self):

        scope = ["user-top-read", "user-read-recently-played"]

        self.__sp = self.__auth(scope)
        self.__db = database.Database()

    def __auth(self, scope):
        # Make sure credentials are set
        if not all(env in os.environ for env in ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIPY_REDIRECT_URI"]):
            raise Exception("Make sure SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET and SPOTIPY_REDIRECT_URI are defined in your environment!")

        auth = SpotifyPKCE(scope=scope, open_browser=False)
        auth.get_access_token()
        return spotipy.Spotify(auth_manager=auth)

    def __update_tracks(self):
        for range in ranges:
            tracks = self.__sp.current_user_top_tracks(limit=50, offset=0, time_range=range)["items"]
            for track in tracks:
                print(__extract_track(track))

    def __update_artists(self):
        pass


    def update(self):
        self.__update_tracks()
        self.__update_artists()


    def test(self):
        print(self.__sp.current_user_top_tracks())
