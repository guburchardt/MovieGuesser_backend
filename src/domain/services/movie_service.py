from typing import List, Tuple, Dict, Any
import random
from src.domain.entities.movie import Movie
from src.domain.repositories.movie_repository import MovieRepository

class MovieService:
    def __init__(self, movie_repository: MovieRepository):
        self.movie_repository = movie_repository
    
    async def get_game_data(self) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
        movies = await self.movie_repository.get_random_movies(20)
        correct_movie = random.choice(movies)
        other_movies = [m for m in movies if m['id'] != correct_movie['id']]
        wrong_options = random.sample(other_movies, 3)
        return correct_movie, wrong_options 