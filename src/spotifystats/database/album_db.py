from __future__ import annotations

import spotifystats.database as db
import spotifystats.models.album as alb


def add_album(album: alb.Album) -> None:
    if db.get_album(album.get_id()) is None:
        artists = album.get_artists()
        # Add artist if it's not in the database, otherwise use the existing artist
        for i, artist in enumerate(artists):
            db_artist = db.get_artist(artist.get_id())
            if db_artist is None:
                db.add_artist(artist)
            else:
                album.set_artist(i, db_artist)

        album.save()

        for artist in album.get_artists():
            artist.add_album(album)
            artist.save()


def get_album(spotify_id: None | str = None, name: None | str = None) -> alb.Album:
    query = {}
    if spotify_id:
        query["spotify_id"] = spotify_id
    if name:
        query["name"] = name

    if query == {}:
        raise ValueError("At least one argument must be provided.")

    return alb.Album.objects(**query).first()
