from app.api_financeira import buscar_preco
from app.websocket.gerenciador_websocket import gerenciador
import asyncio
from sqlalchemy.orm import 
from app.core.database import pegar_bd






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