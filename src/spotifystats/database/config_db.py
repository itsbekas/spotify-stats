from datetime import datetime

from spotifystats.models.config import Config


def get_config() -> Config:
    return Config.objects().first()


def set_config(config: Config) -> None:
    config.save()


def get_last_ranking_update() -> datetime:
    return get_config().get_last_ranking_update()


def set_last_ranking_update(last_ranking_update: datetime) -> None:
    config = get_config()
    config.set_last_ranking_update(last_ranking_update)
    set_config(config)
