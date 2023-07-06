from models import models
from schemas import schemas
from sqlalchemy.orm import Session


def get_code_country(db: Session, country: int):
    return db.query(models.Country).filter(models.Country.code_country == country).first()

def get_countries(db: Session, skip: int, limit: int):
    return db.query(models.Country).offset(skip).limit(limit).all()

def create_country(db: Session, country: schemas.CountryCreate):
    new_country = models.Country(**country.dict())
    db.add(new_country)
    db.commit()
    db.refresh(new_country)
    return new_country

def get_code_province(db: Session, code_province: int):
    return db.query(models.Province).filter(models.Province.code_province == code_province).first()

def get_provinces(db: Session, skip: int, limit: int):
    return db.query(models.Province).offset(skip).limit(limit).all()

def create_province(db: Session, province: schemas.ProvinceCreate):
    new_province = models.Province(**province.dict())
    db.add(new_province)
    db.commit()
    db.refresh(new_province)
    return new_province

def get_profecion(db: Session, code_number: int):
    return db.query(models.Profecion).filter(models.Profecion.code_number == code_number).first()

def get_profeciones(db: Session, skip: int, limit: int):
    return db.query(models.Profecion).offset(skip).limit(limit).all()

def create_profecion(db: Session, profe: schemas.ProfecionCreate):
    new_profecion = models.Profecion(**profe.dict())
    db.add(new_profecion)
    db.commit()
    db.refresh(new_profecion)
    return new_profecion

