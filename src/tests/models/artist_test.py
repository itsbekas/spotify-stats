import spotifystats.models.album as alb
import spotifystats.models.artist as art
import spotifystats.models.artist_ranking as a_rnk
import spotifystats.models.track as trk


def test_create_artist_from_play_response(play_STEREOTYPE):
    artist = art.Artist.from_spotify_response(play_STEREOTYPE["track"]["artists"][0])

    assert isinstance(artist, art.Artist)
    assert artist.get_id() == play_STEREOTYPE["track"]["artists"][0]["id"]
    assert artist.get_name() == play_STEREOTYPE["track"]["artists"][0]["name"]
    assert artist.get_last_retrieved() is None
    assert artist.get_popularity() == 0
    assert artist.get_genres() == []
    assert artist.get_albums() == []
    assert artist.get_tracks() == []
    assert artist.get_rankings() == []


def test_create_artist_from_artist_response(artist_STAYC):
    artist = art.Artist.from_spotify_response(artist_STAYC)

    assert isinstance(artist, art.Artist)
    assert artist.get_id() == artist_STAYC["id"]
    assert artist.get_name() == artist_STAYC["name"]
    assert artist.get_last_retrieved() is None
    assert artist.get_popularity() == artist_STAYC["popularity"]
    assert artist.get_genres() == artist_STAYC["genres"]
    assert artist.get_albums() == []
    assert artist.get_tracks() == []
    assert artist.get_rankings() == []


def test_add_album(play1_artist, play1_album):
    artist = art.Artist.from_spotify_response(play1_artist)
    album = alb.Album.from_spotify_response(play1_album)
    artist.add_album(album)

    assert len(artist.get_albums()) == 1
    assert artist.get_albums()[0].get_id() == play1_album["id"]


def test_add_two_albums(play1_artist, play1_album, play2_album):
    artist = art.Artist.from_spotify_response(play1_artist)
    album1 = alb.Album.from_spotify_response(play1_album)
    album2 = alb.Album.from_spotify_response(play2_album)

    artist.add_album(album1)
    artist.add_album(album2)

    assert len(artist.get_albums()) == 2
    assert album1 in artist.get_albums()
    assert album2 in artist.get_albums()


def test_add_duplicate_album(play1_artist, play1_album):
    artist = art.Artist.from_spotify_response(play1_artist)
    album1 = alb.Album.from_spotify_response(play1_album)
    album2 = alb.Album.from_spotify_response(play1_album)

    artist.add_album(album1)
    artist.add_album(album2)

    assert len(artist.get_albums()) == 1
    assert artist.get_albums()[0].get_id() == play1_album["id"]


def test_add_track(play1_artist, play1_track):
    artist = art.Artist.from_spotify_response(play1_artist)
    track = trk.Track.from_spotify_response(play1_track)

    artist.add_track(track)

    assert len(artist.get_tracks()) == 1
    assert artist.get_tracks()[0].get_id() == play1_track["id"]


def test_add_two_tracks(play1_artist, play1_track, play2_track):
    artist = art.Artist.from_spotify_response(play1_artist)
    track1 = trk.Track.from_spotify_response(play1_track)
    track2 = trk.Track.from_spotify_response(play2_track)

    artist.add_track(track1)
    artist.add_track(track2)

    assert len(artist.get_tracks()) == 2
    assert track1 in artist.get_tracks()
    assert track2 in artist.get_tracks()


def test_add_duplicate_track(play1_artist, play1_track):
    artist = art.Artist.from_spotify_response(play1_artist)
    track1 = trk.Track.from_spotify_response(play1_track)
    track2 = trk.Track.from_spotify_response(play1_track)

    artist.add_track(track1)
    artist.add_track(track2)

    assert len(artist.get_tracks()) == 1
    assert artist.get_tracks()[0].get_id() == play1_track["id"]


def test_add_ranking(ranking_artists_long) -> None:
    artist = art.Artist.from_spotify_response(ranking_artists_long["artists"][0])
    ranking = a_rnk.ArtistRanking.from_spotify_response(ranking_artists_long)

    artist.add_ranking(ranking)

    assert len(artist.get_rankings()) == 1
    assert artist in artist.get_rankings()[0].get_artists()


def test_two_rankings(ranking_artists_medium, ranking_artists_long):
    artist = art.Artist.from_spotify_response(ranking_artists_long["artists"][0])
    rankingL = a_rnk.ArtistRanking.from_spotify_response(ranking_artists_long)

    artist.add_ranking(rankingL)

    rankingM = a_rnk.ArtistRanking.from_spotify_response(ranking_artists_medium)

    artist.add_ranking(rankingM)

    assert len(artist.get_rankings()) == 2
