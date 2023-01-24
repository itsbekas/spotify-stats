class Artist:

    def __init__(self, artist: dict) -> None:
        """Create artist from a spotify response"""
        self.id = artist["id"],
        self.name = artist["name"]
        self.count = 0
        self.last_listened = 0
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "count": self.count,
            "last_listened": self.last_listened
        }
