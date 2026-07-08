from __future__ import annotations


class ValidationError(Exception):
    """
    Error de validacion de un campo de registro.

    Se utiliza para comunicar por campo el motivo del rechazo.
    """

    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message
        super().__init__(message)


class DuplicatePlateError(Exception):
    """
    Error cuando una patente ya existe en el sistema (unicidad).
    """

    def __init__(self, message: str = "La patente ya está registrada."):
        super().__init__(message)


class AuthenticationRequiredError(Exception):
    """
    Error cuando una operacion requiere un usuario autenticado.
    """

    def __init__(self, message: str = "Autenticacion requerida"):
        super().__init__(message)

