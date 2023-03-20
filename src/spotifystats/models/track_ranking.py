from __future__ import annotations

from typing import TYPE_CHECKING, List, Dict, Any

from mongoengine.fields import ListField, ReferenceField

import spotifystats.models.track as trk
from spotifystats.models.ranking import Ranking


class TrackRanking(Ranking):

    tracks = ListField(ReferenceField("Track"))

    @classmethod
    def from_spotify_response(cls, rank_dict: Dict[str, Any]) -> TrackRanking:

        tracks = [
            trk.Track.from_spotify_response(track) for track in rank_dict["tracks"]
        ]

        return cls(
            timestamp=rank_dict["timestamp"],
            time_range=rank_dict["time_range"],
            tracks=tracks,
        )

    def get_tracks(self) -> List[trk.Track]:
        return self.tracks
