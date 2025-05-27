from typing import Dict, Any
from src.domain.services.movie_service import MovieService
from src.interfaces.utils.image_utils import apply_blur

class UpdateBlurUseCase:
    def __init__(self, movie_service: MovieService):
        self.movie_service = movie_service
    
    async def execute(self, movie_id: int, blur_level: int) -> Dict[str, Any]:
        movie = await self.movie_service.movie_repository.get_movie_by_id(movie_id)
        
        if not movie:
            raise Exception("Filme não encontrado")
            
        if not movie.get('poster_path'):
            raise Exception("Filme não possui poster")
            
        poster_data = await self.movie_service.movie_repository.get_movie_poster(
            movie['poster_path']
        )
        
        blurred_image = apply_blur(poster_data, blur_level)
        
        return {
            "image": blurred_image,
            "id": movie_id,
            "title": movie['title']
        } 