from src.api import settings
from src.data.repositories.clientes_json_repo import ClientesJsonRepository
from src.data.repositories.vehiculos_json_repo import VehiculosJsonRepository
from src.data.repositories.ordenes_json_repo import OrdenesJsonRepository

from src.app.services.clientes_service import ClientesService
from src.app.services.vehiculos_service import VehiculosService
from src.app.services.ordenes_service import OrdenesService

_clientes_repo = ClientesJsonRepository(settings.CLIENTES_FILE)
_vehiculos_repo = VehiculosJsonRepository(settings.VEHICULOS_FILE)
_ordenes_repo = OrdenesJsonRepository(settings.ORDENES_FILE)

def get_clientes_service() -> ClientesService:
    return ClientesService(_clientes_repo)

def get_vehiculos_service() -> VehiculosService:
    return VehiculosService(_vehiculos_repo, _clientes_repo)

def get_ordenes_service() -> OrdenesService:
    return OrdenesService(_ordenes_repo, _vehiculos_repo)
