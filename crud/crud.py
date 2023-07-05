from models import models
from sqlalchemy.orm import Session

def get_padron(db: Session, skip: int, limit: int):
    return db.query(models.Padron).offset(skip).limit(limit).all()
