from spotifystats.model.artist import Artist

class Track:
    
    def __init__(self, track: dict) -> None:
        """Create track from a spotify response"""
        self._id = track["id"],
        self._name = track["name"],
        self._artist = [Artist(artist) for artist in track["artists"]]
    
    def __init__(self, id: str, name: str, artists: list(str)) -> None:
        self._id = id
        self._name = name
        self._artists = artists

    def get_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_artists(self) -> list(str):
        return self._artists