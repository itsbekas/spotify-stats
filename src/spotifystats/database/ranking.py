from base import Database, Collection

class RankingDatabase(Database):

    def __init__(self, dbname: str) -> None:
        super().__init__(dbname, Collection.RANKINGS.value)

    def create_ranking(self, timestamp: int) -> None:
        ranking = {
            "id": timestamp,
        }

        self._add_item(Collection.RANKINGS.value, ranking)

    def add_ranking(self, timestamp, ids, collection, range) -> None:
        ranking = { f"{collection}-{range}": ids }

        self._update_item_by_id(Collection.RANKINGS.value, timestamp, ranking)

    def get_ranking(self, timestamp, range) -> None:
        return self._get_item(Collection.RANKINGS.value, timestamp)
