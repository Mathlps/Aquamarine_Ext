from flask import flask, jsonify, request, make_response
# from service_project import 

@app.route("/projects", methods=['POST'])
# @jwt_required
    def create_project():
        return jsonify(message="Projeto criado com sucesso"), 201
@app.route("/projects/<int:id>", methods=['PUT'])
    def update_project_by_id():
        return jsonify(message="Projeto atualizado com sucesso"), 200
@app.route("/projects/<int:id>", methods=['GET'])
    def get_project_by_id():
        return jsonify(message="Projeto recuperado com sucesso"), 200
@app.route("/projects", methods=['GET'])
    def get_all_projects():
        return jsonify(message="Projetos recuperados com sucesso"), 200
@app.route("/projects/<int:id>", methods=['DELETE'])
    def delete_project_by_id():
        return jsonify(message="Projeto excluído com sucesso"), 200

