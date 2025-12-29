from pydantic import BaseModel

class SimbolosSchema(BaseModel):
    simbolo: str
    valor_limite:float

    class config:
        from_attributes = True
