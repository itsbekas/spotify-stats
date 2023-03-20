from __future__ import annotations

from typing import TYPE_CHECKING, List

from mongoengine.fields import ListField, ReferenceField

import spotifystats.models.track as trk
from spotifystats.models.ranking import Ranking


class TrackRanking(Ranking):

    tracks = ListField(ReferenceField("Track"))

    @classmethod
    def from_spotify_response(cls, response) -> TrackRanking:

        tracks = [trk.Track.from_spotify_response(track) for track in response]

        return cls(tracks=tracks)

    def get_tracks(self) -> List[trk.Track]:
        return self.tracks
