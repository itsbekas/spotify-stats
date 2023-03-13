from datetime import datetime

import spotifystats.database as db
import spotifystats.models.ranking as rnk
import spotifystats.models.play as pl
from spotifystats.service.spotify_api import SpotifyAPI


class SpotifyStatsService:

    timestamp: datetime

    def __init__(self):
        self.api = SpotifyAPI()
        db.connect("spotify-stats")

    def update(self) -> None:
        self.timestamp = datetime.now()
        self.update_rankings()
        self.update_history()
        self.update_timestamp()

    def update_rankings(self) -> None:
        for range_type in ["short_term", "medium_term", "long_term"]:
            self.update_artist_rankings(range_type)
            self.update_track_rankings(range_type)

    def update_artist_rankings(self, range_type) -> None:
        top_artists = self.api.get_user_top_artists(range_type)

        rnk.Ranking.from_spotify_response(top_artists)

    def update_track_rankings(self, range_type) -> None:
        top_tracks = self.api.get_user_top_tracks(range_type)

    def update_history(self) -> None:
        ts = db.get_current_timestamp()
        history = self.api.get_user_history(ts)

        for play_dict in history:
            play = pl.Play.from_spotify_response(play_dict)
        print(play)

    def update_timestamp(self) -> None:
        #! TESTING ONLY
        db.update_config_timestamp(datetime(2023, 3, 13, 11, 0, 0))
        # db.update_config_timestamp(self.timestamp)
