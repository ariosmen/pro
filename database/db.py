from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLACHEMY_URL = 'mysql+pymysql://root:@localhost:3306/proygit'
SQLACHEMY_URL = 'sqlite:///./proygit.db'

engine = create_engine(SQLACHEMY_URL, connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()