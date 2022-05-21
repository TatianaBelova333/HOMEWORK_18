# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        param = request.args
        if param:
            movies = movie_service.filter_by_param(param)
        else:
            movies = movie_service.get_all()
        return movies_schema.dump(movies), 200

    def post(self):
        data = request.json
        movie = movie_service.create(data)
        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204

    def put(self, mid):
        data = request.json
        movie_service.update(mid, data)
        return '', 204

    def patch(self, mid):
        data = request.json
        movie_service.update_partial(mid, data)
        return '', 204


