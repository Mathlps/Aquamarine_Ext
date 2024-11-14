from flask  import flask, jsonify, request, make_response
# from news_service import 

@app.route("/noticias", method= ['POST'])
def create_news():
    return jsonify(message="Noticia criada com sucesso")


