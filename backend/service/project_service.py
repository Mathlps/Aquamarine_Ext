class ProjectService:

    @staticmethod
    def create_project(data):
        title = data['titulo'],
        startsAt = data['data_inicio'],
        endsAt = data['data_fim'],
        status = data['status']

        return {"message": "Projeto criado com sucesso!"}, 201

    @staticmethod
    def update_project(data, id):
        title = data['titulo'],
        startsAt = data['data_inicio'],
        endsAt = data['data_fim'],
        status = data['status']

        return {"message":"Projeto atualizado com sucesso"}, 200
    
    @staticmethod
    def get_project_by_id(id):
        return{"message":"Projeto recuperado com sucesso"}, 200

    @staticmethod
    def get_all_projects():
        return {"message":"Projetos recuperados com sucesso"}, 200
    
    @staticmethod
    def delete_project_by_id(id):
        return {"message" : "Projeto excluído com sucesso"}, 200



