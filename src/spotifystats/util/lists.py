from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import spotifystats.models.play as pl
    import spotifystats.models.ranking as rnk
    from spotifystats.models.named_document import NamedDocument


class NamedDocumentList(list):
    def __contains__(self, item: NamedDocument) -> bool:
        ids = [item.get_id() for item in self]
        return item.get_id() in ids


class RankingDocumentList(list):
    def __contains__(self, item: rnk.Ranking) -> bool:
        documents = [
            {
                "timestamp": document.get_timestamp(),
                "time_range": document.get_time_range(),
            }
            for document in self
        ]

        return {
            "timestamp": item.get_timestamp(),
            "time_range": item.get_time_range(),
        } in documents


class PlayDocumentList(list):
    def __contains__(self, item: pl.Play) -> bool:
        timestamps = [play.get_timestamp() for play in self]
        return item.get_timestamp() in timestamps
