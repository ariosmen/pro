from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Country(Base):
    __tablename__ = 'countries'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    code_country = Column(Integer, unique=True)
    
    provinces = relationship('Province', back_populates='owner_province')

class Province(Base):
    __tablename__ = 'provinces'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    code_province = Column(Integer, unique=True)
    code_country = Column(Integer, ForeignKey('countries.code_country'))
    
    owner_province = relationship('Country', back_populates='provinces')
    
    profesiones = relationship('Profesion', back_populates='owner_profesion')

class Profesion(Base):
    __tablename__ = 'profesiones'
    
    id = Column(Integer, primary_key=True)
    code_number = Column(Integer, unique=True)
    tipo_profesion = Column(String(100))
    code_province = Column(Integer, ForeignKey('provinces.code_province'))
    
    owner_profesion = relationship('Province', back_populates='profesiones')