from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING, List

from mongoengine.fields import DateTimeField, ReferenceField

import spotifystats.database as db
import spotifystats.models.track as trk
import spotifystats.util as util
from spotifystats.models.dated_document import DatedDocument


class Play(DatedDocument):
    track = ReferenceField("Track")

    def get_track(self) -> trk.Track:
        return self.track

    @classmethod
    def from_spotify_response(cls, response) -> Play:

        track = db.get_track(response["track"]["id"])
        if track is None:
            track = trk.Track.from_spotify_response(response["track"])
            db.add_track(track)

        return cls(track=track, timestamp=util.iso_to_datetime(response["played_at"]))
