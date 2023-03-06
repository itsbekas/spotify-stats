from .base_repository import BaseRepository
from ..models import Config


class ConfigRepository(BaseRepository):
    def __init__(self):
        super().__init__(Config)
