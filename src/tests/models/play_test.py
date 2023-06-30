import spotifystats.core.models.play as pl
import spotifystats.core.models.track as trk
import spotifystats.core.util as util


def test_create_play_from_response(play_STEREOTYPE):
    play = pl.Play.from_spotify_response(play_STEREOTYPE)

    assert isinstance(play, pl.Play)
    assert play.get_track().get_id() == play_STEREOTYPE["track"]["id"]
    assert play.get_timestamp() == util.iso_to_datetime(play_STEREOTYPE["played_at"])


def test_set_track(play_STEREOTYPE, track_LOVE_DIVE):
    play = pl.Play.from_spotify_response(play_STEREOTYPE)
    track2 = trk.Track.from_spotify_response(track_LOVE_DIVE)

    play.set_track(track2)

    assert play.get_track().get_id() == track_LOVE_DIVE["id"]
