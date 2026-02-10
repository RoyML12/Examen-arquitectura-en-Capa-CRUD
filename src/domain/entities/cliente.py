from pydantic import BaseModel, EmailStr, Field

class ClienteBase(BaseModel):
    nombre: str = Field(min_length=1, max_length=120)
    email: EmailStr
    telefono: str = Field(min_length=5, max_length=30)

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id_cliente: int
