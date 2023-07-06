from pydantic import BaseModel

class ProfesionBase(BaseModel):
    pass

class ProfesionCreate(ProfesionBase):
    code_number: int
    tipo_profesion: str
    code_province: int

class Profesion(ProfesionBase):
    id: int
    code_number: int
    tipo_profesion: str
    
    class Config:
        orm_mode = True


class ProvinceBase(BaseModel):
    name: str
    code_province: int
    code_country: int
    
class ProvinceCreate(ProvinceBase):
    pass

class CantidadProfesiones(BaseModel):
    name: str
    cantidad: int
    
class Province(ProvinceBase):
    id: int
    profesiones: list[Profesion] = []
    
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