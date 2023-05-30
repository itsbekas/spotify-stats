import pytest

import spotifystats.database as db
import spotifystats.models.album as alb


def test_add_album(album_LOVE_DIVE):
    album = alb.Album.from_spotify_response(album_LOVE_DIVE)

    db.add_album(album)

    assert alb.Album.objects().count() == 1
    assert alb.Album.objects().first() == album


def test_add_duplicate_album(album_LOVE_DIVE):
    album = alb.Album.from_spotify_response(album_LOVE_DIVE)

    db.add_album(album)
    db.add_album(album)

    assert alb.Album.objects().count() == 1
    assert alb.Album.objects().first() == album


def test_get_album(album_LOVE_DIVE):
    album = alb.Album.from_spotify_response(album_LOVE_DIVE)

    db.add_album(album)

    assert db.get_album(spotify_id=album.get_id()) == album
    assert db.get_album(name=album.get_name()) == album
    assert db.get_album(spotify_id=album.get_id(), name=album.get_name()) == album


def test_get_album_no_args():
    with pytest.raises(ValueError):
        db.get_album()


def test_get_album_not_in_db(album_LOVE_DIVE):
    album = alb.Album.from_spotify_response(album_LOVE_DIVE)

    assert db.get_album(spotify_id=album.get_id()) is None
    assert db.get_album(name=album.get_name()) is None
    assert db.get_album(spotify_id=album.get_id(), name=album.get_name()) is None
