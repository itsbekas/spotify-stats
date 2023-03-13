from spotifystats.service.spotify_api import SpotifyAPI

from spotifystats.models.config import Config

import spotifystats.database as db 

from datetime import datetime

class SpotifyStatsService:

    timestamp: datetime

    def __init__(self):
        self.api = SpotifyAPI()

    def update(self):
        self.timestamp = datetime.now()
        self.update_rankings()
        self.update_timestamp()

    def update_rankings(self):
        self.update_artist_rankings()
        self.update_track_rankings()

    def update_artist_rankings(self):
        top_artists = self.api.get_user_top_artists()

    def update_track_rankings(self):
        top_tracks = self.api.get_user_top_tracks()

    def update_history(self):
        pass

    def update_timestamp(self) -> None:
        db.update_config_timestamp(self.timestamp)
