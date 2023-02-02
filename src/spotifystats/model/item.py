class Item:
    def __init__(self, item: dict) -> None:
        self.id: str = item["id"]

    def to_dict(self) -> dict:
        return {"id": self.id}

    def __eq__(self, other) -> bool:
        return type(self) == type(other) and self.id == other.id
