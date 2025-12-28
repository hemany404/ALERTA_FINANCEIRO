from fastapi import Depends, HTTPException
from fastapi.security import  OAuth2PasswordRequestForm
from jose import jwt
from app.main import oauth2_schema,SECRETY_KEY,ALGORITHM,ACESS_TOKEN_MINUTO_EXPIRACAO,bcrypt_context
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
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        return False
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False
    return usuario

async def pegar_usuario(token: str =Depends(oauth2_schema)) 