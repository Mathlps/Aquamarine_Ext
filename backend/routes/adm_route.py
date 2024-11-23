from flask import Flask, request, jsonify, Blueprint
from service.adm_service import AdmService

adm_route = Blueprint("adm", __name__)

@adm_route.route("/adm", methods=['GET'])
def get_adm():
    response = AdmService.get_adm_info()
    return jsonify(response)

@adm_route.route("/login", methods=['POST'])
def login():
    print("Rota Login")
    credenciais = request.json
    response, status = AdmService.validate_credentials(credenciais)
    return jsonify(response), status

@adm_route.route("/adm/password", methods=['PUT'])
def update_password():
    credenciais = request.json
    response, status = AdmService.update_password(credenciais)
    print(response, status)
    return jsonify(response), status


