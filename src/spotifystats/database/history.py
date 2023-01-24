from base import Database, Collection

class HistoryDatabase(Database):

    def __init__(self, dbname: str) -> None:
        super().__init__(dbname, Collection.HISTORY.value)

    def add_history(self, history, timestamp) -> None:
        db_history = {
            "id": timestamp,
            "history": history
        }

        self._add_item(Collection.HISTORY.value, db_history)