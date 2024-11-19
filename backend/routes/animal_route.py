from Flask import flask, required, jsonify, Blueprint
from service.animal_service import AnimalService

animal_route = Blueprint("animal",__name__)

@animal_route.route("/animal", methods=['POST'])
def register_animal():
    data = request.json
    response, status = AnimalService.register_animal(data)
    return jsonify(response), status

@animal_route.route("/animal/<int:id>", methods=['GET'])
def get_animal_by_id(id)

@animal_route.route("/animal/<int:idProject>", methods=['GET'])
def get_animals_from_project(id_project)

@animal_route.route("/animal/<int:id>", methods=['GET'])
def get_animal_by_id(id)