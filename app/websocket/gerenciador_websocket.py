from fastapi import WebSocket

class gerenciador_conexao:
    def __init__(self):
        self.usuarios_activos = []

    async def conectar(self,ws:WebSocket):
        ws.accept()    