from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from spotifystats.models.dated_document import DatedDocument
    from spotifystats.models.named_document import NamedDocument


class NamedDocumentList(list):
    def __contains__(self, item: NamedDocument) -> bool:
        ids = [item.get_id() for item in self]
        return item.get_id() in ids


class DatedDocumentList(list):
    def __contains__(self, item: DatedDocument) -> bool:
        timestamps = [item.get_timestamp() for item in self]
        return item.get_timestamp() in timestamps
