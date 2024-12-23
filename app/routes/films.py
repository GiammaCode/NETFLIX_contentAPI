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


@films_bp.route('/<int:filmId>', methods=["GET"])
def get_film(filmId):
    film = mongo.db.films.find_one({"filmId": filmId})
    if film:
        film["_id"] = str(film["_id"])
        return jsonify(film), 200
    return jsonify({"error": "film not found"}), 404


@films_bp.route('/<int:filmId>', methods=["PUT"])
def update_film(filmId):
    data = request.json
    updated_film = mongo.db.films.find_one_and_update(
        {"filmId": filmId},
        {"$set": data},
        return_document=True
    )
    if updated_film:
        updated_film["_id"] = str(updated_film["_id"])
        return jsonify(updated_film), 200
    return jsonify({"error": "Film not found"}), 404


@films_bp.route('/<int:filmId>', methods=["DELETE"])
def delete_film(filmId):
    result = mongo.db.films.delete_one({"filmId": filmId})
    if result.deleted_count > 0:
        return "", 204
    return jsonify({"error": "filmId not found"}), 404







