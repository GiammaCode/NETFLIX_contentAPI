from flask import Blueprint, request, jsonify
from services.db import mongo
from utils.validation import validate_actor

actors_bp = Blueprint("actors", __name__)

@actors_bp.route("/", methods=["GET"])
def get_actors():
    actors = list(mongo.db.actors.find())
    return jsonify(actors), 200

@actors_bp.route("/", methods=["POST"])
def add_actor():
    data = request.json
    valid, error = validate_actor(data)
    if not valid:
        return jsonify(error), 400
    mongo.db.actors.insert_one(data)
    return jsonify({"message": "Actor added successfully"}), 201