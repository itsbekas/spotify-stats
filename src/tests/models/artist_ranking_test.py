import spotifystats.models.artist as art
import spotifystats.models.artist_ranking as a_rnk


def test_create_artist_ranking_from_response(
    ranking_artists_long, top_artists_long, timestampL
):
    ranking = a_rnk.ArtistRanking.from_spotify_response(ranking_artists_long)

    artists = []
    for artist in top_artists_long:
        artists.append(art.Artist.from_spotify_response(artist))

    assert isinstance(ranking, a_rnk.ArtistRanking)
    assert ranking.get_timestamp() == timestampL
    assert ranking.get_time_range() == "long_term"
    assert len(ranking.get_artists()) == 50

    artists = ranking.get_artists()

    for i in range(50):
        assert artists[i].get_id() == top_artists_long[i]["id"]
