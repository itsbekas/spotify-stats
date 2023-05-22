from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    import spotifystats.models.play as pl
    import spotifystats.models.track_ranking as t_rnk

from mongoengine.fields import IntField, ListField, ReferenceField

import spotifystats.models.album as alb
import spotifystats.models.artist as art
from spotifystats.models.named_document import NamedDocument
from spotifystats.util.lists import (
    NamedDocumentList,
    PlayDocumentList,
    RankingDocumentList,
)


class Track(NamedDocument):
    album = ReferenceField("Album")
    artists = ListField(ReferenceField("Artist"))
    popularity = IntField(default=-1)
    plays = ListField(ReferenceField("Play"))
    rankings = ListField(ReferenceField("TrackRanking"))

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
        # Check if track is part of the album
        if self in album.get_tracks():
            self.album = album

    def get_artists(self) -> art.Artist:
        return NamedDocumentList(self.artists)

    def get_popularity(self) -> int:
        return self.popularity

    def get_plays(self) -> List[pl.Play]:
        return PlayDocumentList(self.plays)

    def add_play(self, play: pl.Play) -> None:
        # Check if play corresponds to the track
        if self.get_id() == play.get_track().get_id():
            if play not in self.get_plays():
                self.plays.append(play)

    def get_rankings(self) -> List[t_rnk.TrackRanking]:
        return RankingDocumentList(self.rankings)

    def add_ranking(self, ranking: t_rnk.TrackRanking) -> None:
        if ranking not in self.get_rankings():
            if self in ranking.get_tracks():
                self.rankings.append(ranking)
