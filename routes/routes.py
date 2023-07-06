from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db, engine
from models import models
from schemas import schemas
from crud import crud

models.Base.metadata.create_all(engine)

padron = APIRouter()

@padron.get('/countries/{code_country}', response_model=schemas.Country)
def get_country(code_country: int, db: Session = Depends(get_db)):
    db_country = crud.get_code_country(db, code_country)
    if not db_country:
        raise HTTPException(status_code=400, detail='Country not found')
    return db_country

@padron.get('/countries', response_model=list[schemas.Country])
def get_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_countries(db, skip, limit)

@padron.post('/countries', response_model=schemas.Country)
def create_country(country: schemas.CountryCreate, db: Session = Depends(get_db)):
    new_country = crud.get_code_country(db, country.code_country)
    if new_country:
        raise HTTPException(status_code=400, detail="El pais ya existe")
    return crud.create_country(db, country)

@padron.get('/provinces/{code_province}', response_model=schemas.Province)
def get_province(code_province: int, db: Session = Depends(get_db)):
    db_province = crud.get_code_province(db, code_province)
    if not db_province:
        raise HTTPException(status_code=400, detail='Province not found')
    return db_province

@padron.get('/provinces', response_model=list[schemas.Province])
def get_provinces(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_provinces(db, skip, limit)

@padron.post('/provinces', response_model=schemas.Province)
def create_provinces(province: schemas.ProvinceCreate, db: Session = Depends(get_db)):
    new_province = crud.get_code_province(db, province.code_province)
    if new_province:
        raise HTTPException(status_code=400, detail='Province already exists')
    return crud.create_province(db, province)

@padron.get('/profeciones/{code_number}', response_model=schemas.Profecion)
def get_profecion(code_number: int, db: Session = Depends(get_db)):
    db_profecion = crud.get_profecion(db, code_number)
    if not db_profecion:
        raise HTTPException(status_code=400, detail='Profecion not found')
    return db_profecion

@padron.get('/profeciones', response_model=list[schemas.Profecion])
def get_profeciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_profeciones(db, skip, limit)

@padron.post('/profeciones', response_model=schemas.Profecion)
def create_profecion(profe: schemas.ProfecionCreate, db: Session = Depends(get_db)):
    return crud.create_profecion(db, profe)
    
        
    