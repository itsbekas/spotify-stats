import spotifystats.models.album as alb
import spotifystats.models.track as trk


def test_create_album_from_response(play1_album):
    album = alb.Album.from_spotify_response(play1_album)

    assert isinstance(album, alb.Album)
    assert album.get_id() == play1_album["id"]
    assert album.get_name() == play1_album["name"]
    assert album.get_last_retrieved() is None
    assert len(album.get_artists()) == 1
    assert album.get_artists()[0].get_id() == play1_album["artists"][0]["id"]
    assert len(album.get_tracks()) == 0


def test_add_track(play1_album, play1_track):
    album = alb.Album.from_spotify_response(play1_album)
    track = trk.Track.from_spotify_response(play1_track)

    album.add_track(track)

    assert len(album.get_tracks()) == 1
    assert track in album.get_tracks()


def test_add_two_tracks(play1_album, play1_track, play2_track):
    album = alb.Album.from_spotify_response(play1_album)
    track1 = trk.Track.from_spotify_response(play1_track)
    track2 = trk.Track.from_spotify_response(play2_track)

    album.add_track(track1)
    album.add_track(track2)

    assert len(album.get_tracks()) == 2
    assert track1 in album.get_tracks()
    assert track2 in album.get_tracks()


def test_add_duplicate_track(play1_album, play1_track):
    album = alb.Album.from_spotify_response(play1_album)
    track1 = trk.Track.from_spotify_response(play1_track)
    track2 = trk.Track.from_spotify_response(play1_track)

    album.add_track(track1)
    album.add_track(track2)

    assert len(album.get_tracks()) == 1
    assert track1 in album.get_tracks()
