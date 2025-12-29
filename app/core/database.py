from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker

bd = create_engine("sqlite:///meu_banco.db")
sessao_local = sessionmaker(autocomit =False, autoflush= False, bind=bd)

def pegar_bd():
    bd = sessao_local()
    try:
        yield bd
    finally:
        bd.close    