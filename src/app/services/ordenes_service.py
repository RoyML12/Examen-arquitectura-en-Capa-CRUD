from typing import List
from src.domain.entities.orden import Orden, OrdenCreate, OrdenUpdate
from src.domain.errors import NotFoundError, ForeignKeyError
from src.domain.ports.repositories import OrdenRepository, VehiculoRepository

class OrdenesService:
    def __init__(self, repo: OrdenRepository, vehiculos_repo: VehiculoRepository):
        self.repo = repo
        self.vehiculos_repo = vehiculos_repo

    def list(self) -> List[Orden]:
        return self.repo.list()

    def get(self, id_orden: int) -> Orden:
        orden = self.repo.get(id_orden)
        if not orden:
            raise NotFoundError("Orden no encontrada")
        return orden

    def create(self, data: OrdenCreate) -> Orden:
        if not self.vehiculos_repo.get(data.id_vehiculo):
            raise ForeignKeyError("El id_vehiculo no existe")
        return self.repo.create(data)

    def update(self, id_orden: int, data: OrdenUpdate) -> Orden:
        if not self.repo.get(id_orden):
            raise NotFoundError("Orden no encontrada")
        if not self.vehiculos_repo.get(data.id_vehiculo):
            raise ForeignKeyError("El id_vehiculo no existe")
        return self.repo.update(id_orden, data)

    def delete(self, id_orden: int) -> None:
        if not self.repo.get(id_orden):
            raise NotFoundError("Orden no encontrada")
        self.repo.delete(id_orden)
