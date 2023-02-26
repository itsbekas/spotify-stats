from .base_repository import BaseRepository
from ..model import Album


class AlbumRepository(BaseRepository):
    def __init__(self):
        super().__init__(Album)
