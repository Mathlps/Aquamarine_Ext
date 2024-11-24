from flask import Flask, jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from service.project_service import ProjectService

project_route = Blueprint("project", __name__)

@project_route.route("/projeto", methods=['POST'])
@jwt_required()
def create_project():
    print("Dentro do Route")
    data = request.json
    response, status = ProjectService.create_project(data)
    return jsonify(response), status
    
@project_route.route("/projeto/<int:id>", methods=['PUT'])
@jwt_required()
def update_project_by_id(id):
    data = request.json
    response, status = ProjectService.update_project(data, id)
    return jsonify(response), status

@project_route.route("/projeto/<int:id>", methods=['GET'])
# @jwt_required()
def get_project_by_id(id):
    response, status = ProjectService.get_project_by_id(id)
    return jsonify(response), status

@project_route.route("/projetos", methods=['GET'])
# @jwt_required()
def get_all_projects():
    response, status = ProjectService.get_all_projects()
    return jsonify(response), status

@project_route.route("/projeto/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_project_by_id(id):
    response, status = ProjectService.delete_project_by_id(id)
    return jsonify(response), status

