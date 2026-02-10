from pydantic import BaseModel, Field

class OrdenBase(BaseModel):
    id_vehiculo: int
    falla_vehiculo: str = Field(min_length=1, max_length=500)

class OrdenCreate(OrdenBase):
    pass

class OrdenUpdate(OrdenBase):
    pass

class Orden(OrdenBase):
    id_orden: int
