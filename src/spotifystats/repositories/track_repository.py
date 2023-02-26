from .base_repository import BaseRepository
from ..model.track import Track


class TrackRepository(BaseRepository):
    def __init__(self):
        super().__init__(Track)
