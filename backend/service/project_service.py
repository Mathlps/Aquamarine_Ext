from db_model import Projeto
from flask_jwt_extended import get_jwt_identity 
from extensions import db
class ProjectService:

    @staticmethod
    def create_project(data):
        print("Dentro do Service")
        new_project = Projeto(
            titulo=data['titulo'],
            data_inicio=data['data_inicio'],
            data_fim=data['data_fim'],
            status=data['status'],
            texto = data['texto'],
            id_adm = get_jwt_identity()
        )

        print(new_project)

        db.session.add(new_project)
        db.session.commit()
        return {"message": "Projeto criado com sucesso!"}, 201

    @staticmethod
    def update_project(data, id):
        projeto = Projeto.query.get(id)
        if not projeto:
            return {"error": "Projeto não encontrado"}, 404

        for key, value in data.items():
            if hasattr(projeto, key) and value not in [None, ""]:  # Verifica se o atributo existe no modelo
                setattr(projeto, key, value)  # Atualiza o atributo dinamicamente

        try:
            db.session.commit()
            return {"message": "Projeto atualizado com sucesso!"}, 200
        except Exception as e:
            db.session.rollback()
            return {"error": f"Erro ao atualizar projeto: {str(e)}"}, 500
    
    @staticmethod
    def get_project_by_id(id):
        project = Projeto.query.get(id)
        if not project:
            return {"error": "Projeto não encontrado"}, 404

        return {
            "id": project.id_projeto,
            "titulo": project.titulo,
            "data_inicio": project.data_inicio.strftime('%Y-%m-%d') if project.data_inicio else None,
            "data_fim": project.data_fim.strftime('%Y-%m-%d') if project.data_fim else None,
            "status": project.status,
            "texto": project.texto
        }, 200

    @staticmethod
    def get_all_projects():
        projects = Projeto.query.all()
        return [{
            "id": project.id_projeto,
            "titulo": project.titulo,
            "data_inicio": project.data_inicio.strftime('%Y-%m-%d') if project.data_inicio else None,
            "data_fim": project.data_fim.strftime('%Y-%m-%d') if project.data_fim else None,
            "status": project.status,
            "texto": project.texto

        } for project in projects], 200
    
    @staticmethod
    def delete_project_by_id(id):
        project = Projeto.query.get(id)
        if not project:
            return {"error": "Projeto não encontrado"}, 404

        db.session.delete(project)
        db.session.commit()
        return {"message": "Projeto excluído com sucesso!"}, 200



