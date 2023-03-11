from spotifystats.service.spotify_api import SpotifyAPI

from spotifystats.models.config import Config

import spotifystats.database as db 

from datetime import datetime

class SpotifyStatsService:
    def __init__(self):
        self.api = SpotifyAPI()

    def update(self):
        timestamp = datetime.now()
        
        Config.set_last_updated(timestamp)

