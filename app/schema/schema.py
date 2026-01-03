from pydantic import BaseModel
from fastapi import Path

class SimbolosSchema(BaseModel):
    simbolo: str = Path(...,regex="^[A-Z]{3,10}$")
    valor_limite:float

    class config:
        from_attributes = True
