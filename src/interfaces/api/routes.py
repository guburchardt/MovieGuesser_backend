from flask import Blueprint, jsonify, request
from src.application.use_cases.get_game_use_case import GetGameUseCase
from src.application.use_cases.update_blur_use_case import UpdateBlurUseCase
from src.application.use_cases.reveal_movie_use_case import RevealMovieUseCase
from src.infrastructure.external.tmdb_client import TMDBClient
from src.domain.services.movie_service import MovieService

api = Blueprint('api', __name__)
movie_repository = TMDBClient()
movie_service = MovieService(movie_repository)

@api.route("/game", methods=['GET'])
async def get_game():
    try:
        blur_level = int(request.args.get('blur_level', 1))
        use_case = GetGameUseCase(movie_service)
        result = await use_case.execute(blur_level)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api.route('/update_blur/<int:movie_id>', methods=['GET'])
async def update_blur(movie_id):
    try:
        blur_level = int(request.args.get('blur_level', 1))
        use_case = UpdateBlurUseCase(movie_service)
        result = await use_case.execute(movie_id, blur_level)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api.route('/reveal/<int:movie_id>', methods=['GET'])
async def reveal_movie(movie_id):
    try:
        use_case = RevealMovieUseCase(movie_service)
        result = await use_case.execute(movie_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500 