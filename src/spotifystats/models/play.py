from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING, List

from mongoengine.fields import ReferenceField

import spotifystats.models.track as trk
import spotifystats.util as util
from spotifystats.models.dated_document import DatedDocument


class Play(DatedDocument):
    track = ReferenceField("Track")

    @classmethod
    def from_spotify_response(cls, response) -> Play:

        track = trk.Track.from_spotify_response(response["track"])

        return cls(track=track, timestamp=util.iso_to_datetime(response["played_at"]))

    def get_track(self) -> trk.Track:
        return self.track

    def set_track(self, track: trk.Track) -> None:
        self.track = track
