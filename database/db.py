from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLACHEMY_URL = 'mysql+pymysql://root:localhost:3306/proygit'

engine = create_engine(SQLACHEMY_URL)

SessionLocal = sessionmaker(engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()