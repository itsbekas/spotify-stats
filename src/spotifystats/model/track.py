from spotifystats.model.artist import Artist


class Track:
    def __init__(self, track: dict) -> None:
        """Create track from a spotify response"""
        self.id: str = track["id"]
        self.name: str = track["name"]
        self.artists: list[Artist] = [Artist(artist) for artist in track["artists"]]
        self.count: int = 0
        self.last_listened: int = 0

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "artists": [artist.to_dict() for artist in self.artists],
            "count": self.count,
            "last_listened": self.last_listened,
        }

    def __eq__(self, other) -> bool:
        return (
            type(self) == type(other)
            and self.id == other.id
            and self.name == other.name
            and self.artists == other.artists
            and self.count == other.count
            and self.last_listened == other.last_listened
        )
