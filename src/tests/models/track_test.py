from datetime import timedelta

import spotifystats.models.album as alb
import spotifystats.models.play as pl
import spotifystats.models.track as trk
import spotifystats.models.track_ranking as t_rnk


def test_create_track_from_play_response(play_STEREOTYPE):
    track = trk.Track.from_spotify_response(play_STEREOTYPE["track"])

    assert isinstance(track, trk.Track)
    assert track.get_id() == play_STEREOTYPE["track"]["id"]
    assert track.get_name() == play_STEREOTYPE["track"]["name"]
    assert track.get_last_retrieved() is None
    assert track.get_popularity() == play_STEREOTYPE["track"]["popularity"]
    assert track.get_album().get_id() == play_STEREOTYPE["track"]["album"]["id"]
    assert len(track.get_artists()) == 1
    assert (
        track.get_artists()[0].get_id() == play_STEREOTYPE["track"]["artists"][0]["id"]
    )
    assert track.get_plays() == []
    assert track.get_rankings() == []


def test_create_track_from_track_response(track_STEREOTYPE):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)

    assert isinstance(track, trk.Track)
    assert track.get_id() == track_STEREOTYPE["id"]
    assert track.get_name() == track_STEREOTYPE["name"]
    assert track.get_last_retrieved() is None
    assert track.get_popularity() == track_STEREOTYPE["popularity"]
    assert track.get_album().get_id() == track_STEREOTYPE["album"]["id"]
    assert len(track.get_artists()) == 1
    assert track.get_artists()[0].get_id() == track_STEREOTYPE["artists"][0]["id"]
    assert track.get_plays() == []
    assert track.get_rankings() == []


def test_set_album(track_STEREOTYPE, album_STEREOTYPE):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)
    album = alb.Album.from_spotify_response(album_STEREOTYPE)

    track.set_album(album)

    assert track.get_album().get_id() == album.get_id()


def test_set_invalid_album(track_STEREOTYPE, album_STEREOTYPE, album_LOVE_DIVE):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)
    album1 = alb.Album.from_spotify_response(album_STEREOTYPE)

    track.set_album(album1)

    album2 = alb.Album.from_spotify_response(album_LOVE_DIVE)

    track.set_album(album2)

    assert track.get_album().get_id() == album1.get_id()


def test_add_play(track_STEREOTYPE, play_STEREOTYPE):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)
    play = pl.Play.from_spotify_response(play_STEREOTYPE)

    track.add_play(play)

    assert len(track.get_plays()) == 1
    assert play in track.get_plays()


def test_two_plays(track_STEREOTYPE, play_STEREOTYPE):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)
    play1 = pl.Play.from_spotify_response(play_STEREOTYPE)
    play2 = pl.Play.from_spotify_response(play_STEREOTYPE)

    play2.timestamp = play2.timestamp + timedelta(seconds=1)

    track.add_play(play1)
    track.add_play(play2)

    assert len(track.get_plays()) == 2
    assert play1 in track.get_plays()
    assert play2 in track.get_plays()


def test_duplicate_plays(track_STEREOTYPE, play_STEREOTYPE):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)
    play1 = pl.Play.from_spotify_response(play_STEREOTYPE)
    play2 = pl.Play.from_spotify_response(play_STEREOTYPE)

    track.add_play(play1)
    track.add_play(play2)

    assert len(track.get_plays()) == 1
    assert play1 in track.get_plays()
    assert play2 in track.get_plays()


def test_add_ranking(track_STEREOTYPE, ranking_track_short):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)
    ranking = t_rnk.TrackRanking.from_spotify_response(ranking_track_short)

    track.add_ranking(ranking)

    assert len(track.get_rankings()) == 1
    assert ranking in track.get_rankings()


def test_two_rankings(track_STEREOTYPE, ranking_track_short):
    track = trk.Track.from_spotify_response(track_STEREOTYPE)
    ranking1 = t_rnk.TrackRanking.from_spotify_response(ranking_track_short)
    ranking2 = t_rnk.TrackRanking.from_spotify_response(ranking_track_short)

    ranking2.timestamp = ranking2.timestamp + timedelta(seconds=1)

    track.add_ranking(ranking1)
    track.add_ranking(ranking2)

    assert len(track.get_rankings()) == 2
    assert ranking1 in track.get_rankings()
    assert ranking2 in track.get_rankings()
