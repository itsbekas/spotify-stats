from __future__ import annotations

from typing import TYPE_CHECKING

import spotifystats.models.config as cfg

if TYPE_CHECKING:
    from datetime import datetime
    import spotifystats.models.artist as art
    import spotifystats.models.track as trk

def add_artist(artist: art.Artist) -> None:
    artist.save()

def add_track(track: trk.Track) -> None:
    track.save()

def update_config_timestamp(timestamp: datetime) -> None:
    cfg.Config.set_last_updated(timestamp)