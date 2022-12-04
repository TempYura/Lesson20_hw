from flask import request
from flask_restx import Resource, Namespace
from container import movie_service
from deccorators import auth_required, admin_required

movies_ns = Namespace("movies")


@movies_ns.route("/")
class MoviesView(Resource):
    @auth_required
    def get(self):
        """
        Возвращает список всех фильмов.
        Можно фильтровать по director_id и/или genre_id
        """
        args = request.args.to_dict()

        movies = movie_service.get_all(args)

        if not movies:
            return "Не найдено", 404

        return movies, 200

    @admin_required
    def post(self):
        """Добавляет фильм в фильмотеку"""
        req_json = request.json

        movie = movie_service.create(req_json)

        return movie, 201,  {"location": f"/{movies_ns.name}/{movie['id']}"}


@movies_ns.route("/<int:mid>")
class MovieView(Resource):
    @auth_required
    def get(self, mid):
        """Возвращает подробную информацию о фильме"""
        movie = movie_service.get_one(mid)

        if not movie:
            return "Не найдено", 404

        return movie, 200

    @admin_required
    def put(self, mid):
        """Обновляет фильм"""
        req_json = request.json
        req_json["id"] = mid

        movie = movie_service.update(req_json)

        if not movie:
            return "Не найдено", 404

        return movie, 200

    @admin_required
    def delete(self, mid):
        """Удаляет фильм"""
        movie = movie_service.delete(mid)

        if not movie:
            return "Не найдено", 404

        return movie, 200
