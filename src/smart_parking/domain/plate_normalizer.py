from __future__ import annotations

from .errors import ValidationError
from .types import NormalizedPlate


class PlateNormalizer:
    """
    Normaliza la patente antes de validar y persistir.

    Reglas:
    - eliminar espacios al comienzo y al final;
    - convertir a mayusculas;
    - eliminar espacios internos.
    """

    @staticmethod
    def normalize(raw_plate: str) -> NormalizedPlate:
        if raw_plate is None:
            raise ValidationError(field="plate", message="La patente es obligatoria.")

        if not isinstance(raw_plate, str):
            raise ValidationError(field="plate", message="La patente debe ser un texto.")

        # split() sin argumentos elimina cualquier whitespace repetida y
        # tambien elimina whitespace al inicio/fin.
        normalized = "".join(raw_plate.split()).upper()
        return NormalizedPlate(normalized)

