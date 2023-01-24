class Artist:

    def __init__(self, artist: dict) -> None:
        """Create artist from a spotify response"""
        self._id = artist["id"],
        self._name = artist["name"]

    def __init__(self, id: str, name: str, count: int = 0, last_listened: int = 0) -> None:
        """Create artist from its details"""
        self._id = id
        self._name = name
        self._count = 0
        self._last_listened = 0

    def get_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_count(self) -> int:
        return self._count

    def get_last_listened(self) -> int:
        return self._last_listened
