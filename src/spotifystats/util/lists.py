from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from spotifystats.models.dated_document import DatedDocument
    from spotifystats.models.named_document import NamedDocument

import spotifystats.models.play as pl
import spotifystats.models.ranking as rnk


class NamedDocumentList(list):
    def __contains__(self, item: NamedDocument) -> bool:
        ids = [item.get_id() for item in self]
        return item.get_id() in ids


class DatedDocumentList(list):
    def __contains__(self, item: DatedDocument) -> bool:
        if isinstance(self, pl.Play) and isinstance(item, pl.Play):
            return self.get_timestamp() == item.get_timestamp()

        elif isinstance(self, rnk.Ranking) and isinstance(item, rnk.Ranking):
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

        return False
