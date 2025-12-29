from sqlalchemy import Column,String,Integer,Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Simbolos(Base):
    __tablename__ = "simbolos"
    id = Column(Integer,)