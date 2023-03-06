from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING, List

from mongoengine.fields import DateTimeField, ReferenceField

from spotifystats.models.spotifystatsdocument import SpotifyStatsDocument

if TYPE_CHECKING:
    import spotifystats.models.track as trk

class Play(SpotifyStatsDocument):
    timestamp = DateTimeField(primary_key=True)
    track = ReferenceField("Track")

    def get_timestamp(self) -> dt.datetime:
        return self.timestamp
    
    def get_tracks(self) -> List[trk.Track]:
        return self.tracks
    
