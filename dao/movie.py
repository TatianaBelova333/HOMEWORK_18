from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get_or_404(mid)

    def get_all(self):
        entity_list = self.session.query(Movie).all()
        return entity_list

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

    def filter_by_genre_id(self, gid):
        movies = self.session.query(Movie).filter(Movie.genre_id == gid).all()
        return movies

    def filter_by_director_id(self, did):
        movies = self.session.query(Movie).filter(Movie.director_id == did).all()
        return movies

    def filter_by_year(self, year):
        movies = self.session.query(Movie).filter(Movie.year == year).all()
        return movies

