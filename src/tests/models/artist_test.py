import spotifystats.core.models.artist as art
import spotifystats.core.models.artist_ranking as a_rnk
from spotifystats.core.util.conversions import int_to_datetime


def test_create_artist_from_play_response(play_STEREOTYPE):
    artist_response = play_STEREOTYPE["track"]["artists"][0]
    artist = art.Artist.from_spotify_response(artist_response)

    assert isinstance(artist, art.Artist)
    assert artist.get_id() == artist_response["id"]
    assert artist.get_name() == artist_response["name"]
    assert artist.get_last_retrieved() == int_to_datetime(0)
    assert artist.get_popularity() == -1
    assert artist.get_genres() == []
    assert artist.get_rankings() == []


def test_create_artist_from_artist_response(artist_STAYC):
    artist = art.Artist.from_spotify_response(artist_STAYC)

    assert isinstance(artist, art.Artist)
    assert artist.get_id() == artist_STAYC["id"]
    assert artist.get_name() == artist_STAYC["name"]
    assert artist.get_last_retrieved() == int_to_datetime(0)
    assert artist.get_popularity() == artist_STAYC["popularity"]
    assert artist.get_genres() == artist_STAYC["genres"]
    assert artist.get_rankings() == []


def test_add_ranking(artist_STAYC, ranking_artist_short):
    artist = art.Artist.from_spotify_response(artist_STAYC)
    ranking = a_rnk.ArtistRanking.from_spotify_response(ranking_artist_short)

    artist.add_ranking(ranking)

    assert len(artist.get_rankings()) == 1
    assert ranking in artist.get_rankings()


def test_add_invalid_ranking(artist_STAYC, ranking_artist_long):
    artist = art.Artist.from_spotify_response(artist_STAYC)
    ranking = a_rnk.ArtistRanking.from_spotify_response(ranking_artist_long)

    artist.add_ranking(ranking)

    assert len(artist.get_rankings()) == 0
    assert ranking not in artist.get_rankings()


def test_add_two_rankings(artist_STAYC, ranking_artist_short, ranking_artist_medium):
    artist = art.Artist.from_spotify_response(artist_STAYC)
    ranking1 = a_rnk.ArtistRanking.from_spotify_response(ranking_artist_short)
    ranking2 = a_rnk.ArtistRanking.from_spotify_response(ranking_artist_medium)

    artist.add_ranking(ranking1)
    artist.add_ranking(ranking2)

    assert len(artist.get_rankings()) == 2
    assert ranking1 in artist.get_rankings()
    assert ranking2 in artist.get_rankings()


def test_add_duplicate_rankings(artist_STAYC, ranking_artist_short):
    artist = art.Artist.from_spotify_response(artist_STAYC)
    ranking1 = a_rnk.ArtistRanking.from_spotify_response(ranking_artist_short)
    ranking2 = a_rnk.ArtistRanking.from_spotify_response(ranking_artist_short)

    artist.add_ranking(ranking1)
    artist.add_ranking(ranking2)

    assert len(artist.get_rankings()) == 1
    assert ranking1 in artist.get_rankings()
    assert ranking2 in artist.get_rankings()
