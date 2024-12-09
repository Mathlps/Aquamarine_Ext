import os
from dotenv import load_dotenv, find_dotenv

# Carregar o arquivo .env
load_dotenv(find_dotenv(".env"))

print("Variáveis carregadas:")
# for key, value in os.environ.items():
#     if key.startswith("DEV_") or key.startswith("PROD_") or key in ["JWT_SECRET_KEY", "FLASK_ENV"]:
#         print(f"{key}: {value}")
print(f"Ambiente Flask: {os.environ.get('FLASK_ENV')}")


class Config:
    SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "chave_secreta_padrao")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

class Dev(Config):
    DEBUG = True 
    try:
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+pymysql://{os.environ['DEV_DB_USERNAME']}:{os.environ['DEV_DB_PASSWORD']}"
            f"@{os.environ['DEV_DB_HOST']}:{os.environ['DEV_DB_PORT']}/{os.environ['DEV_DB_NAME']}"
        )
    except KeyError as e:
        raise RuntimeError(f"Faltando variável de ambiente necessária: {e}")

class Prod(Config):
    try:
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+pymysql://{os.environ['PROD_DB_USERNAME']}:{os.environ['PROD_DB_PASSWORD']}"
            f"@{os.environ['PROD_DB_HOST']}:{os.environ['PROD_DB_PORT']}/{os.environ['PROD_DB_NAME']}"
        )
        DEBUG = False
    except KeyError as e:
        raise RuntimeError(f"Faltando variável de ambiente necessária: {e}")
