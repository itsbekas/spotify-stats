from spotifystats.database.base import Database, Collection

class CommonDatabase(Database):

    def __init__(self, dbname: str) -> None:
        super().__init__(dbname, Collection.COMMON.value)

    def get_timestamp(self):
        return self._get_item_by_id(Collection.COMMON.value)["timestamp"]

    def set_timestamp(self, timestamp: int) -> None:
        self._update_item_by_id({"timestamp": timestamp})