import pytest

from spotifystats.models import Artist

from test.model.examples import track1


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
    assert len(artist_dict) == 4
    assert artist_dict["id"] == "0RpddSzUHfncUWNJXKOsjy"
    assert artist_dict["name"] == "Neon Trees"
    assert artist_dict["count"] == 0
    assert artist_dict["last_listened"] == 0


def test_eq(artist_data):
    artist1 = Artist(artist_data)
    artist2 = Artist(artist_data)
    assert artist1 == artist2
