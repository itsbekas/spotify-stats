from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import spotifystats.models.album as alb

import spotifystats.database as db
import spotifystats.models.track as trk


def add_track(track: trk.Track) -> None:

    if get_track(track.get_id()) is None:

        for artist in track.get_artists():
            db.add_artist(artist)

        album: alb.Album = track.get_album()
        db.add_album(album)
        album.add_track(track)

        track.save()


def get_track(spotify_id: str) -> trk.Track:
    return trk.Track.objects(spotify_id=spotify_id).first()
