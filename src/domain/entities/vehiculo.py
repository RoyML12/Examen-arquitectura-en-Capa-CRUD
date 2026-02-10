from pydantic import BaseModel, Field

class VehiculoBase(BaseModel):
    nombre: str = Field(min_length=1, max_length=120)
    modelo: str = Field(min_length=1, max_length=120)
    id_cliente: int

class VehiculoCreate(VehiculoBase):
    pass

class VehiculoUpdate(VehiculoBase):
    pass

class Vehiculo(VehiculoBase):
    id_vehiculo: int
