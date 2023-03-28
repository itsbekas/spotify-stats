import json

import pytest


@pytest.fixture
def artist_STAYC():
    with open("src/tests/data/artists/artist_STAYC.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def track_LOVE_DIVE():
    with open("src/tests/data/tracks/track_LOVE_DIVE.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def track_SO_BAD():
    with open("src/tests/data/tracks/track_SO_BAD.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def track_STEREOTYPE():
    with open("src/tests/data/tracks/track_STEREOTYPE.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def album_LOVE_DIVE():
    with open("src/tests/data/albums/album_LOVE_DIVE.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def album_STEREOTYPE():
    with open("src/tests/data/albums/album_STEREOTYPE.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def album_YOUNG_LUV_COM():
    with open("src/tests/data/albums/album_YOUNG_LUV_COM.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def play_STEREOTYPE():
    with open("src/tests/data/plays/play_stereotype.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def play_Hype_Boy():
    with open("src/tests/data/plays/play_hype_boy.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def ranking_artist_long():
    with open("src/tests/data/rankings/ranking_artist_long.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def ranking_artist_medium():
    with open("src/tests/data/rankings/ranking_artist_medium.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def ranking_artist_short():
    with open("src/tests/data/rankings/ranking_artist_short.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def ranking_track_long():
    with open("src/tests/data/rankings/ranking_track_long.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def ranking_track_medium():
    with open("src/tests/data/rankings/ranking_track_medium.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def ranking_track_short():
    with open("src/tests/data/rankings/ranking_track_short.json", "r") as f:
        play = json.load(f)
    return play
