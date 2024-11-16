import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave_secreta_padrao'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Dev(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql123@localhost/aquamarine'
    DEBUG = True

class Prod(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # configurar na hospedagem com a variável deles
    DEBUG = False
