import spotifystats.core.models.album as alb
import spotifystats.core.models.artist as art
import spotifystats.core.models.track as trk
import spotifystats.core.models.track_ranking as t_rnk
from spotifystats.core.util.conversions import int_to_datetime


def test_create_track_from_play_response(play_STEREOTYPE):
    track_response = play_STEREOTYPE["track"]
    track = trk.Track.from_spotify_response(track_response)

    assert isinstance(track, trk.Track)
    assert track.get_id() == track_response["id"]
    assert track.get_name() == track_response["name"]
    assert track.get_last_retrieved() == int_to_datetime(0)
    assert track.get_popularity() == track_response["popularity"]
    assert track.get_album().get_id() == track_response["album"]["id"]
    assert len(track.get_artists()) == len(track_response["artists"])
    for i, artist in enumerate(track.get_artists()):
        assert isinstance(artist, art.Artist)
        assert track.get_artists()[0].get_id() == track_response["artists"][i]["id"]

    assert track.get_play_count() == 0
    assert track.get_rankings() == []


def test_create_track_from_track_response(track_STEREOTYPE):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)

    assert isinstance(track, trk.Track)
    assert track.get_id() == track_STEREOTYPE["id"]
    assert track.get_name() == track_STEREOTYPE["name"]
    assert track.get_last_retrieved() == int_to_datetime(0)
    assert track.get_popularity() == track_STEREOTYPE["popularity"]
    assert track.get_album().get_id() == track_STEREOTYPE["album"]["id"]
    assert len(track.get_artists()) == len(track_STEREOTYPE["artists"])
    for i, artist in enumerate(track.get_artists()):
        assert isinstance(artist, art.Artist)
        assert track.get_artists()[0].get_id() == track_STEREOTYPE["artists"][i]["id"]
    assert track.get_play_count() == 0
    assert track.get_rankings() == []


def test_set_album(track_STEREOTYPE, album_STEREOTYPE):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)
    album = alb.Album.from_spotify_response(album_STEREOTYPE)

    track.set_album(album)

    assert track.get_album().get_id() == album.get_id()


# The track's album is already checked when adding it to an album
# def test_set_invalid_album(track_STEREOTYPE, album_STEREOTYPE, album_LOVE_DIVE):
#     track = trk.Track.from_spotify_response(track_STEREOTYPE)
#     album1 = alb.Album.from_spotify_response(album_STEREOTYPE)

#     track.set_album(album1)

#     album2 = alb.Album.from_spotify_response(album_LOVE_DIVE)

#     track.set_album(album2)

#     assert track.get_album().get_id() == album1.get_id()


def test_increment_play_count(track_STEREOTYPE):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)

    track.increment_play_count()

    assert track.get_play_count() == 1


def test_add_ranking(track_STEREOTYPE, ranking_track_short):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)
    ranking = t_rnk.TrackRanking.from_spotify_response(ranking_track_short)

    track.add_ranking(ranking)

    assert len(track.get_rankings()) == 1
    assert ranking in track.get_rankings()


def test_add_invalid_ranking(track_STEREOTYPE, ranking_track_long):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)
    ranking = t_rnk.TrackRanking.from_spotify_response(ranking_track_long)

    track.add_ranking(ranking)

    assert len(track.get_rankings()) == 0
    assert ranking not in track.get_rankings()


def test_two_rankings(track_STEREOTYPE, ranking_track_short, ranking_track_medium):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)
    ranking1 = t_rnk.TrackRanking.from_spotify_response(ranking_track_short)
    ranking2 = t_rnk.TrackRanking.from_spotify_response(ranking_track_medium)

    ranking2.timestamp = ranking2.timestamp

    track.add_ranking(ranking1)
    track.add_ranking(ranking2)

    assert len(track.get_rankings()) == 2
    assert ranking1 in track.get_rankings()
    assert ranking2 in track.get_rankings()


def test_duplicate_rankings(track_STEREOTYPE, ranking_track_short):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)
    ranking1 = t_rnk.TrackRanking.from_spotify_response(ranking_track_short)
    ranking2 = t_rnk.TrackRanking.from_spotify_response(ranking_track_short)

    track.add_ranking(ranking1)
    track.add_ranking(ranking2)

    assert len(track.get_rankings()) == 1
    assert ranking1 in track.get_rankings()
    assert ranking2 in track.get_rankings()
