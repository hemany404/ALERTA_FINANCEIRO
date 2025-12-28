from  fastapi import WebSocket,WebSocketDisconnect
from app.websocket.gerenciador_websocket import gerenciador_conexao

gerenciador = gerenciador_conexao()


async def endpoint_websocket(ws:WebSocket):
    await gerenciador.conectar(ws)

    try: 
        while True:
            data = await ws.receive_text()
            await gerenciador.broadcast(data)
    except WebSocketDisconnect:
        gerenciador.desconectar(ws)        