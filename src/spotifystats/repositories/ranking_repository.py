from .base_repository import BaseRepository
from ..models.ranking import Ranking


class RankingRepository(BaseRepository):
    def __init__(self):
        super().__init__(Ranking)
