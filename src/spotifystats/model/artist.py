class Artist:
    def __init__(self, artist: dict) -> None:
        """Create artist from a spotify response"""
        self.id: str = artist["id"]
        self.name: str = artist["name"]
        self.count: int = 0
        self.last_listened: int = 0

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "count": self.count,
            "last_listened": self.last_listened,
        }

    def __eq__(self, other) -> bool:
        return (
            type(self) == type(other)
            and self.id == other.id
            and self.name == other.name
            and self.count == other.count
            and self.last_listened == other.last_listened
        )
