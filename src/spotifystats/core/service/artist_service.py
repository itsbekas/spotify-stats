import spotifystats.core.database as db
import spotifystats.core.models.artist as art


def add_artist(artist: art.Artist) -> None:
    """
    Checks if artist is already in the database, adding it if it's not.
    """

    if db.get_artist(spotify_id=artist.get_id()) is None:
        db.add_artist(artist)


def get_artist(spotify_id: None | str = None, name: None | str = None) -> art.Artist:
    return db.get_artist(spotify_id=spotify_id, name=name)
