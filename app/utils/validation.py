def validate_film(data):
    required_fields = {
        "filmId": int,
        "title": str,
        "actors": str,  # Può essere una lista o una stringa separata da virgole
        "release_year": int,
        "genre": str,
        "rating": (int, float),  # Può essere un intero o un float
    }
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, {"message": f"Missing fields: {', '.join(missing_fields)}"}

    # Controlla i tipi di dati
    for field, field_type in required_fields.items():
        if not isinstance(data[field], field_type):
            return False, {"message": f"Field '{field}' must be of type {field_type.__name__}"}

    return True, None


def validate_actor(data):
    required_fields = {
        "actorId": int,
        "name": str,
        "surname": str,
        "date_of_birth": str,  # Formato stringa, es: "YYYY-MM-DD"
        "films": str,  # Stringa separata da virgole
    }
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, {"message": f"Missing fields: {', '.join(missing_fields)}"}

    # Controlla i tipi di dati
    for field, field_type in required_fields.items():
        if not isinstance(data[field], field_type):
            return False, {"message": f"Field '{field}' must be of type {field_type.__name__}"}

    return True, None
