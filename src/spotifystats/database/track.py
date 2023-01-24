from spotifystats.database.base import Database, Collection


class TrackDatabase(Database):
    def __init__(self, dbname: str) -> None:
        super().__init__(dbname, Collection.TRACKS.value)

    def get_listened_count(self, id: str) -> int:
        return self._get_item_by_id(id)["count"]

    def get_last_listened(self, id: str) -> int:
        return self._get_item_by_id(id)["last_listened"]

    def add_track(self, id: str, name: str, artists: list) -> None:
        if isinstance(artists, str):
            artists = [artists]

        track = {
            "id": id,
            "name": name,
            "artists": artists,
            "count": 0,
            "last_listened": 0,
        }

        self._add_item(track)

    def update_track(self, id: str, timestamp: int) -> None:
        if self.get_track_last_listened(id) >= timestamp:
            return

        count = self._get_item_by_id(id)["count"] + 1
        update = {"count": count, "last_listened": timestamp}

        self._update_item_by_id(id, update)
