from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get_or_404(gid)

    def get_all(self):
        entity_list = self.session.query(Genre).all()
        return entity_list

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()