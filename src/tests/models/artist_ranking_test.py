import spotifystats.core.models.artist_ranking as a_rnk


def test_create_artist_ranking_from_response(ranking_artist_long):
    ranking = a_rnk.ArtistRanking.from_spotify_response(ranking_artist_long)

    assert isinstance(ranking, a_rnk.ArtistRanking)
    assert ranking.get_timestamp() == ranking_artist_long["timestamp"]
    assert ranking.get_time_range() == "long_term"
    assert len(ranking.get_artists()) == 50

    for i, artist in enumerate(ranking.get_artists()):
        assert artist.get_id() == ranking_artist_long["artists"][i]["id"]
