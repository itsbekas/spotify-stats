from spotifystats.model.artist import Artist


class Track:
    def __init__(self, track: dict) -> None:
        """Create track from a spotify response"""
        self.id = (track["id"],)
        self.name = (track["name"],)
        self.artists = [Artist(artist) for artist in track["artists"]]

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "artists": [artist.to_dict() for artist in self.artists],
        }
