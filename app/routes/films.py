from flask import Blueprint, request, jsonify
from services.db import mongo
from utils.validation import validate_film

films_bp = Blueprint("films", __name__)



@films_bp.route("", methods=["GET"])
def get_films():
    films = list(mongo.db.films.find())
    # Convertire il campo `_id` in stringa
    for film in films:
        film["_id"] = str(film["_id"])
    return jsonify(films), 200

@films_bp.route("", methods=["POST"])
def add_film():

    data = request.json
    valid, error = validate_film(data)
    if not valid:
        return jsonify(error), 400
    mongo.db.films.insert_one(data)
    return jsonify({"message": "Film added successfully"}), 201


@films_bp.route('/<int:content_id>', methods=["GET"])
def get_film(content_id):
    films = list(mongo.db.films.find())

    # Cerca un film per ID
    film = next((c for c in films if c['id'] == content_id), None)
    if not film:
        abort(404, description="Content not found")
    film["_id"] = str(film["_id"])
    return jsonify(film)


@films_bp.route('/<int:content_id>', methods=["PUT"])
def update_film(content_id):
    films = list(mongo.db.films.find())
    film = next((c for c in films if c['id'] == content_id), None)
    data = request.json
    valid, error = validate_film(data)
    if not valid:
        return jsonify(error), 400

    # Aggiorna i campi del film esistente
    mongo.db.films.update_one(
        {"_id": content_id},
        {"$set": data}  # Aggiorna solo i campi forniti
    )

    return jsonify(film), 200


@films_bp.route('/<int:content_id>', methods=["DELETE"])
def delete_film(content_id):
    films = list(mongo.db.films.find())
    film = next((c for c in films if c['id'] == content_id), None)
    if not film:
        abort(404, description="Content not found")

    # Rimuove il film dalla lista
    mongo.db.films.delete_one(film)
    return jsonify({"message": f"Film with id {content_id} deleted successfully"}), 200








