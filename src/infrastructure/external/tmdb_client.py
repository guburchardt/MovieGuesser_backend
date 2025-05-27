import requests
from typing import List, Optional
from src.domain.entities.movie import Movie
from src.domain.repositories.movie_repository import MovieRepository
from src.infrastructure.config.settings import settings

class TMDBClient(MovieRepository):
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {settings.TMDB_API_KEY}",
            "accept": "application/json"
        }
    
    async def get_random_movies(self, count: int) -> List[Movie]:
        page = 1  # Você pode implementar a lógica de página aleatória aqui
        response = requests.get(
            f"{settings.TMDB_BASE_URL}/discover/movie",
            params={
                "page": page,
                "sort_by": "popularity.desc",
                "include_adult": False,
                "include_video": False,
                "language": "en-US"
            },
            headers=self.headers
        )
        
        if response.status_code != 200:
            raise Exception("Erro ao buscar filmes")
            
        data = response.json()
        movies = data["results"][:count]
        return [Movie(**movie).to_dict() for movie in movies]
    
    async def get_movie_by_id(self, movie_id: int) -> Optional[Movie]:
        response = requests.get(
            f"{settings.TMDB_BASE_URL}/movie/{movie_id}",
            headers=self.headers
        )
        
        if response.status_code != 200:
            return None
            
        return Movie(**response.json()).to_dict()
    
    async def get_movie_poster(self, poster_path: str) -> bytes:
        response = requests.get(
            f"{settings.TMDB_IMAGE_BASE_URL}{poster_path}",
            headers=self.headers
        )
        
        if response.status_code != 200:
            raise Exception("Erro ao buscar poster")
            
        return response.content 