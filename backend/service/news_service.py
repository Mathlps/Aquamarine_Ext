class NewsService:

    @staticmethod
    def create_news(data):
        title = data['titulo'],
        createdAt = data['data_publicacao'],
        news_text = data['texto']
        return {"message":"Notícia Criada"}, 201

    @staticmethod
    def update_news(data, id):
        title = data['titulo'],
        createdAt = data['data_publicacao'],
        news_text = data['texto']
        return {"message":"Notícia Atualizada"},200

    @staticmethod
    def get_news_by_id(id):

        return {"message":"Notícia Recuperada"},200

    @staticmethod
    def get_all_news(id):

        return {"message":"Todas as Notícias Recuperadas"},200

    @staticmethod
    def delete_news(id):

        return {"message":"Notícia Excluída"},200