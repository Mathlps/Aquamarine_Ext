from db_model import Noticia
from flask_jwt_extended import get_jwt_identity 
from extensions import db
class NewsService:

    @staticmethod
    def create_news(data):
        new_news = Noticia(
            titulo=data['titulo'],
            data_publicacao=data['data_publicacao'],
            texto=data['texto'],
            id_adm  = get_jwt_identity()
        )
        db.session.add(new_news)
        db.session.commit()
        return {"message":"Notícia Criada"}, 201

    @staticmethod
    def update_news(data, id):
        noticia = Noticia.query.get(id)

        if not noticia:
            return {"error": "Nenhuma Notícia com este ID foi encontrada"}, 404
        
        noticia.titulo = data.get('titulo', noticia.titulo)
        noticia.data_publicacao = data.get('data_publicacao', noticia.data_publicacao)
        noticia.texto = data.get('texto', noticia.texto)

        db.session.commit()
        return {"message":"Notícia Atualizada"},200

    @staticmethod
    def get_news_by_id(id):
        noticia = Noticia.query.get(id)
        if not noticia:
            return {"error": "Notícia não encontrada"}, 404

        return {
            "titulo": noticia.titulo,
            "data_publicacao": noticia.data_publicacao,
            "texto": noticia.texto,
            "id_adm": noticia.id_adm
        }, 200

    @staticmethod
    def get_all_news():
        noticias = Noticia.query.all()
        return [{
            "titulo": noticia.titulo,
            "data_publicacao": noticia.data_publicacao,
            "texto": noticia.texto,
            "id_adm": noticia.id_adm
        } for noticia in noticias], 200

    @staticmethod
    def delete_news(id):
        noticia = Noticia.query.get(id)

        if not noticia:
            return {"error": "Notícia não encontrada"}, 404 
        
        db.session.delete(noticia)
        db.session.commit()
        return {"message":"Notícia Excluída"},200