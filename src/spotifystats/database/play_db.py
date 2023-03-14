from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime

import spotifystats.database as db
import spotifystats.models.play as play


def add_play(play: play.Play) -> None:
    if get_play(play.get_timestamp()) is None:

        track = play.get_track()
        db.add_track(track)

        play.save()


def get_play(timestamp: datetime) -> play.Play:
    return play.Play.objects(timestamp=timestamp).first()