from __future__ import annotations

from typing import TYPE_CHECKING

import spotifystats.models.artist as art


def add_artist(artist: art.Artist) -> None:
    """
    Checks if artist is already in the database, adding it if it's not.
    """
    if get_artist(artist.get_id()) is None:
        artist.save()


def get_artist(spotify_id: str) -> art.Artist:
    return art.Artist.objects(spotify_id=spotify_id).first()
