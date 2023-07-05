from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models import models
from crud import crud


padron = APIRouter()

@padron.get('/padron')
def get_padron(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_padron(skip, limit, db)