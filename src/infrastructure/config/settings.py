import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

@dataclass
class Settings:
    TMDB_API_KEY: str = os.getenv('TMDB_API_KEY', '')
    TMDB_BASE_URL: str = os.getenv('TMDB_BASE_URL', 'https://api.themoviedb.org/3')
    TMDB_IMAGE_BASE_URL: str = os.getenv('TMDB_IMAGE_BASE_URL', 'https://image.tmdb.org/t/p/w500')
    DEBUG: bool = os.getenv('DEBUG', 'True').lower() == 'true'

settings = Settings() 