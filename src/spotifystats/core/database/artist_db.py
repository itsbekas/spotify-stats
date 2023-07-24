from __future__ import annotations

import spotifystats.core.models.artist as art


def add_artist(artist: art.Artist) -> None:
    """
    Checks if artist is already in the database, adding it if it's not.
    """
    artist.save()


def get_artist(spotify_id: None | str = None, name: None | str = None) -> art.Artist:
    query = {}
    if spotify_id:
        query["spotify_id"] = spotify_id
    if name:
        query["name"] = name

    if query == {}:
        raise ValueError("At least one argument must be provided.")

    return art.Artist.objects(**query).first()


def get_top_artists(limit: int = 50) -> list[art.Artist]:
    return art.Artist.objects().order_by("-play_count").limit(limit)
