from .base_repository import BaseRepository
from ..models import Play


class PlayRepository(BaseRepository):
    def __init__(self):
        super().__init__(Play)
