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
    assert track.get_popularity() == 0
    assert len(track.get_albums()) == 1
    assert track.get_albums()[0].get_id() == play_STEREOTYPE["track"]["album"]["id"]
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
    assert len(track.get_albums()) == 1
    assert track.get_albums()[0].get_id() == track_STEREOTYPE["album"]["id"]
    assert len(track.get_artists()) == 1
    assert track.get_artists()[0].get_id() == track_STEREOTYPE["artists"][0]["id"]
    assert track.get_plays() == []
    assert track.get_rankings() == []


def test_set_album(play1_track, play1_album, play2_album):
    track = trk.Track.from_spotify_response(play1_track)
    album2 = alb.Album.from_spotify_response(play2_album)

    assert track.get_album().get_id() == play1_album["id"]

    track.set_album(album2)

    assert track.get_album().get_id() == play2_album["id"]


def test_add_play(play1, play1_track):
    track = trk.Track.from_spotify_response(play1_track)
    play = pl.Play.from_spotify_response(play1)

    track.add_play(play)

    assert len(track.get_plays()) == 1


def test_two_plays(play1, play2, play1_track):
    track = trk.Track.from_spotify_response(play1_track)
    play1 = pl.Play.from_spotify_response(play1)
    play2 = pl.Play.from_spotify_response(play2)

    track.add_play(play1)
    track.add_play(play2)

    assert len(track.get_plays()) == 2


def test_add_ranking(ranking_tracks_long, top_tracks_long):
    track = trk.Track.from_spotify_response(top_tracks_long[0])
    ranking = t_rnk.TrackRanking.from_spotify_response(ranking_tracks_long)

    track.add_ranking(ranking)

    assert len(track.get_rankings()) == 1


def test_two_rankings(ranking_tracks_medium, ranking_tracks_long, top_tracks_long):
    track = trk.Track.from_spotify_response(top_tracks_long[0])
    rankingL = t_rnk.TrackRanking.from_spotify_response(ranking_tracks_long)
    rankingM = t_rnk.TrackRanking.from_spotify_response(ranking_tracks_medium)

    track.add_ranking(rankingL)
    track.add_ranking(rankingM)

    assert len(track.get_rankings()) == 2
