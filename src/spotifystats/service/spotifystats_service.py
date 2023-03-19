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

    def update_rankings(self) -> None:
        for range_type in ["short_term", "medium_term", "long_term"]:
            self.update_artist_rankings(range_type)
            self.update_track_rankings(range_type)

    def update_artist_rankings(self, range_type) -> None:
        top_artists = self.api.get_user_top_artists(range_type)
        print(top_artists[0])

        rnk.Ranking.from_spotify_response(top_artists)

    def update_track_rankings(self, range_type) -> None:
        top_tracks = self.api.get_user_top_tracks(range_type)

    def update_history(self) -> None:
        latest_timestamp = db.get_latest_timestamp()
        history = self.api.get_user_history(latest_timestamp)

        for play_dict in history:
            play = pl.Play.from_spotify_response(play_dict)
            db.add_play(play)
