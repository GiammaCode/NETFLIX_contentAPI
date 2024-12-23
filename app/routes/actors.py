from flask import Blueprint, request, jsonify
from services.db import mongo
from utils.validation import validate_actor

actors_bp = Blueprint("actors", __name__)

@actors_bp.route("/", methods=["GET"])
def get_actors():
    actors = list(mongo.db.actors.find())
    # Converti ObjectId in stringa per ogni attore
    for actor in actors:
        actor["_id"] = str(actor["_id"])
    return jsonify(actors), 200

@actors_bp.route("/", methods=["POST"])
def add_actor():
    data = request.json
    valid, error = validate_actor(data)
    if not valid:
        return jsonify(error), 400
    mongo.db.actors.insert_one(data)
    return jsonify({"message": "Actor added successfully"}), 201


# GET a specific actor by actorId
@actors_bp.route("/<int:actorId>", methods=["GET"])
def get_actor_by_id(actorId):
    actor = mongo.db.actors.find_one({"actorId": actorId})
    if actor:
        actor["_id"] = str(actor["_id"])
        return jsonify(actor), 200
    return jsonify({"error": "Actor not found"}), 404

# UPDATE a specific actor by actorId
@actors_bp.route("/<int:actorId>", methods=["PUT"])
def update_actor(actorId):
    data = request.json
    updated_actor = mongo.db.actors.find_one_and_update(
        {"actorId": actorId},
        {"$set": data},
        return_document=True
    )
    if updated_actor:
        updated_actor["_id"] = str(updated_actor["_id"])
        return jsonify(updated_actor), 200
    return jsonify({"error": "Actor not found"}), 404

# DELETE a specific actor by actorId
@actors_bp.route("/<int:actorId>", methods=["DELETE"])
def delete_actor(actorId):
    result = mongo.db.actors.delete_one({"actorId": actorId})
    if result.deleted_count > 0:
        return "", 204
    return jsonify({"error": "Actor not found"}), 404

@actors_bp.route("/<int:actorId>/films", methods=["GET"])
def get_films_by_actor(actorId):
    # Recupera l'attore dal database
    actor = mongo.db.actors.find_one({"actorId": actorId})
    if actor:
        # Recupera la lista di filmId associati all'attore
        film_ids = actor.get("films", "").split(", ")
        # Converti i filmId in interi, se necessario
        try:
            film_ids = [int(film_id) for film_id in film_ids]
        except ValueError:
            return jsonify({"error": "Invalid film ID format"}), 400
        # Recupera i dettagli dei film dalla collezione 'films'
        films = list(mongo.db.films.find({"filmId": {"$in": film_ids}}))
        # Converte `_id` in stringa per evitare errori di serializzazione
        for film in films:
            film["_id"] = str(film["_id"])
        return jsonify({"actorId": actorId, "films": films}), 200
    # Se l'attore non esiste
    return jsonify({"error": "Actor not found"}), 404
