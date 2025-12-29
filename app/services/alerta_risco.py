from app.api_financeira import buscar_preco
from app.routes.rotas import gerenciador
import asyncio

RISCO ={
    "BTCUSDT":100000,
    "ETHUSDT":3000
}

async def risco_loop():
    while True:
        for simbolo,valor in RISCO.items():
            try:
                preco = await buscar_preco(simbolo)
                if preco and preco < valor:
                    await gerenciador.broadcast(f"⚠ {simbolo} abaixo de {valor}! ({preco})")
            except Exception as e:
                print("Erro no monitoramento:", e)        

            await asyncio.sleep(10)