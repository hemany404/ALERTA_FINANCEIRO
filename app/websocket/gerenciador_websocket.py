from fastapi import WebSocket

class gerenciador_conexao:
    def __init__(self):
        self.usuarios_activos = []

    async def conectar(self,ws:WebSocket):
        await ws.accept()
        self.usuarios_activos.append(ws)
        print(len(self.usuarios_activos))

    def desconectar(self,ws:WebSocket):
        self.usuarios_activos.remove(ws)

    async def broadcast(self,mensagem:str):
        for conectado in self.usuarios_activos:
            await conectado.send_text(mensagem)
            print(len(self.usuarios_activos))
            
gerenciador = gerenciador_conexao()           