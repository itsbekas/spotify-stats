from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime

import spotifystats.models.config as cfg


def get_current_timestamp() -> datetime:
    config = cfg.Config.get_config()
    return config.get_last_updated()


def update_config_timestamp(timestamp: datetime) -> None:
    config = cfg.Config.get_config()
    config.set_last_updated(timestamp)
    config.save()