from flask import Flask

app =  Flask(__name__)

@app.route("/projeto/<int:id>", methods= ['GET'])
def get_project_by_id(id):
        return "<h1>PROJETO TAL</h1>"

@app.route("/noticia/<int:id>", methods= ['GET'])
def get_news_by_id(id):
    return "<h1>NOTICIA TAL</h1>"

if __name__ == "__main__":
    app.run(debug=True)