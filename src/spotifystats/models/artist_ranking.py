from __future__ import annotations

from typing import Any, Dict, List

from mongoengine.fields import ListField, ReferenceField

import spotifystats.models.artist as art
from spotifystats.models.ranking import Ranking
from spotifystats.util.lists import NamedDocumentList


class ArtistRanking(Ranking):
    artists = ListField(ReferenceField("Artist"))

    @classmethod
    def from_spotify_response(cls, rank_dict: Dict[str, Any]) -> ArtistRanking:
        artists = [
            art.Artist.from_spotify_response(artist) for artist in rank_dict["artists"]
        ]

        return cls(
            timestamp=rank_dict["timestamp"],
            time_range=rank_dict["time_range"],
            artists=artists,
        )

    def get_artists(self) -> List[art.Artist]:
        return NamedDocumentList(self.artists)
