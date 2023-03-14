import json

import pytest
from mongoengine import connect, disconnect
from mongoengine.connection import get_connection

import spotifystats.database as db
import spotifystats.models.album as alb
import spotifystats.models.artist as art


@pytest.fixture
def example_artist():
    with open("src/tests/data/play.json", "r") as f:
        play = json.load(f)
    return play["track"]["artists"][0]


@pytest.fixture
def example_album():
    with open("src/tests/data/play.json", "r") as f:
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


def test_create_artist(example_artist):
    artist = art.Artist.from_spotify_response(example_artist)
    artist.save()
    assert artist.get_id() == example_artist["id"]
    assert artist.get_name() == example_artist["name"]
    assert artist.get_albums() == []
    assert artist.get_tracks() == []


def test_add_album(example_artist, example_album):
    artist = art.Artist.from_spotify_response(example_artist)
    album = alb.Album.from_spotify_response(example_album)
    artist.add_album(album)

    assert artist.get_albums() == [album]
