import pytest

import spotifystats.core.database as db
import spotifystats.core.models.track as trk


def test_add_track(track_STEREOTYPE):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)

    db.add_track(track)

    assert trk.Track.objects().count() == 1
    assert trk.Track.objects().first() == track


def test_add_duplicate_track(track_STEREOTYPE):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)

    db.add_track(track)
    db.add_track(track)

    assert trk.Track.objects().count() == 1
    assert trk.Track.objects().first() == track


def test_get_track(track_STEREOTYPE):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)

    db.add_track(track)

    assert db.get_track(spotify_id=track.get_id()) == track
    assert db.get_track(name=track.get_name()) == track
    assert db.get_track(spotify_id=track.get_id(), name=track.get_name()) == track


def test_get_track_no_args():
    with pytest.raises(ValueError):
        db.get_track()


def test_get_track_not_in_db(track_STEREOTYPE):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)

    assert db.get_track(spotify_id=track.get_id()) is None
    assert db.get_track(name=track.get_name()) is None
    assert db.get_track(spotify_id=track.get_id(), name=track.get_name()) is None
