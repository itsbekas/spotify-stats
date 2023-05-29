import pytest

import spotifystats.database as db
import spotifystats.models.artist as art


def test_add_artist(artist_STAYC):
    artist = art.Artist.from_spotify_response(artist_STAYC)

    db.add_artist(artist)

    assert art.Artist.objects().count() == 1
    assert art.Artist.objects().first() == artist


def test_add_duplicate_artist(artist_STAYC):
    artist = art.Artist.from_spotify_response(artist_STAYC)

    db.add_artist(artist)
    db.add_artist(artist)

    assert art.Artist.objects().count() == 1
    assert art.Artist.objects().first() == artist


def test_get_artist(artist_STAYC):
    artist = art.Artist.from_spotify_response(artist_STAYC)

    db.add_artist(artist)

    assert db.get_artist(spotify_id=artist.get_id()) == artist
    assert db.get_artist(name=artist.get_name()) == artist
    assert db.get_artist(spotify_id=artist.get_id(), name=artist.get_name()) == artist


def test_get_artist_no_args(artist_STAYC):
    artist = art.Artist.from_spotify_response(artist_STAYC)

    db.add_artist(artist)

    with pytest.raises(ValueError):
        db.get_artist()


def test_get_artist_not_in_db(artist_STAYC):
    artist = art.Artist.from_spotify_response(artist_STAYC)

    assert db.get_artist(spotify_id=artist.get_id()) is None
    assert db.get_artist(name=artist.get_name()) is None
    assert db.get_artist(spotify_id=artist.get_id(), name=artist.get_name()) is None
