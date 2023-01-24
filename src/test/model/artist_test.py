import pytest

from spotifystats.model import Artist

# Neon Trees (0RpddSzUHfncUWNJXKOsjy) - Everybody Talks (ID)
track1 = {
    "track": {
        "album": {
            "album_type": "album",
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/0RpddSzUHfncUWNJXKOsjy"
                    },
                    "href": "https://api.spotify.com/v1/artists/0RpddSzUHfncUWNJXKOsjy",
                    "id": "0RpddSzUHfncUWNJXKOsjy",
                    "name": "Neon Trees",
                    "type": "artist",
                    "uri": "spotify:artist:0RpddSzUHfncUWNJXKOsjy",
                }
            ],
            "available_markets": ["AD"],
            "external_urls": {
                "spotify": "https://open.spotify.com/album/0uRFz92JmjwDbZbB7hEBIr"
            },
            "href": "https://api.spotify.com/v1/albums/0uRFz92JmjwDbZbB7hEBIr",
            "id": "0uRFz92JmjwDbZbB7hEBIr",
            "images": [
                {
                    "height": 640,
                    "url": "https://i.scdn.co/image/ab67616d0000b2734a6c0376235e5aa44e59d2c2",
                    "width": 640,
                },
                {
                    "height": 300,
                    "url": "https://i.scdn.co/image/ab67616d00001e024a6c0376235e5aa44e59d2c2",
                    "width": 300,
                },
                {
                    "height": 64,
                    "url": "https://i.scdn.co/image/ab67616d000048514a6c0376235e5aa44e59d2c2",
                    "width": 64,
                },
            ],
            "name": "Picture Show",
            "release_date": "2012-01-01",
            "release_date_precision": "day",
            "total_tracks": 11,
            "type": "album",
            "uri": "spotify:album:0uRFz92JmjwDbZbB7hEBIr",
        },
        "artists": [
            {
                "external_urls": {
                    "spotify": "https://open.spotify.com/artist/0RpddSzUHfncUWNJXKOsjy"
                },
                "href": "https://api.spotify.com/v1/artists/0RpddSzUHfncUWNJXKOsjy",
                "id": "0RpddSzUHfncUWNJXKOsjy",
                "name": "Neon Trees",
                "type": "artist",
                "uri": "spotify:artist:0RpddSzUHfncUWNJXKOsjy",
            }
        ],
        "available_markets": ["AD"],
        "disc_number": 1,
        "duration_ms": 177280,
        "explicit": True,
        "external_ids": {"isrc": "USUM71119189"},
        "external_urls": {
            "spotify": "https://open.spotify.com/track/2iUmqdfGZcHIhS3b9E9EWq"
        },
        "href": "https://api.spotify.com/v1/tracks/2iUmqdfGZcHIhS3b9E9EWq",
        "id": "2iUmqdfGZcHIhS3b9E9EWq",
        "is_local": False,
        "name": "Everybody Talks",
        "popularity": 79,
        "preview_url": "https://p.scdn.co/mp3-preview/2f070fe27132eedc8df3c98babc8984b69ba62cb?cid=e54208d6b446464d956531ac8b414b60",
        "track_number": 3,
        "type": "track",
        "uri": "spotify:track:2iUmqdfGZcHIhS3b9E9EWq",
    },
    "played_at": "2023-01-24T13:52:04.516Z",
    "context": None,
}


@pytest.fixture
def artist_data():
    return track1["track"]["artists"][0]


def test_init(artist_data):
    artist = Artist(artist_data)
    assert artist.id == "0RpddSzUHfncUWNJXKOsjy"
    assert artist.name == "Neon Trees"
    assert artist.count == 0
    assert artist.last_listened == 0


def test_to_dict(artist_data):
    artist = Artist(artist_data)
    artist_dict = artist.to_dict()
    assert artist_dict.length() == 4
    assert artist_dict["id"] == "0RpddSzUHfncUWNJXKOsjy"
    assert artist_dict["name"] == "Neon Trees"
    assert artist_dict["count"] == 0
    assert artist_dict["last_listened"] == 0


dict = {"boas": 1, "bruh": 2, "sim": 4}
