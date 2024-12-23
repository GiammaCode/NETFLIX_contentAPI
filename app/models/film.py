class Film:
    def __init__(self, filmId, title, actors, release_year, genre, rating):
        self.filmId = filmId  # ID univoco del film (integer)
        self.title = title  # Titolo del film (string)
        self.actors = actors  # Lista di ID degli attori nel film (string o list)
        self.release_year = release_year  # Anno di rilascio (integer)
        self.genre = genre  # Genere del film (string)
        self.rating = rating  # Valutazione del film (float)

    def to_dict(self):
        """Converti l'oggetto Film in un dizionario serializzabile in JSON."""
        return {
            "filmId": self.filmId,
            "title": self.title,
            "actors": self.actors,
            "release_year": self.release_year,
            "genre": self.genre,
            "rating": self.rating,
        }

    @staticmethod
    def from_dict(data):
        """Crea un'istanza di Film da un dizionario."""
        return Film(
            title=data.get("title"),
            actors=data.get("actors"),
            release_year=data.get("release_year"),
            genre=data.get("genre"),
            rating=data.get("rating"),
        )
