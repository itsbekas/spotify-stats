class Artist:

    def __init__(self, artist: dict) -> None:
        """Create artist from a spotify response"""
        self._id = artist["id"],
        self._name = artist["name"]

    def __init__(self, id: str, name: str) -> None:
        self._id = id
        self._name = name

    def get_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name
