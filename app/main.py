from fastapi import FastAPI,Depends
from passlib.context import CryptContext
from dotenv import load_dotenv
import asyncio
from app.routes.rotas import endpoint_websocket
from app.services.alerta_risco import risco_loop
from app.auth.auth import autenticar_usuario,criar_token
from app.core.database import pegar_db
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import session
import os
from fastapi.security import OAuth2PasswordBearer


load_dotenv()
SECRETY_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACESS_TOKEN_MINUTO_EXPIRACAO = int(os.getenv("ACESS_TOKEN_MINUTO_EXPIRACAO"))

app = FastAPI()


bcrypt_context = CryptContext(schemes=["bcrypt"],deprecated= "auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")


@app.websocket("/ws")
async def ws_rota(ws):
    await endpoint_websocket(ws)

@app.on_event("iniciar")
async def iniciar_loop():
    asyncio.create_task(risco_loop)

@app.post("/token")
async def token(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate(form.username, form.password, db)
    if not user:
        return {"error": "invalid"}
    return {"access_token": create_token(user), "token_type": "bearer"}    