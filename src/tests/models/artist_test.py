import spotifystats.models.album as alb
import spotifystats.models.artist as art
import spotifystats.models.artist_ranking as a_rnk
import spotifystats.models.track as trk
from spotifystats.util.conversions import int_to_datetime


def test_create_artist_from_play_response(play_STEREOTYPE):
    artist_response = play_STEREOTYPE["track"]["artists"][0]
    artist = art.Artist.from_spotify_response(artist_response)

    assert isinstance(artist, art.Artist)
    assert artist.get_id() == artist_response["id"]
    assert artist.get_name() == artist_response["name"]
    assert artist.get_last_retrieved() == int_to_datetime(0)
    assert artist.get_popularity() == -1
    assert artist.get_genres() == []
    assert artist.get_albums() == []
    assert artist.get_tracks() == []
    assert artist.get_rankings() == []


def test_create_artist_from_artist_response(artist_STAYC):
    artist = art.Artist.from_spotify_response(artist_STAYC)

    assert isinstance(artist, art.Artist)
    assert artist.get_id() == artist_STAYC["id"]
    assert artist.get_name() == artist_STAYC["name"]
    assert artist.get_last_retrieved() == int_to_datetime(0)
    assert artist.get_popularity() == artist_STAYC["popularity"]
    assert artist.get_genres() == artist_STAYC["genres"]
    assert artist.get_albums() == []
    assert artist.get_tracks() == []
    assert artist.get_rankings() == []


def test_add_album(artist_STAYC, album_STEREOTYPE):
    artist = art.Artist.from_spotify_response(artist_STAYC)
    album = alb.Album.from_spotify_response(album_STEREOTYPE)

    artist.add_album(album)

    assert len(artist.get_albums()) == 1
    assert album in artist.get_albums()


def test_add_invalid_album(artist_STAYC, album_LOVE_DIVE):
    artist = art.Artist.from_spotify_response(artist_STAYC)
    album = alb.Album.from_spotify_response(album_LOVE_DIVE)

    artist.add_album(album)

    assert len(artist.get_albums()) == 0
    assert album not in artist.get_albums()


def test_add_two_albums(artist_STAYC, album_STEREOTYPE, album_YOUNG_LUV_COM):
    artist = art.Artist.from_spotify_response(artist_STAYC)
    album1 = alb.Album.from_spotify_response(album_STEREOTYPE)
    album2 = alb.Album.from_spotify_response(album_YOUNG_LUV_COM)

    artist.add_album(album1)
    artist.add_album(album2)

    assert len(artist.get_albums()) == 2
    assert album1 in artist.get_albums()
    assert album2 in artist.get_albums()


def test_add_duplicate_album(artist_STAYC, album_STEREOTYPE):
    artist = art.Artist.from_spotify_response(artist_STAYC)
    album1 = alb.Album.from_spotify_response(album_STEREOTYPE)
    album2 = alb.Album.from_spotify_response(album_STEREOTYPE)

    artist.add_album(album1)
    artist.add_album(album2)

    assert len(artist.get_albums()) == 1
    assert album1 in artist.get_albums()
    assert album2 in artist.get_albums()


def test_add_track(artist_STAYC, track_STEREOTYPE):
    artist = art.Artist.from_spotify_response(artist_STAYC)
    track = trk.Track.from_spotify_response(track_STEREOTYPE)

    artist.add_track(track)

    assert len(artist.get_tracks()) == 1
    assert track in artist.get_tracks()


def test_add_invalid_track(artist_STAYC, track_LOVE_DIVE):
    artist = art.Artist.from_spotify_response(artist_STAYC)
    track = trk.Track.from_spotify_response(track_LOVE_DIVE)

    artist.add_track(track)

    assert len(artist.get_tracks()) == 0
    assert track not in artist.get_tracks()


def test_add_two_tracks(artist_STAYC, track_STEREOTYPE, track_SO_BAD):
    artist = art.Artist.from_spotify_response(artist_STAYC)
    track1 = trk.Track.from_spotify_response(track_STEREOTYPE)
    track2 = trk.Track.from_spotify_response(track_SO_BAD)

    artist.add_track(track1)
    artist.add_track(track2)

    assert len(artist.get_tracks()) == 2
    assert track1 in artist.get_tracks()
    assert track2 in artist.get_tracks()


def test_add_duplicate_track(artist_STAYC, track_STEREOTYPE):
    artist = art.Artist.from_spotify_response(artist_STAYC)
    track1 = trk.Track.from_spotify_response(track_STEREOTYPE)
    track2 = trk.Track.from_spotify_response(track_STEREOTYPE)

    artist.add_track(track1)
    artist.add_track(track2)

    assert len(artist.get_tracks()) == 1
    assert track1 in artist.get_tracks()
    assert track2 in artist.get_tracks()


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
