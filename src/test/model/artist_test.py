import pytest

from spotifystats.model import Artist

from examples import track1

@pytest.fixture
def artist_data():
    return track1["track"]["artists"][0]

def test_init(artist_data):
    artist = Artist(artist_data)
    assert artist.id == "0RpddSzUHfncUWNJXKOsjy"
    assert artist.name == "Neon Trees"
    assert artist.count == 0
    assert artist.last_listened == 0

def test_to_dict(artist_data):
    artist = Artist(artist_data)
    artist_dict = artist.to_dict()
    assert artist_dict.length() == 4
    assert artist_dict["id"] == "0RpddSzUHfncUWNJXKOsjy"
    assert artist_dict["name"] == "Neon Trees"
    assert artist_dict["count"] == 0
    assert artist_dict["last_listened"] == 0
