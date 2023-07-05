from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db, engine
from models import models
from schemas import schemas
from crud import crud

models.Base.metadata.create_all(engine)

padron = APIRouter()

@padron.get('/countries', response_model=schemas.Country)
def get_padron(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_padron(skip, limit, db)

