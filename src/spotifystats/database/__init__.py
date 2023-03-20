from mongoengine import connect

from spotifystats.database.album_db import add_album, get_album
from spotifystats.database.artist_db import add_artist, get_artist
from spotifystats.database.play_db import add_play, get_latest_timestamp, get_play
from spotifystats.database.ranking_db import add_artist_ranking, add_track_ranking
from spotifystats.database.track_db import add_track, get_track

__all__ = [
    "connect",
    "add_album",
    "get_album",
    "add_artist",
    "get_artist",
    "add_play",
    "get_play",
    "get_latest_timestamp",
    "add_artist_ranking",
    "add_track_ranking",
    "add_track",
    "get_track",
]
