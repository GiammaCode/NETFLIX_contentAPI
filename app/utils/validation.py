def validate_film(data):
    required_fields = ["title", "release_year", "genre", "rating"]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, {"message": f"Missing fields: {', '.join(missing_fields)}"}
    return True, None

def validate_actor(data):
    required_fields = ["name", "surname", "date_of_birth"]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, {"message": f"Missing fields: {', '.join(missing_fields)}"}
    return True, None
