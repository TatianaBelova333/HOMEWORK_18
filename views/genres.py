from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service


genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200

    def post(self):
        data = request.json
        genre = genre_service.create(data)
        return '', 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200

    def delete(self, gid):
        genre_service.delete(gid)
        return '', 204

    def put(self, gid):
        data = request.json
        genre_service.update(gid, data)
        return '', 204

    def patch(self, gid):
        data = request.json
        genre_service.update_partial(gid, data)
        return '', 204
