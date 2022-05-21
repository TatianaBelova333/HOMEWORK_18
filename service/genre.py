from dao.genre import GenreDAO


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.dao = genre_dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, gid, data):
        genre = self.get_one(gid)
        genre.name = data.get('name')
        self.dao.update(genre)

    def update_partial(self, gid, data):
        genre = self.get_one(gid)
        if 'name' in data:
            genre.name = data.get('name')
        self.dao.update(genre)

    def delete(self, gid):
        self.dao.delete(gid)

