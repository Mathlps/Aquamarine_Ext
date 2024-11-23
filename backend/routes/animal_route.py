from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from service.animal_service import AnimalService

animal_route = Blueprint("animal", __name__)

@animal_route.route("/animal", methods=['POST'])
@jwt_required()
def register_animal():
    data = request.json
    response, status = AnimalService.register_animal(data)
    return jsonify(response), status

@animal_route.route("/animal/<int:id>", methods=['GET'])
def get_animal_by_id(id):

    response, status = AnimalService.get_animal_by_id(id)
    return jsonify(response), status

@animal_route.route("/animal/<int:id_project>", methods=['GET'])
def get_animals_from_project(id_project):

    response, status = AnimalService.get_animals_from_project(id_project)
    return jsonify(response), status

@animal_route.route("/animal/<int:id>", methods=['DELETE'])
@jwt_required()
def remove_animal(id):
    response, status = AnimalService.remove_animal(id)
    return jsonify(response), status