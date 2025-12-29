from sqlalchemy import Column,String,Integer,Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Simbolos(Base):
    __tablename__ = "simbolos"
    id = Column(Integer,primary_key=True, autoincrement=True)
    simbolo = Column(String,nullable=True)
    valor_limite = Column(Float,nullable=True)

    def __init__(self,simbolo,valor_limite):
        self.simbolo = simbolo
        self.valor_limite= valor_limite
       