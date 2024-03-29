from __future__ import annotations

import datetime as dt

import spotifystats.core.database as db
import spotifystats.core.models.play as pl


def add_play(play: pl.Play) -> None:
    if get_play(play.get_timestamp()) is None:
        track = play.get_track()
        db_track = db.get_track(track.get_id())
        if db_track is None:
            db.add_track(track)
        else:
            play.set_track(db_track)

        play.save()

        # Add play to track
        track = play.get_track()
        track.increment_play_count()
        track.save()

        for artist in track.get_artists():
            artist.increment_play_count()
            artist.save()


def get_play(timestamp: dt.datetime) -> pl.Play:
    return pl.Play.objects(timestamp=timestamp).first()


def get_plays_in_range(
    start: dt.datetime, end: dt.datetime, limit: int = 0
) -> list[pl.Play]:
    return (
        pl.Play.objects(timestamp__gte=start, timestamp__lte=end)
        .order_by("-timestamp")
        .limit(limit)
    )


# todo: test to make sure order is correct
# add older, add latest, add older then check if latest is the first one
def get_latest_timestamp() -> dt.datetime:
    latest_play = pl.Play.objects().first()
    if latest_play is None:
        return dt.datetime.now() - dt.timedelta(minutes=1000)
    return latest_play.get_timestamp()
