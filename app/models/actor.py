class Actor:
    def __init__(self, actorId: int, name: str, surname: str, date_of_birth: str, films: str):
        self.actorId = actorId  # ID dell'attore
        self.name = name  # Nome dell'attore
        self.surname = surname  # Cognome dell'attore
        self.date_of_birth = date_of_birth  # Data di nascita
        self.films = films  # Lista di ID dei film in cui ha recitato (es. "1, 33")

    def to_dict(self):
        """Converte l'oggetto Actor in un dizionario serializzabile in JSON."""
        return {
            "actorId": self.actorId,
            "name": self.name,
            "surname": self.surname,
            "date_of_birth": self.date_of_birth,
            "films": self.films,
        }

    @staticmethod
    def from_dict(data):
        """Crea un'istanza di Actor da un dizionario."""
        return Actor(
            id=data.get("id"),
            name=data.get("name"),
            surname=data.get("surname"),
            date_of_birth=data.get("dateOfBirth"),
            films=data.get("films"),
        )
