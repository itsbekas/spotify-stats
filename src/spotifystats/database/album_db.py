from __future__ import annotations

import spotifystats.database as db
import spotifystats.models.album as alb


def add_album(album: alb.Album) -> None:
    if db.get_album(album.get_id()) is None:
        artists = album.get_artists()
        # Add artist if it's not in the database, otherwise use the existing artist
        for i, artist in enumerate(artists):
            print(artist)
            db_artist = db.get_artist(artist.get_id())
            if db_artist is None:
                print("Adding artist " + artist.get_id() + " to database")
                db.add_artist(artist)
            else:
                print("Artist found: ", artist.get_id())
                artists[i] = db_artist
        print("Saving album: ", album.get_id())
        album.save()

        for artist in album.get_artists():
            print("Adding album " + album.get_id() + " to artist " + artist.get_id())
            artist.add_album(album)
            print("Saving artist: ", artist.get_id())
            artist.save()


def get_album(spotify_id: str) -> alb.Album:
    return alb.Album.objects(spotify_id=spotify_id).first()
