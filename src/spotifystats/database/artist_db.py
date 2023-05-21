from __future__ import annotations

import spotifystats.models.artist as art


def add_artist(artist: art.Artist) -> None:
    """
    Checks if artist is already in the database, adding it if it's not.
    """

    if get_artist(spotify_id=artist.get_id()) is None:
        print("Saving artist: ", artist.get_id())
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
