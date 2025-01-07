"""
API Blueprint for Film Management

This module defines API routes for managing film-related operations, including
retrieving, adding, updating, and deleting films.

Blueprint:
    - `films_bp`: A Flask Blueprint for film-related routes.

Routes:
    1. `GET /`: Retrieve a list of all films.
    2. `POST /`: Add a new film to the database.
    3. `GET /<int:filmId>`: Retrieve details of a specific film by its ID.
    4. `PUT /<int:filmId>`: Update the details of a specific film by its ID.
    5. `DELETE /<int:filmId>`: Delete a specific film by its ID.

Dependencies:
    - Flask: For routing and handling HTTP requests.
    - pymongo: For database operations with MongoDB.
    - utils.validation.validate_film: For validating film input data.
"""

from flask import Blueprint, request, jsonify
from services.db import mongo
from utils.validation import validate_film

# Define the Blueprint
films_bp = Blueprint("films", __name__)

@films_bp.route("/", methods=["GET"])
def get_films():
    """
    Retrieve all films from the database.

    Returns:
        Response: A JSON response with a list of films and status code 200.
    """
    films = list(mongo.db.films.find())
    for film in films:
        film["_id"] = str(film["_id"])  # Convert ObjectId to string for serialization
    return jsonify(films), 200

@films_bp.route("/", methods=["POST"])
def add_film():
    """
    Add a new film to the database.

    Request Body:
        JSON: Film details (validated using `validate_film`).

    Returns:
        Response:
            - 201: Success message if the film is added.
            - 400: Error message if validation fails.
    """
    data = request.json

    # Validate the film data
    valid, error = validate_film(data)
    if not valid:
        return jsonify(error), 400

    # Insert the film into the database
    mongo.db.films.insert_one(data)

    # Update each actor's films list
    actor_ids = data.get("actors", [])
    if isinstance(actor_ids, str):
        actor_ids = [int(actor_id.strip()) for actor_id in actor_ids.split(",")]

    for actor_id in actor_ids:
        actor = mongo.db.actors.find_one({"actorId": actor_id})
        if actor:
            existing_films = actor.get("films", "").split(", ")
            if str(data["filmId"]) not in existing_films:
                updated_films = ", ".join(filter(None, [str(data["filmId"])] + existing_films))
                mongo.db.actors.update_one(
                    {"actorId": actor_id},
                    {"$set": {"films": updated_films}}
                )

    return jsonify({"message": "Film added and actors updated successfully"}), 201

@films_bp.route("/<int:filmId>", methods=["GET"])
def get_film(filmId):
    """
    Retrieve details of a specific film by its filmId.

    Args:
        filmId (int): The unique ID of the film.

    Returns:
        Response:
            - 200: Film details if found.
            - 404: Error message if the film is not found.
    """
    film = mongo.db.films.find_one({"filmId": filmId})
    if film:
        film["_id"] = str(film["_id"])
        return jsonify(film), 200
    return jsonify({"error": "Film not found"}), 404

@films_bp.route("/<int:filmId>", methods=["PUT"])
def update_film(filmId):
    """
    Update details of a specific film by its filmId.

    Args:
        filmId (int): The unique ID of the film.

    Request Body:
        JSON: Updated film details.

    Returns:
        Response:
            - 200: Updated film details if successful.
            - 404: Error message if the film is not found.
    """
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

@films_bp.route("/<int:filmId>", methods=["DELETE"])
def delete_film(filmId):
    """
    Delete a specific film by its filmId.

    Args:
        filmId (int): The unique ID of the film.

    Returns:
        Response:
            - 204: No content if deletion is successful.
            - 404: Error message if the film is not found.
    """
    result = mongo.db.films.delete_one({"filmId": filmId})
    if result.deleted_count > 0:
        return "", 204
    return jsonify({"error": "Film ID not found"}), 404

@films_bp.route("/<int:filmId>/actors", methods=["GET"])
def get_actors_by_film(filmId):
    """
    Retrieve a list of actors associated with a specific film.

    Args:
        filmId (int): The unique ID of the film.

    Returns:
        Response:
            - 200: List of associated actors if successful.
            - 400: Error message if the actor ID format is invalid.
            - 404: Error message if the film is not found.
    """
    # Trova il film corrispondente all'ID
    film = mongo.db.films.find_one({"filmId": filmId})
    if not film:
        return jsonify({"error": "Film not found"}), 404

    # Recupera gli ID degli attori dal film
    actor_ids = film.get("actors", [])
    if not actor_ids:
        return jsonify({"actors": []}), 200

    try:
        # Converti gli ID degli attori in formato integer
        actor_ids = [int(actor_id) for actor_id in actor_ids]
    except ValueError:
        return jsonify({"error": "Invalid actor ID format"}), 400

    # Trova gli attori corrispondenti
    actors = list(mongo.db.actors.find({"actorId": {"$in": actor_ids}}))
    for actor in actors:
        actor["_id"] = str(actor["_id"])  # Converti ObjectId in stringa per la serializzazione

    return jsonify({"filmId": filmId, "actors": actors}), 200
