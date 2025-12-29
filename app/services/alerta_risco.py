from fastapi import Depends,HTTPException
from app.api_financeira import buscar_preco
from app.websocket.gerenciador_websocket import gerenciador
import asyncio
from typing import Annotated
from sqlalchemy.orm import session
from app.model.modelo import Simbolos
from app.core.database import pegar_bd




async def risco_loop():
    Session:session= next(pegar_bd())
    simbolos = Session.query(Simbolos).all()
    simbolo_dict = {s.simbolo: s.valor_limite for s in simbolos}
    while True:
        for simbolo,valor in simbolo_dict.items():
            try:
                preco = await buscar_preco(simbolo)
                if preco and valor > preco:
                    await gerenciador.broadcast(f"☢️❌ {simbolo} abaixo de {valor}! preçco actual({preco})")
                    print("mensagem enviada")
            except Exception as e:
                print("Erro no monitoramento:", e)        

            await asyncio.sleep(20)