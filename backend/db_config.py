import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv(".env.local"))

# import os
# print("Variáveis carregadas:")
# for key, value in os.environ.items():
#     if key.startswith("DB_") or key == "JWT_SECRET_KEY" or key == "FLASK_ENV":
#         print(f"{key}: {value}")


class Config:
    SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'chave_secreta_padrao'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Dev(Config):
    try:
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+pymysql://{os.environ['DB_USERNAME']}:{os.environ['DB_PASSWORD']}"
            f"@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
        )
    except KeyError as e:
        raise RuntimeError(f"Faltando variável de ambiente necessária: {e}")
        
class Prod(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # configurar na hospedagem com a variável deles
    DEBUG = False
