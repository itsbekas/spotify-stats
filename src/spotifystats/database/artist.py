from spotifystats.database.base import Database, Collection


class ArtistDatabase(Database):
    def __init__(self, dbname: str) -> None:
        super().__init__(dbname, Collection.ARTISTS.value)

    def get_listened_count(self, id: str):
        return self._get_item_by_id(id)["count"]

    def get_last_listened(self, id: str):
        return self._get_item_by_id(id)["last_listened"]

    def add_artist(self, id, name) -> None:
        artist = {"id": id, "name": name, "count": 0, "last_listened": 0}

        self._add_item(artist)

    def update_artist(self, id: str, timestamp: int) -> None:
        if self.get_artist_last_listened(id) >= timestamp:
            return

        count = self._get_item_by_id(id)["count"] + 1
        update = {"count": count, "last_listened": timestamp}
        self._update_item_by_id(id, update)
