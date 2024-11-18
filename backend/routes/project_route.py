from flask import Flask, jsonify, request, Blueprint
# from app import app, db
# from jwt import 
from service.project_service import ProjectService

project_route = Blueprint("project", __name__)

@project_route.route("/projects", methods=['POST'])
# @jwt_required
def create_project():
    data = request.json
    # idAdmin = get_jwt_identity()
    return jsonify(*ProjectService.create_project(data))

@project_route.route("/projects/<int:id>", methods=['PUT'])
# @jwt_required
def update_project_by_id(id):
    data = request.json
    return jsonify(*ProjectService.update_project(data, id))

@project_route.route("/projects/<int:id>", methods=['GET'])
# @jwt_required
def get_project_by_id(id):
    return jsonify(*ProjectService.get_project_by_id(id))

@project_route.route("/projects", methods=['GET'])
# @jwt_required
def get_all_projects():
    return jsonify(*ProjectService.get_all_projects())

@project_route.route("/projects/<int:id>", methods=['DELETE'])
# @jwt_required
def delete_project_by_id(id):
    return jsonify(*ProjectService.delete_project_by_id(id))

