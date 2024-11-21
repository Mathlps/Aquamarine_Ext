import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from db_config import Dev,Prod

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    
    # Configuração do ambiente
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(Prod)
    else:
        app.config.from_object(Dev)

    db.init_app(app)
    migrate.init_app(app,db)

    with app.app_context():
        from db_model import Administrador, Projeto, Animal, Noticia
        from routes.project_route import project_route
        from routes.news_route import news_route
        from routes.animal_route import animal_route
        app.register_blueprint(project_route)
        app.register_blueprint(news_route)
        app.register_blueprint(animal_route)

    return app

app = create_app()

# @app.route("/login")
# def home():
#     return "<h1>Efetuar Login</h1>"


if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])