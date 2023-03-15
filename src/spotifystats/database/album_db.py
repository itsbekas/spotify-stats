from __future__ import annotations

from typing import TYPE_CHECKING, List

import spotifystats.database as db
import spotifystats.models.album as alb

if TYPE_CHECKING:
    import spotifystats.models.artist as art


def add_album(album: alb.Album) -> None:
    if db.get_album(album.get_id()) is None:
        artists = album.get_artists()
        # Add artist if it's not in the database, otherwise use the existing artist
        for i, artist in enumerate(artists):
            db_artist = db.get_artist(artist.get_id())
            if db_artist is None:
                db.add_artist(artist)
            else:
                artists[i] = db_artist
        album.save()


def update_album(album: alb.Album) -> None:
    album.save()


def get_album(spotify_id: str) -> alb.Album:
    return alb.Album.objects(spotify_id=spotify_id).first()
