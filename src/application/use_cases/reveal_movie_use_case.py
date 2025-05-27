from typing import Dict, Any
import base64
from src.domain.services.movie_service import MovieService

class RevealMovieUseCase:
    def __init__(self, movie_service: MovieService):
        self.movie_service = movie_service
    
    async def execute(self, movie_id: int) -> Dict[str, Any]:
        movie = await self.movie_service.movie_repository.get_movie_by_id(movie_id)
        
        if not movie:
            raise Exception("Filme não encontrado")
            
        if not movie.get('poster_path'):
            raise Exception("Filme não possui poster")
            
        poster_data = await self.movie_service.movie_repository.get_movie_poster(
            movie['poster_path']
        )
        
        return {
            "image": base64.b64encode(poster_data).decode(),
            "title": movie['title']
        } 