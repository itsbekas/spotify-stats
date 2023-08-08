from __future__ import annotations

from typing import TYPE_CHECKING, List

from mongoengine.fields import IntField, ListField, ReferenceField, StringField

from spotifystats.core.models.named_document import NamedDocument
from spotifystats.core.util.lists import RankingDocumentList

if TYPE_CHECKING:
    import spotifystats.core.models.artist_ranking as a_rnk


class Artist(NamedDocument):
    popularity: int = IntField(default=-1)
    play_count: int = IntField(default=0)
    genres: List[str] = ListField(StringField())
    rankings: List[a_rnk.ArtistRanking] = ListField(ReferenceField("ArtistRanking"))
    meta = {"collection": "artists", "indexes": ["play_count"]}

    @classmethod
    def from_spotify_response(cls, response) -> Artist:
        popularity = response["popularity"] if "popularity" in response else -1
        genres = response["genres"] if "genres" in response else []

        return cls(
            spotify_id=response["id"],
            name=response["name"],
            popularity=popularity,
            genres=genres,
        )

    def get_rankings(self) -> List[a_rnk.ArtistRanking]:
        return RankingDocumentList(self.rankings)

    def add_ranking(self, ranking: a_rnk.ArtistRanking) -> None:
        if ranking not in self.get_rankings():
            if self in ranking.get_artists():
                self.rankings.append(ranking)

    def get_genres(self) -> List[str]:
        return self.genres

    def add_genre(self, genre: str) -> None:
        self.genres.append(genre)

    def get_popularity(self) -> int:
        return self.popularity

    def set_popularity(self, popularity: int) -> None:
        self.popularity = popularity

    def get_play_count(self) -> int:
        return self.play_count

    def increment_play_count(self) -> None:
        self.play_count += 1
