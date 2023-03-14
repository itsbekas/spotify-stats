import pytest
import json
from mongoengine import connect, disconnect
from mongoengine.connection import _get_db

import spotifystats.models.artist as art


@pytest.fixture
def example_artist():
    with open("tests/data/play.json", "r") as f:
        play = json.load(f)
    return play["track"]["artists"][0]


def setup_function():
    """setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    connect("spotify-stats-test")


def teardown_function():
    """teardown any state that was previously setup with a setup_function
    call.
    """
    db = _get_db()
    db.connection.drop_database("spotify-stats-test")
    disconnect()


def test_create_artist(example_artist):
    artist = art.Artist.from_spotify_response(example_artist)
