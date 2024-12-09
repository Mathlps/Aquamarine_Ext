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

@animal_route.route("/animal/<int:id>", methods=['PUT'])
@jwt_required()
def update_animal_by_id(id):
    data = request.json
    response, status = AnimalService.update_animal_register(data, id)
    return jsonify(response), status

@animal_route.route("/animal/<int:id>", methods=['GET'])
def get_animal_by_id(id):

    response, status = AnimalService.get_animal_by_id(id)
    return jsonify(response), status

@animal_route.route("/animais", methods=['GET'])
def list_all_animals():
    response, status = AnimalService.list_all_animals()
    return jsonify(response), status

@animal_route.route("/animal/projeto/<int:id_project>", methods=['GET'])
def get_animals_from_project(id_project):

    response, status = AnimalService.get_animals_from_project(id_project)
    return jsonify(response), status

@animal_route.route("/animal/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_animal(id):
    response, status = AnimalService.delete_animal(id)
    return jsonify(response), status

@animal_route.route("/animal/<int:id>/vincular/<int:id_project>", methods=['PUT'])
@jwt_required()
def link_animal_to_project(id, id_project):
    response, status = AnimalService.link_animal_to_project(id, id_project)
    return jsonify(response), status


@animal_route.route("/animal/<int:id>/desvincular", methods=['PUT'])
@jwt_required()
def unlink_animal_from_project(id):
    response, status = AnimalService.unlink_animal_from_project(id)
    return jsonify(response), status