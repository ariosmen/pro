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

def get_profesion(db: Session, code_number: int):
    return db.query(models.Profesion).filter(models.Profesion.code_number == code_number).first()

def get_profesiones(db: Session, skip: int, limit: int):
    return db.query(models.Profesion).offset(skip).limit(limit).all()

def create_profesion(db: Session, profe: schemas.ProfesionCreate):
    new_profesion = models.Profesion(**profe.dict())
    db.add(new_profesion)
    db.commit()
    db.refresh(new_profesion)
    return new_profesion

def cantidad_profesiones(db: Session, code_province: int):
    name = db.query(models.Province).filter(models.Province.code_province == code_province).first()
    db_profesiones = db.query(models.Profesion).filter(models.Profesion.code_province == code_province).all()
    return {"name": name.name, "cantidad": len(db_profesiones)}

def profesiones_for_code_province(db:Session, code_province):
    return db.query(models.Profesion).filter(models.Profesion.code_province == code_province).all()