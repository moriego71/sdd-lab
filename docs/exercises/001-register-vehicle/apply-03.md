# Apply 003

## Objetivo
/opsx:apply

Continuemos con la tercera iteración del Ejercicio 001.

Respetá las decisiones definidas en:

- AGENTS.md
- proposal.md
- design.md
- tasks.md

Stack tecnológico:

- Lenguaje: Python
- Base de datos: PostgreSQL (todavía no implementar)

En esta iteración implementá únicamente la abstracción de persistencia.

Objetivos:

1. Definir la interfaz `VehicleRepository`.
2. Declarar las operaciones necesarias para este caso de uso:
   - `save(vehicle)`
   - `exists_by_plate(normalized_plate)`
3. Mantener completamente desacoplado el dominio de cualquier tecnología de persistencia.
4. No implementar todavía PostgreSQL.
5. No implementar repositorios concretos.
6. No implementar servicios de aplicación.
7. No implementar API HTTP.
8. No implementar autenticación.
9. No implementar tests.

Antes de generar código, explicá brevemente qué archivos vas a crear o modificar y por qué.

Al finalizar, exportá toda la respuesta en un único bloque Markdown para poder archivarla como documentación del laboratorio. No agregues contenido nuevo; únicamente reformatéala en un único bloque Markdown.

---

# Prompt enviado a OpenSpec
/opsx:apply

Continuemos con la tercera iteración del Ejercicio 001.

Respetá las decisiones definidas en:

- AGENTS.md
- proposal.md
- design.md
- tasks.md

Stack tecnológico:

- Lenguaje: Python
- Base de datos: PostgreSQL (todavía no implementar)

En esta iteración implementá únicamente la abstracción de persistencia.

Objetivos:

1. Definir la interfaz `VehicleRepository`.
2. Declarar las operaciones necesarias para este caso de uso:
   - `save(vehicle)`
   - `exists_by_plate(normalized_plate)`
3. Mantener completamente desacoplado el dominio de cualquier tecnología de persistencia.
4. No implementar todavía PostgreSQL.
5. No implementar repositorios concretos.
6. No implementar servicios de aplicación.
7. No implementar API HTTP.
8. No implementar autenticación.
9. No implementar tests.

Antes de generar código, explicá brevemente qué archivos vas a crear o modificar y por qué.

Al finalizar, exportá toda la respuesta en un único bloque Markdown para poder archivarla como documentación del laboratorio. No agregues contenido nuevo; únicamente reformatéala en un único bloque Markdown.

# Respuesta de OpenSpec
```markdown
Implementación - Iteración 3 (solo abstracción de persistencia) | Ejercicio 001

### Archivos creados / modificados (y por qué)

Creé:
- `src/smart_parking/domain/repository.py`: para definir la interfaz `VehicleRepository` como contrato del dominio, sin dependencia de tecnología concreta (PostgreSQL u otra).

Modifiqué:
- `src/smart_parking/domain/__init__.py`: para exportar `VehicleRepository` desde el paquete de dominio y mantener una API de módulo consistente.

---

### Qué se implementó

Se definió la interfaz de persistencia pedida para el caso de uso de registro de vehículo:

- `save(vehicle)`
- `exists_by_plate(normalized_plate)`

Implementación realizada en `src/smart_parking/domain/repository.py` usando `Protocol`:

```python
from __future__ import annotations

from typing import Protocol

from .types import NormalizedPlate
from .vehicle import Vehicle


class VehicleRepository(Protocol):
    """
    Contrato de persistencia para la entidad Vehicle.

    Esta interfaz pertenece al dominio y define solo las operaciones
    necesarias para el caso de uso de registro de vehículos.
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
```

Y se exportó en `src/smart_parking/domain/__init__.py`:

```python
from .repository import VehicleRepository
```

(incluido en `__all__`).

---

### Restricciones respetadas

- Dominio desacoplado de persistencia concreta.
- No se implementó PostgreSQL.
- No se implementaron repositorios concretos.
- No se implementaron servicios de aplicación.
- No se implementó API HTTP.
- No se implementó autenticación.
- No se implementaron tests.

Verificación: no se detectaron errores de linter en `src/smart_parking/domain`.
```

---

# Observaciones del ingeniero

- La implementación respetó completamente el alcance definido para la tercera iteración.
- Se definió el contrato `VehicleRepository` sin introducir dependencias hacia PostgreSQL u otra tecnología de persistencia.
- La interfaz contiene únicamente las operaciones necesarias para el caso de uso actual, evitando incorporar funcionalidades fuera del alcance del ejercicio.
- La utilización de `Protocol` resulta adecuada para mantener el dominio desacoplado y facilitar futuras implementaciones concretas.
- La arquitectura comienza a evidenciar una clara separación entre el dominio y la infraestructura, sentando las bases para aplicar una implementación concreta de persistencia en iteraciones posteriores.

---

# Aprendizajes

- Definir primero contratos antes que implementaciones favorece el desacoplamiento y permite evolucionar la infraestructura sin afectar el dominio.
- Limitar cada iteración a una única responsabilidad facilita la revisión técnica y reduce el riesgo de introducir cambios innecesarios.
- El uso de interfaces (`Protocol`) permite diseñar la arquitectura desde el comportamiento esperado, independientemente de la tecnología que se utilice posteriormente.
- La documentación incremental de cada iteración continúa generando un historial claro de decisiones de ingeniería y de la evolución del proyecto.
