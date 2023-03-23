from __future__ import annotations

from typing import TYPE_CHECKING, List

from mongoengine.fields import ListField, ReferenceField

from spotifystats.models.named_document import NamedDocument

if TYPE_CHECKING:
    import spotifystats.models.album as alb
    import spotifystats.models.artist_ranking as a_rnk
    import spotifystats.models.track as trk


class Artist(NamedDocument):
    albums = ListField(ReferenceField("Album"))
    tracks = ListField(ReferenceField("Track"))
    rankings = ListField(ReferenceField("ArtistRanking"))

    @classmethod
    def from_spotify_response(cls, response) -> Artist:
        return cls(spotify_id=response["id"], name=response["name"])

    def get_albums(self) -> List[alb.Album]:
        return self.albums

    def add_album(self, album: alb.Album) -> None:
        # Check if artist already has this album
        if album not in self.get_albums():
            # Check if artist is part of the album
            if self not in album.get_artists():
                self.albums.append(album)

    def get_tracks(self) -> List[trk.Track]:
        return self.tracks

    def add_track(self, track: trk.Track) -> None:
        # Check if artist already has this track
        if track not in self.get_tracks():
            # Check if artist is part of the track
            if self not in track.get_artists():
                self.tracks.append(track)

    def get_rankings(self) -> List[a_rnk.ArtistRanking]:
        return self.rankings

    def add_ranking(self, ranking: a_rnk.ArtistRanking) -> None:
        # Check if artist is part of the ranking
        if self not in ranking.get_artists():
            self.rankings.append(ranking)
