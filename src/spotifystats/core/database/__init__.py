from mongoengine import connect, disconnect

from spotifystats.core.database.album_db import add_album, get_album
from spotifystats.core.database.artist_db import add_artist, get_artist, get_top_artists
from spotifystats.core.database.play_db import add_play, get_latest_timestamp, get_play
from spotifystats.core.database.ranking_db import add_artist_ranking, add_track_ranking
from spotifystats.core.database.track_db import add_track, get_track

__all__ = [
    "connect",
    "disconnect",
    "add_album",
    "get_album",
    "add_artist",
    "get_artist",
    "get_top_artists",
    "add_play",
    "get_play",
    "get_latest_timestamp",
    "add_artist_ranking",
    "add_track_ranking",
    "add_track",
    "get_track",
]
