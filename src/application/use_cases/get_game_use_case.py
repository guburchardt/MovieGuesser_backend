from typing import Dict, Any
import random
from src.domain.services.movie_service import MovieService
from src.interfaces.utils.image_utils import apply_blur

class GetGameUseCase:
    def __init__(self, movie_service: MovieService):
        self.movie_service = movie_service
    
    async def execute(self, blur_level: int = 1) -> Dict[str, Any]:
        correct_movie, wrong_options = await self.movie_service.get_game_data()
        
        if not correct_movie.get('poster_path'):
            raise Exception("Filme selecionado não possui poster")
        
        poster_data = await self.movie_service.movie_repository.get_movie_poster(
            correct_movie['poster_path']
        )
        
        blurred_image = apply_blur(poster_data, blur_level)
        
        all_options = [correct_movie] + wrong_options
        random.shuffle(all_options)
        
        return {
            "image": blurred_image,
            "options": [
                {"id": movie['id'], "title": movie['title']}
                for movie in all_options
            ],
            "correct_id": correct_movie['id']
        } 