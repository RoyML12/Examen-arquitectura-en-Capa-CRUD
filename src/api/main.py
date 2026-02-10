from fastapi import FastAPI
from src.api.routers import clientes, vehiculos, ordenes
from src.api.error_handlers import register_error_handlers

app = FastAPI(title="Taller Mecanico")

register_error_handlers(app)

app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(vehiculos.router, prefix="/vehiculos", tags=["Vehículos"])
app.include_router(ordenes.router, prefix="/ordenes", tags=["Órdenes"])
