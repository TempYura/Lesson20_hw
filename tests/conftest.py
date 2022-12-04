from unittest.mock import MagicMock

import pytest

from dao.model.director import Director
from dao.director import DirectorDAO

from dao.model.genre import Genre
from dao.genre import GenreDAO

from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name='Director 1')
    director_2 = Director(id=2, name='Director 2')
    director_3 = Director(id=3, name='Director 3')

    directors = {1: director_1, 2: director_2, 3: director_3}

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.create = MagicMock(return_value=director_1)
    director_dao.delete = MagicMock(return_value=director_1)
    director_dao.update = MagicMock(return_value=director_1)

    return director_dao

@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name='Genre 1')
    genre_2 = Genre(id=2, name='Genre 2')
    genre_3 = Genre(id=3, name='Genre 3')

    genres = {1: genre_1, 2: genre_2, 3: genre_3}

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.create = MagicMock(return_value=genre_1)
    genre_dao.delete = MagicMock(return_value=genre_1)
    genre_dao.update = MagicMock(return_value=genre_1)

    return genre_dao

@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='Movie 1', description="description", trailer="trailer", year=1234, rating=10.0, genre_id=1, director_id=1)
    movie_2 = Movie(id=1, title='Movie 2', description="description", trailer="trailer", year=2222, rating=10.0, genre_id=2, director_id=2)
    movie_3 = Movie(id=1, title='Movie 3', description="description", trailer="trailer", year=3333, rating=10.0, genre_id=3, director_id=3)

    movies = {1: movie_1, 2: movie_2, 3: movie_3}

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=movies.values())
    movie_dao.create = MagicMock(return_value=movie_1)
    movie_dao.delete = MagicMock(return_value=movie_1)
    movie_dao.update = MagicMock(return_value=movie_1)

    return movie_dao
