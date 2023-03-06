from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING, List

from mongoengine.fields import DateTimeField, ReferenceField

from spotifystats.models.timed_document import TimedDocument

if TYPE_CHECKING:
    import spotifystats.models.track as trk

class Play(TimedDocument):
    track = ReferenceField("Track")

    def get_timestamp(self) -> dt.datetime:
        return self.timestamp
    
    def get_tracks(self) -> List[trk.Track]:
        return self.tracks
    
