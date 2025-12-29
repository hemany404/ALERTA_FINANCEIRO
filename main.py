from fastapi import FastAPI,Depends
import asyncio
from app.services.alerta_risco import risco_loop
from  fastapi import WebSocket,WebSocketDisconnect
from app.websocket.gerenciador_websocket import gerenciador


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

app.post("/adicionar_simbolo")

@app.on_event("startup")
async def iniciar_loop():
    asyncio.create_task(risco_loop())
  