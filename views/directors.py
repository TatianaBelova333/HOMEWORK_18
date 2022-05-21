from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service


director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200

    def post(self):
        data = request.json
        director = director_service.create(data)
        return '', 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200

    def delete(self, did):
        director_service.delete(did)
        return '', 204

    def put(self, did):
        data = request.json
        director_service.update(did, data)
        return '', 204

    def patch(self, did):
        data = request.json
        director_service.update_partial(did, data)
        return '', 204
