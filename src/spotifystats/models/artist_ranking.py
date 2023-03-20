from __future__ import annotations

from typing import TYPE_CHECKING, List

from mongoengine.fields import ListField, ReferenceField

import spotifystats.models.artist as art
from spotifystats.models.ranking import Ranking


class ArtistRanking(Ranking):

    artists = ListField(ReferenceField("Artist"))

    @classmethod
    def from_spotify_response(cls, response) -> ArtistRanking:

        artists = [art.Artist.from_spotify_response(artist) for artist in response]

        return cls(artists=artists)

    def get_artists(self) -> List[art.Artist]:
        return self.artists
