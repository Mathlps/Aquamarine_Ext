from flask  import Flask, jsonify, request, Blueprint
# from news_service import 

news_route = Blueprint("news", __name__)

@news_route.route("/noticias", methods= ['POST'])
def create_news():
    return jsonify(message="Noticia criada com sucesso")


