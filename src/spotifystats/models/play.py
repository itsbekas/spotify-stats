from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING, List

from mongoengine.fields import DateTimeField, ReferenceField

from spotifystats.models.timed_document import TimedDocument

import spotifystats.models.track as trk

import spotifystats.util as util


class Play(TimedDocument):
    track = ReferenceField("Track")

    def get_tracks(self) -> List[trk.Track]:
        return self.tracks
    
    @classmethod
    def from_spotify_response(cls, response) -> Play:
        cls(
            track = trk.Track.from_spotify_response(response["track"]),
            timestamp = util.iso_to_datetime(response["played_at"])
        )
