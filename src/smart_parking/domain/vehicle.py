from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .types import NormalizedPlate, UserId


@dataclass(frozen=True)
class Vehicle:
    """
    Entidad de dominio que representa un vehiculo registrado en el sistema.

    En esta iteracion el modelo se alinea con las reglas definidas en el diseño:
    - `patente` debe utilizar el valor normalizado.
    - `marca`, `modelo` y `color` deben estar presentes y ser consistentes con
      validaciones futuras (trim + longitud maxima).
    """

    id: str
    user_id: UserId
    patente: NormalizedPlate
    marca: str
    modelo: str
    color: str
    fecha_alta: datetime

