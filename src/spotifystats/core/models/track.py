from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    import spotifystats.core.models.track_ranking as t_rnk

from mongoengine.fields import IntField, ListField, ReferenceField

import spotifystats.core.models.album as alb
import spotifystats.core.models.artist as art
from spotifystats.core.models.named_document import NamedDocument
from spotifystats.core.util.lists import NamedDocumentList, RankingDocumentList


class Track(NamedDocument):
    album: alb.Album = ReferenceField("Album")
    artists: List[art.Artist] = ListField(ReferenceField("Artist"))
    popularity: int = IntField(default=-1)
    plays = IntField(default=0)
    rankings: List[t_rnk.TrackRanking] = ListField(ReferenceField("TrackRanking"))
    meta = {"collection": "tracks"}

    @classmethod
    def from_spotify_response(cls, response) -> Track:
        album = (
            alb.Album.from_spotify_response(response["album"])
            if "album" in response
            else None
        )

        artists = (
            [
                art.Artist.from_spotify_response(artist_response)
                for artist_response in response["artists"]
            ]
            if "artists" in response
            else []
        )

        popularity = response["popularity"] if "popularity" in response else None

        return cls(
            spotify_id=response["id"],
            name=response["name"],
            album=album,
            artists=artists,
            popularity=popularity,
        )

    def get_album(self) -> alb.Album:
        return self.album

    def set_album(self, album: alb.Album) -> None:
        self.album = album

    def get_artists(self) -> List[art.Artist]:
        return NamedDocumentList(self.artists)

    def set_artist(self, index: int, artist: art.Artist) -> None:
        self.artists[index] = artist

    def get_popularity(self) -> int:
        return self.popularity

    def increment_plays(self) -> None:
        self.plays += 1

    def get_rankings(self) -> List[t_rnk.TrackRanking]:
        return RankingDocumentList(self.rankings)

    def add_ranking(self, ranking: t_rnk.TrackRanking) -> None:
        if ranking not in self.get_rankings():
            if self in ranking.get_tracks():
                self.rankings.append(ranking)
