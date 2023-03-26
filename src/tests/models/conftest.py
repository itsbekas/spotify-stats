import json

import pytest


@pytest.fixture
def artist_STAYC():
    with open("src/tests/data/artists/artist_STAYC.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def track_STEREOTYPE():
    with open("src/tests/data/tracks/track_STEREOTYPE.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def play_STEREOTYPE():
    with open("src/tests/data/plays/play_STEREOTYPE.json", "r") as f:
        play = json.load(f)
    return play


@pytest.fixture
def play_Hype_Boy():
    with open("src/tests/data/plays/play_Hype_Boy.json", "r") as f:
        play = json.load(f)
    return play
