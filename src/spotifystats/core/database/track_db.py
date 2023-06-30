from __future__ import annotations

import spotifystats.database as db
import spotifystats.models.track as trk


def add_track(track: trk.Track) -> None:
    if get_track(track.get_id()) is None:
        artists = track.get_artists()
        for i, artist in enumerate(artists):
            db_artist = db.get_artist(artist.get_id())
            if db_artist is None:
                db.add_artist(artist)
            else:
                track.set_artist(i, db_artist)

        # Add the album to the database if it doesn't exist yet
        album = track.get_album()
        if album is not None:
            db_album = db.get_album(album.get_id())
            if db_album is None:
                db.add_album(album)
            else:
                track.set_album(db_album)

        track.save()

        for artist in track.get_artists():
            artist.add_track(track)
            artist.save()

        album = track.get_album()
        if album is not None:
            album.add_track(track)
            album.save()


def get_track(
    spotify_id: None | str = None, name: None | str = None
) -> None | trk.Track:
    query = {}
    if spotify_id:
        query["spotify_id"] = spotify_id
    if name:
        query["name"] = name

    if query == {}:
        raise ValueError("At least one argument must be provided.")

    return trk.Track.objects(**query).first()
