from __future__ import annotations

from typing import TYPE_CHECKING, List

from mongoengine.fields import IntField, ListField, ReferenceField, StringField

from spotifystats.models.named_document import NamedDocument
from spotifystats.util.lists import DatedDocumentList, NamedDocumentList

if TYPE_CHECKING:
    import spotifystats.models.album as alb
    import spotifystats.models.artist_ranking as a_rnk
    import spotifystats.models.track as trk


class Artist(NamedDocument):
    popularity = IntField(required=True)
    genres = ListField(StringField())
    albums = ListField(ReferenceField("Album"))
    tracks = ListField(ReferenceField("Track"))
    rankings = ListField(ReferenceField("ArtistRanking"))

    @classmethod
    def from_spotify_response(cls, response) -> Artist:
        popularity = response["popularity"] if "popularity" in response else None
        genres = response["genres"] if "genres" in response else None
        return cls(
            spotify_id=response["id"],
            name=response["name"],
            popularity=popularity,
            genres=genres,
        )

    def get_albums(self) -> List[alb.Album]:
        return NamedDocumentList(self.albums)

    def add_album(self, album: alb.Album) -> None:
        # Check if artist already has this album
        if album not in self.get_albums():
            # Check if artist is part of the album
            if self in album.get_artists():
                self.albums.append(album)

    def get_tracks(self) -> List[trk.Track]:
        return NamedDocumentList(self.tracks)

    def add_track(self, track: trk.Track) -> None:
        # Check if artist already has this track
        if track not in self.get_tracks():
            # Check if artist is part of the track
            if self in track.get_artists():
                self.tracks.append(track)

    def get_rankings(self) -> List[a_rnk.ArtistRanking]:
        return DatedDocumentList(self.rankings)

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
