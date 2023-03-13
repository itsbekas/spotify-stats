from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import spotifystats.models.artist as art

def add_artist(artist: art.Artist) -> None:
    artist.save()
