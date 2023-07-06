from pydantic import BaseModel

class ProfecionBase(BaseModel):
    pass

class ProfecionCreate(ProfecionBase):
    code_number: int
    tipo_profecion: str
    code_province: int

class Profecion(ProfecionBase):
    id: int
    code_number: int
    tipo_profecion: str
    
    class Config:
        orm_mode = True


class ProvinceBase(BaseModel):
    name: str
    code_province: int
    code_country: int
    
class ProvinceCreate(ProvinceBase):
    pass

class CantidadProfeciones(BaseModel):
    name: str
    cantidad: int
    
class Province(ProvinceBase):
    id: int
    profeciones: list[Profecion] = []
    
    class Config:
        orm_mode = True
    

class CountryBase(BaseModel):
    name: str
    code_country: int

class CountryCreate(CountryBase):
    pass
    
class Country(CountryBase):
    id: int
    provinces: list[Province] = []
    
    class Config:
        orm_mode = True