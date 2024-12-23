from flask import Blueprint, request, jsonify
from services.db import mongo
from utils.validation import validate_film

films_bp = Blueprint("films", __name__)

@films_bp.route("/", methods=["GET"])
def get_films():
    films = list(mongo.db.films.find())
    # Convertire il campo `_id` in stringa
    for film in films:
        film["_id"] = str(film["_id"])
    return jsonify(films), 200

@films_bp.route("/", methods=["POST"])
def add_film():
    data = request.json
    valid, error = validate_film(data)
    if not valid:
        return jsonify(error), 400
    mongo.db.films.insert_one(data)
    return jsonify({"message": "Film added successfully"}), 201
