from app.api_financeira import buscar_preco
from app.routes.rotas import gerenciador
import asyncio

RISCO ={
    "bitcoin":100000,
    "ethereum":3000
}

async def risco_loop():
    while True:
        for simbolo,valor in RISCO.items():
            preco = await buscar_preco(simbolo)
            if preco and preco < valor:
                await gerenciador.broadcast(f"⚠ {simbolo} abaixo de {valor}! ({preco})")
            await asyncio.sleep(2)