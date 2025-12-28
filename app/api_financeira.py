import httpx

async def buscar_preco(simbolo:str):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={simbolo}&vs_currencies=usd"
        async with httpx.AsyncClient as cliente:
                r = await cliente.get(url)
                data = r.json()
                return data.get(simbolo, {}).get("usd")
