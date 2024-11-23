from flask  import Flask, jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from service.news_service import NewsService

news_route = Blueprint("news", __name__)

@news_route.route("/noticias", methods= ['POST'])
@jwt_required()
def create_news():
    data = request.json
    response,status = NewsService.create_news(data)
    return jsonify(response), status

@news_route.route("/noticias", methods= ['PUT'])
@jwt_required()
def update_news(id):
    data = request.json
    response,status = NewsService.update_news(data, id)
    return jsonify(response), status

@news_route.route("/noticias", methods= ['GET'])
def get_news_by_id(id):
    response,status = NewsService.get_news_by_id(id)
    return jsonify(response), status

@news_route.route("/noticias", methods= ['GET'])
def get_all_news():
    response,status = NewsService.get_all_news()
    return jsonify(response), status

@news_route.route("/noticias", methods= ['DELETE'])
@jwt_required()
def delete_news(id):
    response,status = NewsService.delete_news(id)
    return jsonify(response), status



