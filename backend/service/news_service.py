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
            link_imagem = data['link_imagem'],
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
        
        for key, value in data.items():
            if hasattr(noticia, key) and value not in [None, ""]:  # Verifica se o atributo existe no modelo
                setattr(noticia, key, value)  # Atualiza o atributo dinamicamente

        try:
            db.session.commit()
            return {"message": "Noticia atualizada com sucesso!"}, 200
        except Exception as e:
            db.session.rollback()
            return {"error": f"Erro ao atualizar noticia: {str(e)}"}, 500

    @staticmethod
    def get_news_by_id(id):
        noticia = Noticia.query.get(id)
        if not noticia:
            return {"error": "Notícia não encontrada"}, 404

        return {
            "titulo": noticia.titulo,
            "data_publicacao": noticia.data_publicacao,
            "texto": noticia.texto,
            "id_adm": noticia.id_adm,
            "link_imagem": noticia.link_imagem,
            "link_noticia": noticia.link_noticia
            
        }, 200

    @staticmethod
    def get_all_news():
        noticias = Noticia.query.all()
        return [{
            "titulo": noticia.titulo,
            "data_publicacao": noticia.data_publicacao,
            "texto": noticia.texto,
            "id_adm": noticia.id_adm,
            "link_imagem": noticia.link_imagem,
            "link_noticia": noticia.link_noticia

        } for noticia in noticias], 200

    @staticmethod
    def delete_news(id):
        noticia = Noticia.query.get(id)

        if not noticia:
            return {"error": "Notícia não encontrada"}, 404 
        
        db.session.delete(noticia)
        db.session.commit()
        return {"message":"Notícia Excluída"},200