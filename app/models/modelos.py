from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome_usuario = Column(String,nullable=False, index=True)
    email = Column(String,unique=True,nullable=False,index=True)
    senha = Column(String,nullable=False)
    admin = Column(Boolean, default=False)
