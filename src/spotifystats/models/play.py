from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING, List

from mongoengine.fields import DateTimeField, ReferenceField

from spotifystats.models.timed_document import TimedDocument

import spotifystats.models.track as trk

import spotifystats.util as util


class Play(TimedDocument):
    track = ReferenceField("Track")

    def get_track(self) -> trk.Track:
        return self.track

    @classmethod
    def from_spotify_response(cls, response) -> Play:
        return cls(
            track=trk.Track.from_spotify_response(response["track"]),
            timestamp=util.iso_to_datetime(response["played_at"]),
        )
