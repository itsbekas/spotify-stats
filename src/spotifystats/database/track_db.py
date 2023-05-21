from __future__ import annotations

import spotifystats.database as db
import spotifystats.models.track as trk


def add_track(track: trk.Track) -> None:
    if get_track(track.get_id()) is None:
        artists = track.get_artists()
        for i, artist in enumerate(artists):
            db_artist = db.get_artist(artist.get_id())
            if db_artist is None:
                print("Adding artist " + artist.get_id() + " to database")
                db.add_artist(artist)
            else:
                print("Artist found: ", artist.get_id())
                artists[i] = db_artist

        # Add the album to the database if it doesn't exist yet
        album = track.get_album()
        db_album = db.get_album(album.get_id())
        if db_album is None:
            print("Adding album " + album.get_id() + " to database")
            db.add_album(album)
        else:
            print("Album found: ", album.get_id())
            track.set_album(db_album)

        print("Saving track: ", track.get_id())
        track.save()

        for artist in track.get_artists():
            print("Adding track " + track.get_id() + " to artist " + artist.get_id())
            artist.add_track(track)
            print("Saving artist: ", artist.get_id())
            artist.save()

        album = track.get_album()
        print("Adding track " + track.get_id() + " to album " + album.get_id())
        album.add_track(track)
        print("Saving album: ", album.get_id())
        album.save()


def get_track(spotify_id: str) -> trk.Track:
    return trk.Track.objects(spotify_id=spotify_id).first()
