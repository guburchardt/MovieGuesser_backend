import os
from dataclasses import dataclass

@dataclass
class Settings:
    TMDB_API_KEY: str = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZGJlODA2ZGU5NDhlYjNlYmIxMzhmMTY4YmZkNTEwYiIsIm5iZiI6MTc0NjgwMTkyMy43NzMsInN1YiI6IjY4MWUxNTAzZWQ1YzY5ZGIzZjg4YzhlYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7HtJl3EjRHwKpndZFf3q7WJ3SB9J1liokbwJXmoFnBQ"
    TMDB_BASE_URL: str = "https://api.themoviedb.org/3"
    TMDB_IMAGE_BASE_URL: str = "https://image.tmdb.org/t/p/w500"
    DEBUG: bool = True

settings = Settings() 