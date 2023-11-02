from datetime import datetime
from os import environ

import spotifystats.core.database as db
import spotifystats.core.models.artist_ranking as a_rnk
import spotifystats.core.models.play as pl
import spotifystats.core.models.track_ranking as t_rnk
from spotifystats.core.service.spotify_api import SpotifyAPI


class SpotifyStatsService:
    timestamp: datetime

    def __init__(self):
        self.api = SpotifyAPI()

        mongodb_user = environ["SPOTIFYSTATS_MONGODB_USER"]
        if mongodb_user is None:
            raise ValueError("SPOTIFYSTATS_MONGODB_USER is not set")

        mongodb_password = environ.get("SPOTIFYSTATS_MONGODB_PASSWORD")
        if mongodb_password is None:
            raise ValueError("SPOTIFYSTATS_MONGODB_PASSWORD is not set")
        
        mongodb_host = environ.get("SPOTIFYSTATS_MONGODB_HOST")
        if mongodb_host is None:
            raise ValueError("SPOTIFYSTATS_MONGODB_HOST is not set")

        mongodb_port = environ.get("SPOTIFYSTATS_MONGODB_PORT")
        if mongodb_port is None:
            raise ValueError("SPOTIFYSTATS_MONGODB_PORT is not set")

        mongodb_db_name = environ.get("SPOTIFYSTATS_MONGODB_DB_NAME")
        if mongodb_name is None:
            raise ValueError("SPOTIFYSTATS_MONGODB_DB_NAME is not set")


        mongodb_uri = f"mongodb://{mongodb_user}:{mongodb_password}@{mongodb_host}:{mongodb_port}/{mongodb_db_name}"

        db.connect(
            name=mongodb_name,
            host=mongodb_uri,
            uuidRepresentation="standard",
        )

    def update(self) -> None:
        self.timestamp = datetime.now()
        self.update_rankings()
        self.update_history()
        print("Finished updating:", self.timestamp)

    def update_rankings(self) -> None:
        for range_type in ["short_term", "medium_term", "long_term"]:
            self.update_artist_rankings(range_type)
            self.update_track_rankings(range_type)

    def update_artist_rankings(self, time_range: str) -> None:
        top_artists = self.api.get_user_top_artists(time_range)

        rank_dict = {
            "artists": top_artists,
            "time_range": time_range,
            "timestamp": self.timestamp,
        }

        rank = a_rnk.ArtistRanking.from_spotify_response(rank_dict)
        db.add_artist_ranking(rank)

    def update_track_rankings(self, time_range: str) -> None:
        top_tracks = self.api.get_user_top_tracks(time_range)

        rank_dict = {
            "tracks": top_tracks,
            "time_range": time_range,
            "timestamp": self.timestamp,
        }

        rank = t_rnk.TrackRanking.from_spotify_response(rank_dict)
        db.add_track_ranking(rank)

    def update_history(self) -> None:
        latest_timestamp = db.get_latest_timestamp()
        history = self.api.get_user_history(latest_timestamp)

        for play_dict in history:
            play = pl.Play.from_spotify_response(play_dict)
            db.add_play(play)
