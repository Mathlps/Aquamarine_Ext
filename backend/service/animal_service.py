class AnimalService:

    @staticmethod
    def register_animal(data):
        name = data['nome']
        species = data['especie']
        size = data['porte']
        status = data['status']

        return {"message": "Animal Registrado com Sucesso"}, 201

    @staticmethod
    def get_animal_by_id(id):

        return {}
    
    @staticmethod
    def get_animals_from_project(id_project):

        return{}

    @staticmethod
    def get_animal_by_id(id):

        return{}
        
