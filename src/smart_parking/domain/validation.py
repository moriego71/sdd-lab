from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .errors import ValidationError
from .types import NormalizedPlate


MAX_FIELD_LENGTH = 100


@dataclass(frozen=True)
class ValidatedVehicleRegistrationInput:
    """
    Representa los datos del registro ya validados y listos para el
    procesamiento posterior (por ejemplo, persistencia).
    """

    patente: NormalizedPlate
    marca: str
    modelo: str
    color: str


def _validate_required_text(field: str, value: Optional[str]) -> str:
    if value is None:
        raise ValidationError(field=field, message=f"El campo {field} es obligatorio.")

    if not isinstance(value, str):
        raise ValidationError(field=field, message=f"El campo {field} debe ser un texto.")

    trimmed = value.strip()
    if trimmed == "":
        raise ValidationError(field=field, message=f"El campo {field} es obligatorio.")

    if len(trimmed) > MAX_FIELD_LENGTH:
        raise ValidationError(
            field=field,
            message=f"El campo {field} no debe superar {MAX_FIELD_LENGTH} caracteres.",
        )

    return trimmed


def validate_vehicle_registration_fields(
    patente: NormalizedPlate,
    marca: Optional[str],
    modelo: Optional[str],
    color: Optional[str],
) -> ValidatedVehicleRegistrationInput:
    """
    Valida la entrada del registro luego de normalizar la patente.

    - patente: debe ser no vacia (ya normalizada).
    - marca/modelo/color: texto requerido, sin vacios luego de trim y con
      longitud maxima.
    """

    patente_str = str(patente) if patente is not None else ""
    patente_str = patente_str.strip()
    if patente_str == "":
        raise ValidationError(field="plate", message="El campo patente es obligatorio.")

    if len(patente_str) > MAX_FIELD_LENGTH:
        raise ValidationError(
            field="plate",
            message=f"El campo patente no debe superar {MAX_FIELD_LENGTH} caracteres.",
        )

    marca_trimmed = _validate_required_text(field="brand", value=marca)
    modelo_trimmed = _validate_required_text(field="model", value=modelo)
    color_trimmed = _validate_required_text(field="color", value=color)

    return ValidatedVehicleRegistrationInput(
        patente=NormalizedPlate(patente_str),
        marca=marca_trimmed,
        modelo=modelo_trimmed,
        color=color_trimmed,
    )

