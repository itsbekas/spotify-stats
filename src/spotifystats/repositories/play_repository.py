from .base_repository import BaseRepository
from ..model import Play


class PlayRepository(BaseRepository):
    def __init__(self):
        super().__init__(Play)
