import json
from datetime import datetime

import pytest


@pytest.fixture
def play1():
    with open("src/tests/data/play1.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def play2():
    with open("src/tests/data/play2.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def play1_artist(play1):
    return play1["track"]["artists"][0]


@pytest.fixture
def play2_artist(play2):
    return play2["track"]["artists"][0]


@pytest.fixture
def play1_album(play1):
    return play1["track"]["album"]


@pytest.fixture
def play2_album(play2):
    return play2["track"]["album"]


@pytest.fixture
def play1_track(play1):
    return play1["track"]


@pytest.fixture
def play2_track(play2):
    return play2["track"]


@pytest.fixture
def timestampS():
    return datetime(2023, 3, 19, 16, 0, 0)


@pytest.fixture
def timestampM():
    return datetime(2023, 3, 20, 16, 0, 0)


@pytest.fixture
def timestampL():
    return datetime(2023, 3, 21, 16, 0, 0)


@pytest.fixture
def top_artists_medium():
    with open("src/tests/data/top_artists_medium.json", "r") as f:
        top_artists = json.load(f)
    return top_artists


@pytest.fixture
def top_artists_long():
    with open("src/tests/data/top_artists_long.json", "r") as f:
        top_artists = json.load(f)
    return top_artists


@pytest.fixture
def top_tracks_medium():
    with open("src/tests/data/top_tracks_medium.json", "r") as f:
        top_tracks = json.load(f)
    return top_tracks


@pytest.fixture
def top_tracks_long():
    with open("src/tests/data/top_tracks_long.json", "r") as f:
        top_tracks = json.load(f)
    return top_tracks


@pytest.fixture
def ranking_artists_medium(top_artists_medium, timestampM):
    return {
        "timestamp": timestampM,
        "time_range": "medium_term",
        "artists": top_artists_medium,
    }


@pytest.fixture
def ranking_artists_long(top_artists_long, timestampL):
    return {
        "timestamp": timestampL,
        "time_range": "long_term",
        "artists": top_artists_long,
    }


@pytest.fixture
def ranking_tracks_medium(top_tracks_medium, timestampM):
    return {
        "timestamp": timestampM,
        "time_range": "medium_term",
        "tracks": top_tracks_medium,
    }


@pytest.fixture
def ranking_tracks_long(top_tracks_long, timestampL):
    return {
        "timestamp": timestampL,
        "time_range": "long_term",
        "tracks": top_tracks_long,
    }
