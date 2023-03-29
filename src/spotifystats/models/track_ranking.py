from __future__ import annotations

from typing import Any, Dict, List

from mongoengine.fields import ListField, ReferenceField

import spotifystats.models.track as trk
from spotifystats.models.ranking import Ranking
from spotifystats.util import iso_to_datetime
from spotifystats.util.lists import NamedDocumentList


class TrackRanking(Ranking):
    tracks = ListField(ReferenceField("Track"))

    @classmethod
    def from_spotify_response(cls, rank_dict: Dict[str, Any]) -> TrackRanking:
        timestamp = iso_to_datetime(rank_dict["timestamp"])

        tracks = [
            trk.Track.from_spotify_response(track) for track in rank_dict["tracks"]
        ]

        return cls(
            timestamp=timestamp,
            time_range=rank_dict["time_range"],
            tracks=tracks,
        )

    def get_tracks(self) -> List[trk.Track]:
        return NamedDocumentList(self.tracks)
