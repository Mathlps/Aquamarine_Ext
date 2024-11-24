from db_model import Animal, Projeto
from flask_jwt_extended import get_jwt_identity 
from extensions import db
class AnimalService:

    @staticmethod
    def register_animal(data):
        new_animal = Animal(
            nome=data['nome'],
            especie=data['especie'],
            porte=data['porte'],
            status=data['status'],
            id_adm = get_jwt_identity()
        )

        db.session.add(new_animal)
        db.session.commit()
        return {"message": "Animal Registrado com Sucesso"}, 201
    
    @staticmethod
    def update_animal_register(data, id):
        animal = Animal.query.get(id)

        if not animal:
            return {"error": "Animal não encontrado"}, 404
        
        animal.nome= data['nome'],
        animal.especie= data['especie'],
        animal.porte= data['porte'],
        animal.status= data['status']

        db.session.commit()
        return {"message": "Registro de Animal atualizado com Sucesso!"}, 200


    @staticmethod
    def get_animal_by_id(id):
        animal = Animal.query.get(id)

        if not animal:
            return {"error": "Animal não encontrado"}, 404

        return {
            "id": animal.id_animal,
            "nome": animal.nome,
            "especie": animal.especie,
            "porte": animal.porte,
            "status": animal.status,
            "id_projeto": animal.id_projeto
        }, 200

    @staticmethod
    def list_all_animals():
        animals = Animal.query.all()

        if not animals:
            return {"error": "Nenhum animal encontrado"}, 404

        return [{
            "id": animal.id_animal,
            "nome": animal.nome,
            "especie": animal.especie,
            "porte": animal.porte,
            "status": animal.status,
            "id_projeto": animal.id_projeto
        } for animal in animals], 200
    
    @staticmethod
    def get_animals_from_project(id_project):
        animals = Animal.query.filter_by(id_projeto=id_project).all()

        if not animals:
            return {"error": "Nenhum animal encontrado para este projeto"}, 404

        return [{
            "id": animal.id_animal,
            "nome": animal.nome,
            "especie": animal.especie,
            "porte": animal.porte,
            "status": animal.status,
            "id_projeto": animal.id_projeto
        } for animal in animals], 200


    @staticmethod
    def delete_animal(id):
        animal = Animal.query.get(id)

        if not animal:
            return {"error": "Animal não encontrado"}, 404

        db.session.delete(animal)
        db.session.commit()

        return {"message": "Animal excluído com sucesso"}, 200


    @staticmethod
    def link_animal_to_project(id, id_project):
        animal = Animal.query.get(id)
        projeto = Projeto.query.get(id_project)

        if not animal:
            return {"error": "Animal não encontrado"}, 404
        elif not projeto:
            return{"error": "Projeto não encontrado"}, 404

        animal.id_projeto = id_project
        db.session.commit()

        return {"message": "Animal vinculado ao projeto com sucesso!"}, 200

    @staticmethod
    def unlink_animal_from_project(id):
        animal = Animal.query.get(id)

        if not animal:
            return {"error": "Animal não encontrado"}, 404

        if not animal.id_projeto:
            return {"error": "Animal não está vinculado a nenhum projeto"}, 400

        animal.id_projeto = None
        db.session.commit()

        return {"message": "Animal desvinculado do projeto com sucesso!"}, 200       
