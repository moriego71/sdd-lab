from __future__ import annotations

from typing import Protocol

from .types import NormalizedPlate
from .vehicle import Vehicle


class VehicleRepository(Protocol):
    """
    Contrato de persistencia para la entidad Vehicle.

    Esta interfaz pertenece al dominio y define solo las operaciones
    necesarias para el caso de uso de registro de vehiculos.
    """

    def save(self, vehicle: Vehicle) -> Vehicle:
        """
        Persiste un vehiculo y devuelve la entidad almacenada.
        """
        ...

    def exists_by_plate(self, normalized_plate: NormalizedPlate) -> bool:
        """
        Indica si ya existe un vehiculo con la patente normalizada informada.
        """
        ...

