import spotifystats.models.track_ranking as t_rnk
from spotifystats.util import iso_to_datetime


def test_create_track_ranking_from_response(ranking_track_long):
    ranking = t_rnk.TrackRanking.from_spotify_response(ranking_track_long)

    assert isinstance(ranking, t_rnk.TrackRanking)
    assert ranking.get_timestamp() == iso_to_datetime(ranking_track_long["timestamp"])
    assert ranking.get_time_range() == "long_term"
    assert len(ranking.get_tracks()) == 50

    for i, track in enumerate(ranking.get_tracks()):
        assert track.get_id() == ranking_track_long["tracks"][i]["id"]
