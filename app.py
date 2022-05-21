from flask import Flask
from flask_restx import Api
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from setup_db import db
from config import Config
from constants import DATA
from dao.model.movie import Movie
from dao.model.director import Director
from dao.model.genre import Genre


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()
        movies = []
        for movie in DATA["movies"]:
            m = Movie(
                id=movie["pk"],
                title=movie["title"],
                description=movie["description"],
                trailer=movie["trailer"],
                year=movie["year"],
                rating=movie["rating"],
                genre_id=movie["genre_id"],
                director_id=movie["director_id"],
            )
            movies.append(m)
        with db.session.begin():
            db.session.add_all(movies)

        directors = []
        for director in DATA["directors"]:
            d = Director(
                id=director["pk"],
                name=director["name"],
            )
            directors.append(d)
        with db.session.begin():
            db.session.add_all(directors)

        genres = []
        for genre in DATA["genres"]:
            g = Genre(
                id=genre["pk"],
                name=genre["name"],
            )
            genres.append(g)
        with db.session.begin():
            db.session.add_all(genres)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)

