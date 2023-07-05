from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Country(Base):
    __tablename__ = 'countries'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    code_country = Column(Integer, unique=True)
    
    province = relationship('Province', back_populates='owner_province')

class Province(Base):
    __tablename__ = 'provinces'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    code_province = Column(Integer, unique=True)
    code_country = Column(Integer, ForeignKey('countries.code_country'))
    
    owner_province = relationship('Country', back_populates='province')
    prof = relationship('Profecion', back_populates='owner_profes')
    
class Profecion():
    __tablename__ = 'profeciones'
    
    id = Column(Integer, primary_key=True)
    code_number = Column(Integer)
    tipo_profecion = Column(String)
    code_province = Column(Integer, ForeignKey('profeciones.code_province'))
    
    owner_profes = relationship('Province', back_populates='prof')