import spotifystats.models.album as alb
import spotifystats.models.artist as art
import spotifystats.models.play as pl
import spotifystats.models.ranking as rnk
import spotifystats.models.track as trk


def test_create_track_from_response(play1_track):
    track = trk.Track.from_spotify_response(play1_track)

    assert isinstance(track, trk.Track)
    assert track.get_id() == play1_track["id"]
    assert track.get_name() == play1_track["name"]
    assert track.get_last_retrieved() is None
    assert track.get_album().get_id() == play1_track["album"]["id"]
    assert len(track.get_artists()) == 1
    assert track.get_artists()[0].get_id() == play1_track["artists"][0]["id"]
    assert track.get_popularity() == play1_track["popularity"]
    assert len(track.get_plays()) == 0
    assert len(track.get_rankings()) == 0


def test_set_album(play1_track, play1_album, play2_album):
    track = trk.Track.from_spotify_response(play1_track)
    album2 = alb.Album.from_spotify_response(play2_album)

    assert track.get_album().get_id() == play1_album["id"]

    track.set_album(album2)

    assert track.get_album().get_id() == play2_album["id"]
