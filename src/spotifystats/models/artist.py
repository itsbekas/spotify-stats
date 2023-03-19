from __future__ import annotations

from typing import TYPE_CHECKING, List

from mongoengine.fields import ListField, ReferenceField

from spotifystats.models.named_document import NamedDocument

if TYPE_CHECKING:
    import spotifystats.models.album as alb
    import spotifystats.models.track as trk


class Artist(NamedDocument):
    albums = ListField(ReferenceField("Album"))
    tracks = ListField(ReferenceField("Track"))

    @classmethod
    def from_spotify_response(cls, response) -> Artist:
        return cls(spotify_id=response["id"], name=response["name"])

    def get_albums(self) -> List[alb.Album]:
        return self.albums

    def add_album(self, album: alb.Album) -> None:
        ids = [a.get_id() for a in self.get_albums()]
        if album.get_id() not in ids:
            self.albums.append(album)

    def get_tracks(self) -> List[trk.Track]:
        return self.tracks

    def add_track(self, track: trk.Track) -> None:
        ids = [t.get_id() for t in self.get_tracks()]
        if track.get_id() not in ids:
            self.tracks.append(track)
