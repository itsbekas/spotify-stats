from spotifystats.database.base import Database, Collection
from spotifystats.model import Artist


class ArtistDatabase(Database):
    def __init__(self, dbname: str) -> None:
        super().__init__(dbname, Collection.ARTISTS.value)

    def get_artist(self, id: str) -> Artist:
        return Artist(self._get_item_by_id(id))

    def get_listened_count(self, id: str):
        return self._get_item_by_id(id)["count"]

    def get_last_listened(self, id: str):
        return self._get_item_by_id(id)["last_listened"]

    def add_artist(self, artist: Artist) -> None:
        self._add_item(artist)

    def update_artist(self, id: str, timestamp: int) -> None:
        artist: Artist = self.get_artist(id)
        if artist.last_listened >= timestamp:
            return

        count = artist.count + 1
        update = {"count": count, "last_listened": timestamp}
        self._update_item_by_id(id, update)
