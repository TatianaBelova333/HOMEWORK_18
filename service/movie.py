# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

from dao.movie import MovieDAO


class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.dao = movie_dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, mid, data):
        movie = self.get_one(mid)
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')
        self.dao.update(movie)

    def update_partial(self, mid, data):
        movie = self.get_one(mid)
        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'genre_id' in data:
            movie.genre_id = data.get('genre_id')
        if 'director_id' in data:
            movie.director_id = data.get('director_id')
        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)

    def filter_by_param(self, param):
        if param.get('genre_id'):
            gid = param.get('genre_id', type=int)
            return self.dao.filter_by_genre_id(gid)
        elif param.get('director_id'):
            did = param.get('director_id', type=int)
            return self.dao.filter_by_director_id(did)
        elif param.get('year'):
            year = param.get('year', type=int)
            return self.dao.filter_by_year(year)