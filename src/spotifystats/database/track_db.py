from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import spotifystats.models.track as trk

def add_track(track: trk.Track) -> None:
    track.save()