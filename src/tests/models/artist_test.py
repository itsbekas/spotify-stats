import json

import pytest
from mongoengine import connect, disconnect
from mongoengine.connection import get_connection

import spotifystats.database as db
import spotifystats.models.album as alb
import spotifystats.models.artist as art


@pytest.fixture
def artist_response():
    with open("src/tests/data/play1.json", "r") as f:
        play = json.load(f)
    return play["track"]["artists"][0]


@pytest.fixture
def album_response():
    with open("src/tests/data/play1.json", "r") as f:
        play = json.load(f)
    return play["track"]["album"]


def setup_function():
    """setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    connect("spotify-stats-test")


def teardown_function():
    """teardown any state that was previously setup with a setup_function
    call.
    """
    conn = get_connection()
    conn.drop_database("spotify-stats-test")
    disconnect()


def test_create_artist(artist_response):
    artist = art.Artist.from_spotify_response(artist_response)
    assert isinstance(artist, art.Artist)
    assert artist.get_id() == artist_response["id"]
    assert artist.get_name() == artist_response["name"]
    assert artist.get_albums() == []
    assert artist.get_tracks() == []


def test_add_album(artist_response, album_response):
    artist = art.Artist.from_spotify_response(artist_response)
    album = alb.Album.from_spotify_response(album_response)
    artist.add_album(album)

    assert len(artist.get_albums()) == 1
    assert artist.get_albums()[0] == alb.Album.from_spotify_response(album_response)
