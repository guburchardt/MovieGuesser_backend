import pytest
from src.infrastructure.external.tmdb_client import TMDBClient
from requests.exceptions import HTTPError

# Teste integracao API
@pytest.mark.asyncio
async def test_tmdb_integration():
    client = TMDBClient()
    
    movies = await client.get_random_movies(4)
    
    assert len(movies) == 4
    for movie in movies:
        assert "id" in movie
        assert "title" in movie
        assert "poster_path" in movie
        
        if movie["poster_path"]:
            poster_data = await client.get_movie_poster(movie["poster_path"])
            assert isinstance(poster_data, bytes)
            assert len(poster_data) > 0 

# Teste filmes aleatorios
@pytest.mark.asyncio
async def test_get_random_movies():
    client = TMDBClient()
    movies = await client.get_random_movies(4)
    
    assert len(movies) == 4
    for movie in movies:
        assert "id" in movie
        assert "title" in movie
        assert "poster_path" in movie

# Teste poster filme
@pytest.mark.asyncio
async def test_get_movie_poster():
    client = TMDBClient()
    movies = await client.get_random_movies(1)
    movie = movies[0]
    
    if movie["poster_path"]:
        poster_data = await client.get_movie_poster(movie["poster_path"])
        assert isinstance(poster_data, bytes)
        assert len(poster_data) > 0

# Teste filme por id
@pytest.mark.asyncio
async def test_get_movie_by_id():
    client = TMDBClient()
    movies = await client.get_random_movies(1)
    movie_id = movies[0]["id"]
    
    movie = await client.get_movie_by_id(movie_id)
    assert movie["id"] == movie_id
    assert "title" in movie
    assert "poster_path" in movie

# Teste opcoes filme
@pytest.mark.asyncio
async def test_get_movie_options():
    client = TMDBClient()
    movies = await client.get_random_movies(4)
    
    movie_ids = [movie["id"] for movie in movies]
    assert len(set(movie_ids)) 
    
    for movie in movies:
        assert movie["poster_path"] is not None
