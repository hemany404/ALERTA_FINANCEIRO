from fastapi import FastAPI,Depends
from passlib.context import CryptContext
from dotenv import load_dotenv
import asyncio

from app.services.alerta_risco import risco_loop
from app.auth.auth import autenticar_usuario,criar_token
from app.core.database import pegar_db
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import session
import os
from  fastapi import WebSocket,WebSocketDisconnect,APIRouter
from app.websocket.gerenciador_websocket import gerenciador_conexao
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bcrypt_context = CryptContext(schemes=["bcrypt"],deprecated= "auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

gerenciador = gerenciador_conexao()

@app.websocket("/ws")
async def endpoint_websocket(ws:WebSocket):
        await gerenciador.conectar(ws)

        try: 
            while True:
                data = await ws.receive_text()
                await gerenciador.broadcast(data)

        except WebSocketDisconnect:
            gerenciador.desconectar(ws)        

@app.on_event("startup")
async def iniciar_loop():
    asyncio.create_task(risco_loop())
  