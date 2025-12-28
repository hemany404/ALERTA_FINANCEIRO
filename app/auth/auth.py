from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from app.main import SECRETY_KEY,ALGORITHM,ACESS_TOKEN_MINUTO_EXPIRACAO
from sqlalchemy.orm import Session
from app.models.modelos import Usuario
from app.core.database import pegar_db
from datetime import timedelta, timezone, datetime

def criar_token(id_usuario: int, duracao_token = timedelta(minutes=ACESS_TOKEN_MINUTO_EXPIRACAO)):
    data_expircao = datetime.now(timezone.utc) + duracao_token
    dic_info = {"sub":str(id_usuario), "expiracao": str(data_expircao)}
    jwt_codificado = jwt.encode(dic_info,SECRETY_KEY,ALGORITHM)
    return jwt_codificado

def autenticar_usuario(email,senha,session):
    instituicao = session.query(Usuario).filter(Instituicao.email == email).first()
    if not instituicao:
        return False
    elif not bcrypt_context.verify(senha,instituicao.senha):
        return False
    return instituicao
