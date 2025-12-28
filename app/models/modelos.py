from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome_usuario = Column(String, index=True)
    email = Column(String,)
    senha = Column(String)
    admin = Column(Boolean, default=False)
