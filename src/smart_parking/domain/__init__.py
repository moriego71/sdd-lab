"""
Módulo de dominio.

Contiene las entidades y reglas de negocio del sistema.
"""

from .errors import AuthenticationRequiredError, DuplicatePlateError, ValidationError
from .plate_normalizer import PlateNormalizer
from .repository import VehicleRepository
from .types import NormalizedPlate, UserId
from .validation import ValidatedVehicleRegistrationInput, validate_vehicle_registration_fields
from .vehicle import Vehicle

__all__ = [
    "Vehicle",
    "UserId",
    "NormalizedPlate",
    "PlateNormalizer",
    "VehicleRepository",
    "ValidatedVehicleRegistrationInput",
    "validate_vehicle_registration_fields",
    "ValidationError",
    "DuplicatePlateError",
    "AuthenticationRequiredError",
]

