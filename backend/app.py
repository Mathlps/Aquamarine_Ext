import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db_config import Dev,Prod

db = SQLAlchemy()
app =  Flask(__name__)

if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object(Prod)
else:
    app.config.from_object(Dev)

# db = SQLAlchemy(app)

@app.route("/projeto/<int:id>", methods= ['GET'])
def get_project_by_id(id):
        return "<h1>PROJETO TAL</h1>"

@app.route("/noticia/<int:id>", methods= ['GET'])
def get_news_by_id(id):
    return "<h1>NOTICIA TAL</h1>"

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])