from spotifystats.model.artist import Artist

class Track:
    
    def __init__(self, track: dict) -> None:
        """Create track from a spotify response"""
        self._id = track["id"],
        self._name = track["name"],
        self._artists = [Artist(artist) for artist in track["artists"]]

    def get_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_artists(self) -> list[str]:
        return self._artists

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "name": self._name,
            "artists": [artist.to_dict() for artist in self._artists]
        }