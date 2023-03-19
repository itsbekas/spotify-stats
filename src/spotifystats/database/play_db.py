from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

import spotifystats.database as db
import spotifystats.models.play as pl


def add_play(play: pl.Play) -> None:
    if get_play(play.get_timestamp()) is None:

        track = play.get_track()
        db_track = db.get_track(track.get_id())
        if db_track is None:
            db.add_track(track)
        else:
            play.set_track(db_track)

        play.save()


def get_play(timestamp: dt.datetime) -> pl.Play:
    return pl.Play.objects(timestamp=timestamp).first()


# todo: test to make sure order is correct -> add older, add latest, add older then check if latest is the first one
def get_latest_timestamp() -> dt.datetime:
    latest_play = pl.Play.objects().first()
    if latest_play is None:
        return dt.datetime.now() - dt.timedelta(minutes=1000)
    return latest_play.get_timestamp()
