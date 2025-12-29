import httpx

async def buscar_preco(simbolo: str) -> float:
    async with httpx.AsyncClient() as cliente:
        resposta = await cliente.get(
            "https://api.binance.com/api/v3/ticker/price",
            params={"symbol": simbolo}
        )

        dados = resposta.json()

        if "price" not in dados:
            raise ValueError(f"Erro da API: {dados}")

        return float(dados["price"])
