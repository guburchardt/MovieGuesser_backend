from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.movie import Movie

class MovieRepository(ABC):
    @abstractmethod
    async def get_random_movies(self, count: int) -> List[Movie]:
        pass
    
    @abstractmethod
    async def get_movie_by_id(self, movie_id: int) -> Optional[Movie]:
        pass
    
    @abstractmethod
    async def get_movie_poster(self, poster_path: str) -> bytes:
        pass 