import pytest

from spotifystats.models import Artist, Track

from test.model.examples import track1


@pytest.fixture
def track_data():
    return track1["track"]


def test_init(track_data):
    track = Track(track_data)
    assert track.id == "2iUmqdfGZcHIhS3b9E9EWq"
    assert track.name == "Everybody Talks"
    assert track.artists == [Artist(track_data["artists"][0])]
    assert track.count == 0
    assert track.last_listened == 0


def test_to_dict(track_data):
    track = Track(track_data)
    track_dict = track.to_dict()
    assert len(track_dict) == 5
    assert track_dict["id"] == "2iUmqdfGZcHIhS3b9E9EWq"
    assert track_dict["name"] == "Everybody Talks"
    assert track_dict["artists"] == [Artist(track_data["artists"][0]).to_dict()]
    assert track_dict["count"] == 0
    assert track_dict["last_listened"] == 0


def test_eq(track_data):
    track1 = Track(track_data)
    track2 = Track(track_data)
    print(track1)
    print(track2)
    assert track1 == track2
