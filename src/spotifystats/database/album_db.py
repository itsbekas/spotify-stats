from __future__ import annotations

from typing import TYPE_CHECKING

import spotifystats.database as db
import spotifystats.models.album as alb


def add_album(album: alb.Album) -> None:

    if get_album(album.get_id()) is None:

        for artist in album.get_artists():
            db.add_artist(artist)

        album.save()


def get_album(spotify_id: str) -> alb.Album:
    return alb.Album.objects(spotify_id=spotify_id).first()
