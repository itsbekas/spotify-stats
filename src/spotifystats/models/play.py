from __future__ import annotations

from mongoengine.fields import IntField, ReferenceField

import spotifystats.models.track as trk
import spotifystats.util as util
from spotifystats.models.dated_document import DatedDocument


class Play(DatedDocument):
    track: trk.Track = ReferenceField("Track")
    ms_played: int = IntField()
    meta = {"collection": "plays"}

    @classmethod
    def from_spotify_response(cls, response) -> Play:
        track = trk.Track.from_spotify_response(response["track"])
        timestamp = util.iso_to_datetime(response["played_at"])
        ms_played = response["ms_played"]

        return cls(track=track, timestamp=timestamp, ms_played=ms_played)

    def get_track(self) -> trk.Track:
        return self.track

    def set_track(self, track: trk.Track) -> None:
        self.track = track
