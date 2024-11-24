from flask_sqlalchemy import SQLAlchemy
from extensions import db


class Administrador(db.Model):
    __tablename__ = 'Administrador'

    id_adm = db.Column('IdAdm', db.Integer, primary_key=True, nullable=False)
    nome = db.Column('Nome', db.String(45), nullable=True)
    email = db.Column('Email', db.String(45), nullable=True)
    cpf = db.Column('CPF', db.String(15), nullable=True)
    senha = db.Column('Senha', db.String(255), nullable=True)

    projetos = db.relationship('Projeto', backref='administrador', lazy=True)
    animais = db.relationship('Animal', backref='administrador', lazy=True)
    noticias = db.relationship('Noticia', backref='administrador', lazy=True)

class Projeto(db.Model):
    __tablename__ = 'Projeto'

    id_projeto = db.Column('IdProjeto', db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column('Titulo', db.String(45), nullable=True)
    data_inicio = db.Column('Data_inicio', db.Date, nullable=True)
    data_fim = db.Column('Data_fim', db.Date, nullable=True)
    status = db.Column('pStatus', db.String(45), nullable=True)
    texto = db.Column('Texto', db.Text, nullable=True)
    id_adm = db.Column('IdAdm', db.Integer, db.ForeignKey('Administrador.IdAdm'), nullable=False)

    animais = db.relationship('Animal', backref='projeto', lazy=True)

class Animal(db.Model):
    __tablename__ = 'Animal'

    id_animal = db.Column('IdAnimal', db.Integer, primary_key=True, autoincrement=True)
    status = db.Column('aStatus', db.String(45), nullable=True)
    nome = db.Column('Nome', db.String(45), nullable=True)
    especie = db.Column('Especie', db.String(45), nullable=True)
    porte = db.Column('Porte', db.String(45), nullable=True)
    id_projeto = db.Column('IdProjeto', db.Integer, db.ForeignKey('Projeto.IdProjeto'), nullable=True)
    id_adm = db.Column('IdAdm', db.Integer, db.ForeignKey('Administrador.IdAdm'), nullable=False)

class Noticia(db.Model):
    __tablename__ = 'Noticia'

    id_noticia = db.Column('IdNoticia', db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column('Titulo', db.String(45), nullable=True)
    data_publicacao = db.Column('Data_publicacao', db.Date, nullable=True)
    texto = db.Column('Texto', db.Text, nullable=True)
    id_adm = db.Column('IdAdm', db.Integer, db.ForeignKey('Administrador.IdAdm'), nullable=False)
