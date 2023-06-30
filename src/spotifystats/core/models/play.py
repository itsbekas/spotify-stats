from __future__ import annotations

from mongoengine.fields import ReferenceField

import spotifystats.core.models.track as trk
import spotifystats.core.util as util
from spotifystats.core.models.dated_document import DatedDocument


class Play(DatedDocument):
    track: trk.Track = ReferenceField("Track")
    meta = {"collection": "plays"}

    @classmethod
    def from_spotify_response(cls, response) -> Play:
        track = trk.Track.from_spotify_response(response["track"])
        timestamp = util.iso_to_datetime(response["played_at"])

        return cls(track=track, timestamp=timestamp)

    def get_track(self) -> trk.Track:
        return self.track

    def set_track(self, track: trk.Track) -> None:
        self.track = track
