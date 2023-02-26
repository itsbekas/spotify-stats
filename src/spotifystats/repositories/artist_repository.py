from .base_repository import BaseRepository
from ..model import Artist


class ArtistRepository(BaseRepository):
    def __init__(self):
        super().__init__(Artist)
