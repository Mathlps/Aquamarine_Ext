from db_model import Animal
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
    def update_animal(id, data):
        animal = Animal.query.get(id)

        if not animal:
            return {"error": "Animal não encontrado"}, 404

        animal.nome = data.get('nome', animal.nome)
        animal.especie = data.get('especie', animal.especie)
        animal.porte = data.get('porte', animal.porte)
        animal.status = data.get('status', animal.status)
        db.session.commit()

        return {"message": "Animal atualizado com sucesso"}, 200

    @staticmethod
    def remove_animal(id):
        animal = Animal.query.get(id)

        if not animal:
            return {"error": "Animal não encontrado"}, 404

        db.session.delete(animal)
        db.session.commit()

        return {"message": "Animal excluído com sucesso"}, 200
        
