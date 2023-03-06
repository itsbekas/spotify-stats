from .base_repository import BaseRepository
from ..models import Album


class AlbumRepository(BaseRepository):
    def __init__(self):
        super().__init__(Album)
