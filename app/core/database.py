from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///meu_banco.bd")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def pegar_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()