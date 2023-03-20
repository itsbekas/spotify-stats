import spotifystats.models.album as alb
import spotifystats.models.artist as art
import spotifystats.models.play as pl
import spotifystats.models.artist_ranking as a_rnk
import spotifystats.models.track as trk

import spotifystats.util as util


def test_create_track_from_response(play1):
    play = pl.Play.from_spotify_response(play1)

    assert isinstance(play, pl.Play)
    assert play.get_track().get_id() == play1["track"]["id"]
    assert play.get_timestamp() == util.iso_to_datetime(play1["played_at"])


def test_set_album(play1, play1_track, play2_track):
    play = pl.Play.from_spotify_response(play1)
    track2 = trk.Track.from_spotify_response(play2_track)

    assert play.get_track().get_id() == play1_track["id"]

    play.set_track(track2)

    assert play.get_track().get_id() == play2_track["id"]
