from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import spotifystats.models.album as alb

import spotifystats.database as db
import spotifystats.models.track as trk


def add_track(track: trk.Track) -> None:

    if get_track(track.get_id()) is None:
        artists = track.get_artists()
        # Add artist if it's not in the database, otherwise use the existing artist
        for i, artist in enumerate(artists):
            db_artist = db.get_artist(artist.get_id())
            if db_artist is None:
                db.add_artist(artist)
            else:
                artists[i] = db_artist

        # Add the album to the database if it doesn't exist yet
        album = track.get_album()
        db_album = db.get_album(album.get_id())
        if db_album is None:
            db.add_album(album)
        else:
            track.set_album(db_album)

        track.save()

        # After the track has been saved, add it to the album and update it
        album.add_track(track)
        db.update_album(track.get_album())


def get_track(spotify_id: str) -> trk.Track:
    return trk.Track.objects(spotify_id=spotify_id).first()
