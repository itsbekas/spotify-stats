import spotifystats.models.track_ranking as t_rnk


def test_create_track_ranking_from_response(ranking_track_long):
    ranking = t_rnk.TrackRanking.from_spotify_response(ranking_track_long)

    assert isinstance(ranking, t_rnk.TrackRanking)
    # I'm guessing datetimes are stored as strings in the database
    # and can't be converted if the object is not saved
    assert ranking.get_timestamp() == ranking_track_long["timestamp"]
    assert ranking.get_time_range() == "long_term"
    assert len(ranking.get_tracks()) == 50

    for i, track in enumerate(ranking.get_tracks()):
        assert track.get_id() == ranking_track_long["tracks"][i]["id"]
