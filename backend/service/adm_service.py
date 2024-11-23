from db_model import Administrador
from werkzeug.security import check_password_hash,generate_password_hash
from flask_jwt_extended import create_access_token
from extensions import db
class AdmService:

    @staticmethod
    def get_adm_info():
        return {"message",adm}, 200
        
    @staticmethod
    def validate_credentials(credenciais):
        email = credenciais['email']
        password= credenciais['senha']
        adm = Administrador.query.filter_by(email=email).first()

        if not adm or not check_password_hash(adm.senha,password):
            return {"error": "Verifique suas credenciais novamente"}, 404
        
        access_token = create_access_token(identity=adm.id_adm)
        return {"token": access_token}, 200

    @staticmethod
    def update_password(credenciais):
        email = credenciais['email']
        password= credenciais['senha']

        adm = Administrador.query.filter_by(email=email).first()
        if not adm:
            return {"error": "Verifique suas credenciais novamente"}, 404
        
        novaSenha = generate_password_hash(password, method='pbkdf2:sha256')
        adm.senha = novaSenha


        db.session.commit()
        return {"message": "Senha Atualizada com Sucesso"}, 200