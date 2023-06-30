import spotifystats.core.models.album as alb
import spotifystats.core.models.artist as art
import spotifystats.core.models.track as trk
from spotifystats.core.util.conversions import int_to_datetime


def test_create_album_from_play_response(play_STEREOTYPE):
    album_response = play_STEREOTYPE["track"]["album"]
    album = alb.Album.from_spotify_response(album_response)

    assert isinstance(album, alb.Album)
    assert album.get_id() == album_response["id"]
    assert album.get_name() == album_response["name"]
    assert album.get_last_retrieved() == int_to_datetime(0)
    assert album.get_popularity() == -1
    assert album.get_genres() == []
    assert album.get_tracks() == []
    assert len(album.get_artists()) == len(album_response["artists"])
    for i, artist in enumerate(album.get_artists()):
        assert isinstance(artist, art.Artist)
        assert album.get_artists()[0].get_id() == album_response["artists"][i]["id"]


def test_create_album_from_album_response(album_STEREOTYPE):
    album_response = album_STEREOTYPE
    album = alb.Album.from_spotify_response(album_response)

    assert isinstance(album, alb.Album)
    assert album.get_id() == album_response["id"]
    assert album.get_name() == album_response["name"]
    assert album.get_last_retrieved() == int_to_datetime(0)
    assert album.get_popularity() == album_response["popularity"]
    assert album.get_genres() == album_response["genres"]
    assert len(album.get_tracks()) == len(album_response["tracks"])
    for i, track in enumerate(album.get_tracks()):
        assert isinstance(track, trk.Track)
        assert track.get_id() == album_response["tracks"][i]["id"]
    assert len(album.get_artists()) == len(album_response["artists"])
    for i, artist in enumerate(album.get_artists()):
        assert isinstance(artist, art.Artist)
        assert album.get_artists()[0].get_id() == album_response["artists"][i]["id"]


def test_add_track(play_STEREOTYPE, track_COMPLEX):
    album_response = play_STEREOTYPE["track"]["album"]
    album = alb.Album.from_spotify_response(album_response)
    track = trk.Track.from_spotify_response(track_COMPLEX)

    album.add_track(track)

    assert len(album.get_tracks()) == 1
    assert track in album.get_tracks()


def test_add_invalid_track(album_STEREOTYPE, track_LOVE_DIVE):
    album = alb.Album.from_spotify_response(album_STEREOTYPE)
    track = trk.Track.from_spotify_response(track_LOVE_DIVE)

    album.add_track(track)

    assert len(album.get_tracks()) == len(album_STEREOTYPE["tracks"])
    assert track not in album.get_tracks()


def test_add_two_tracks(play_STEREOTYPE, track_COMPLEX, track_SLOW_DOWN):
    album_response = play_STEREOTYPE["track"]["album"]
    album = alb.Album.from_spotify_response(album_response)
    track1 = trk.Track.from_spotify_response(track_COMPLEX)
    track2 = trk.Track.from_spotify_response(track_SLOW_DOWN)

    album.add_track(track1)
    album.add_track(track2)

    assert len(album.get_tracks()) == 2
    assert track1 in album.get_tracks()
    assert track2 in album.get_tracks()


def test_add_duplicate_track(album_STEREOTYPE, track_STEREOTYPE):
    album = alb.Album.from_spotify_response(album_STEREOTYPE)
    track = trk.Track.from_spotify_response(track_STEREOTYPE)

    album.add_track(track)

    assert len(album.get_tracks()) == len(album_STEREOTYPE["tracks"])
    assert track in album.get_tracks()
