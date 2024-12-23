class Actor:
    def __init__(self, actorId, name, surname, date_of_birth, films):
        self.actorId = actorId
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.films = films

    def to_dict(self):
        return {
            "actorId": self.actorId,
            "name": self.name,
            "surname": self.surname,
            "date_of_birth": self.date_of_birth,
            "films": self.films
        }
