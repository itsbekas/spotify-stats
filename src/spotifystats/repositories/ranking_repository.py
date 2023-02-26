from .base_repository import BaseRepository
from ..model.ranking import Ranking


class RankingRepository(BaseRepository):
    def __init__(self):
        super().__init__(Ranking)
