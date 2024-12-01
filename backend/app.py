import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from flask_migrate import Migrate
from db_config import Dev,Prod
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    
    CORS(app)
    
    # Configuração do ambiente
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(Prod)
    else:
        app.config.from_object(Dev)

    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)

    with app.app_context():
        from db_model import Administrador, Projeto, Animal, Noticia
        from routes.project_route import project_route
        from routes.news_route import news_route
        from routes.animal_route import animal_route
        from routes.adm_route import adm_route
        app.register_blueprint(project_route)
        app.register_blueprint(news_route)
        app.register_blueprint(animal_route)
        app.register_blueprint(adm_route)

    return app

app = create_app()

# @app.route("/login")
# def home():
#     return "<h1>Efetuar Login</h1>"


if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])