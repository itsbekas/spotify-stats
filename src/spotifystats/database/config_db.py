from __future__ import annotations

from typing import TYPE_CHECKING

import spotifystats.models.config as cfg

if TYPE_CHECKING:
    from datetime import datetime

def get_current_timestamp() -> datetime:
    cfg = cfg.Config.get_config()
    return cfg.get_last_updated()

def update_config_timestamp(timestamp: datetime) -> None:
    cfg = cfg.Config.get_config()
    cfg.set_last_updated(timestamp)
    cfg.save()