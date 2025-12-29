from app.api_financeira import buscar_preco
from app.websocket.gerenciador_websocket import gerenciador
import asyncio
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import session
from app.model.modelo import Simbolos
from app.core.database import pegar_bd

Session = Annotated[session, Depends(pegar_bd)]


simbolo = Session.query(si)

async def risco_loop():
    while True:
        for simbolo,valor in RISCO.items():
            try:
                preco = await buscar_preco(simbolo)
                if preco and valor > preco:
                    await gerenciador.broadcast(f"☢️❌ {simbolo} abaixo de {valor}! ({preco})")
                    print("mensagem enviada")
            except Exception as e:
                print("Erro no monitoramento:", e)        

            await asyncio.sleep(1)