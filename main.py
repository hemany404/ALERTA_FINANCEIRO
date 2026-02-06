from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import session
from  fastapi import WebSocket,WebSocketDisconnect


import asyncio

from app.services.alerta_risco import risco_loop
from app.websocket.gerenciador_websocket import gerenciador
from app.model.modelo import Simbolos
from app.schema.schema import SimbolosSchema
from app.core.database import pegar_bd 



app = FastAPI()


@app.websocket("/ws")
async def endpoint_websocket(ws:WebSocket):
        await gerenciador.conectar(ws)

        try: 
            while True:
                data = await ws.receive_text()
                await gerenciador.broadcast(data)

        except WebSocketDisconnect:
            gerenciador.desconectar(ws)        

@app.post("/teste_do_broadcast")
async def enviar_msg(msg:str):
     await gerenciador.broadcast(msg)
     return {"mensagem enviada"}

@app.post("/adicionar_simbolo")
async def adicioanar_simbolo(
            simbolo_schema:SimbolosSchema,
            session: session = Depends(pegar_bd)):
     simbolo =session.query(Simbolos).filter(Simbolos.simbolo ==  simbolo_schema.simbolo).first()
     
     if  simbolo:
          raise HTTPException(status_code=401,detail=" Este simbolo já foi adicionado")
     
     novo_simbolo = Simbolos(simbolo_schema.simbolo,simbolo_schema.valor_limite )
     session.add(novo_simbolo)
     session.commit()

     return {
          "mensagem":"simbolo adicionado com sucesso"
     }
          
     

@app.on_event("startup")
async def iniciar_loop():
    
    asyncio.create_task(risco_loop())
      

  