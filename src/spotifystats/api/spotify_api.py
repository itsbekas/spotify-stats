from ..model import Artist, Track


class SpotifyAPI:
    def get_top_artists(self, range="medium_term"):
        result = self.sp.current_user_top_artists(limit=50, time_range=range)
        artists = [Artist.from_spotify_response(item) for item in result["items"]]
        return artists

    def get_top_tracks(self, range="medium_term"):
        result = self.sp.current_user_top_tracks(limit=50, time_range=range)
        tracks = [Track.from_spotify_response(item) for item in result["items"]]
        return tracks
