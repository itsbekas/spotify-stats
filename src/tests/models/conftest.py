import json
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
