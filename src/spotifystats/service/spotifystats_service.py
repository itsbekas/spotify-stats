from spotifystats.service.spotify_api import SpotifyAPI


class SpotifyStatsService:
    def __init__(self):
        self.api = SpotifyAPI()

    def get_current_ranking(self, type, range):
        # get last ranking from db (sort by timestamp and limit=1)
        pass

