from flask import Flask, jsonify, request, Blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity 
from service.project_service import ProjectService

project_route = Blueprint("project", __name__)

@project_route.route("/projects", methods=['POST'])
@jwt_required
def create_project():
    data = request.json
    response, status = ProjectService.create_project(data)
    return jsonify(response), status
    
@project_route.route("/projects/<int:id>", methods=['PUT'])
# @jwt_required
def update_project_by_id(id):
    data = request.json
    response, status = ProjectService.update_project(data, id)
    return jsonify(response), status

@project_route.route("/projects/<int:id>", methods=['GET'])
# @jwt_required
def get_project_by_id(id):
    response, status = ProjectService.get_project_by_id(id)
    return jsonify(response), status

@project_route.route("/projects", methods=['GET'])
# @jwt_required
def get_all_projects():
    response, status = ProjectService.get_all_projects()
    return jsonify(response), status

@project_route.route("/projects/<int:id>", methods=['DELETE'])
# @jwt_required
def delete_project_by_id(id):
    response, status = ProjectService.delete_project_by_id(id)
    return jsonify(response), status

