from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from spotifystats.models.named_document import NamedDocument


def is_duplicate(new_item: NamedDocument, item_list: List[NamedDocument]):
    ids = [item.get_id() for item in item_list]
    return new_item.get_id() in ids
