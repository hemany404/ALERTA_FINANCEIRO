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



app = FastAPI()


bcrypt_context = CryptContext(schemes=["bcrypt"],deprecated= "auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")


@app.websocket("/ws")
async def ws_rota(ws):
    await endpoint_websocket(ws)

@app.on_event("startup")
async def iniciar_loop():
    asyncio.create_task(risco_loop)

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends(), session: session = Depends(pegar_db)):
    usuario = autenticar_usuario(form.username, form.password, session)
    if not usuario:
        return False
    return {"access_token": criar_token(usuario.id),
             "token_type": "bearer"
    }    