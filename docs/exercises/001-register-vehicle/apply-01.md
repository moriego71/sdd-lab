# Apply 001

## Objetivo

Iniciar la implementación del Ejercicio 001 respetando el enfoque incremental del laboratorio.

En esta primera iteración se busca únicamente crear la estructura base del proyecto y el modelo de dominio `Vehicle`, evitando implementar infraestructura, persistencia o API.

---

# Prompt enviado a OpenSpec

```text
/opsx:apply

Implementemos únicamente la primera iteración del Ejercicio 001.

Respetá las decisiones definidas en:
- AGENTS.md
- proposal.md
- design.md
- tasks.md

Stack tecnológico:
- Lenguaje: Python
- Base de datos: PostgreSQL

Objetivo de esta iteración:

1. Crear la estructura inicial del proyecto Python.
2. Crear únicamente el dominio de Vehicle y la organización de carpetas.
3. No implementar todavía la API HTTP.
4. No implementar todavía PostgreSQL.
5. No implementar todavía persistencia.
6. No implementar todavía autenticación.
7. No implementar todavía tests.

Quiero avanzar en pequeños pasos para revisar cada decisión antes de continuar.

Antes de generar código, explicá brevemente qué archivos vas a crear y por qué.

Al finalizar, exportá toda la respuesta en un único bloque Markdown para poder archivarla como documentación del laboratorio. No agregues contenido nuevo; únicamente reformatéala en un único bloque Markdown.
```

---

# Respuesta de OpenSpec

```md
### Qué voy a crear y por qué

- **`pyproject.toml`**  
  Define la estructura mínima del proyecto Python, usando `setuptools` y el layout `src/`.  
  En esta iteración no agrego dependencias porque todavía **no** vamos a implementar API HTTP, PostgreSQL, persistencia, autenticación ni tests.

- **`src/smart_parking/__init__.py`**  
  Marca el paquete principal del proyecto.  
  Sirve como base para organizar luego la arquitectura por capas.

- **`src/smart_parking/domain/__init__.py`**  
  Marca el paquete de dominio.  
  Acá deben vivir las entidades y reglas de negocio, separadas de infraestructura.

- **`src/smart_parking/domain/vehicle.py`**  
  Define la entidad de dominio `Vehicle` con la estructura básica acordada en `design.md`:  
  `id`, `user_id`, `plate`, `brand`, `model`, `color`, `created_at`.

  En esta primera iteración **no** incluiré todavía:
  - normalización de patente;
  - validaciones;
  - repositorios;
  - servicios de aplicación;
  - API HTTP;
  - autenticación;
  - persistencia;
  - tests.

---

### Archivos

#### `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "smart-parking-platform"
version = "0.1.0"
description = "Smart Parking Platform - SDD lab project (register vehicle module first)"
readme = "README.md"
requires-python = ">=3.11"
authors = [
  { name = "SDD Lab" }
]
dependencies = []

[project.optional-dependencies]
dev = []

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
```

#### `src/smart_parking/__init__.py`

```python
"""
Paquete principal de dominio para Smart Parking Platform.

En esta primera iteración solo se modela el dominio de Vehículo.
"""
```

#### `src/smart_parking/domain/__init__.py`

```python
"""
Módulo de dominio.

Contiene las entidades y reglas de negocio del sistema.
"""
```

#### `src/smart_parking/domain/vehicle.py`

```python
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import NewType


UserId = NewType("UserId", str)


@dataclass(frozen=True)
class Vehicle:
    """
    Entidad de dominio que representa un vehículo registrado en el sistema.

    Esta primera iteración solo define la estructura básica según las
    decisiones de diseño. La lógica de normalización de la patente y
    las validaciones se implementarán en iteraciones posteriores.
    """

    id: str
    user_id: UserId
    plate: str
    brand: str
    model: str
    color: str
    created_at: datetime
```

---

### Resultado esperado de la iteración

Con esto queda preparada una base mínima y limpia para el proyecto:

- estructura inicial Python;
- paquete principal;
- paquete de dominio;
- entidad `Vehicle`.

Todavía no se introduce ninguna decisión de infraestructura, para mantener esta iteración chica y revisable.
```

### Qué acabo de crear y por qué

- **`pyproject.toml`**: define el proyecto Python (`smart-parking-platform`), usando `setuptools` y mapeando el código a `src/`. No agrega dependencias aún, respetando que en esta iteración no hay API, DB ni tests.
- **`src/smart_parking/__init__.py`**: punto de entrada del paquete de dominio de la plataforma, preparado para crecer por capas (dominio, aplicación, persistencia, API).
- **`src/smart_parking/domain/__init__.py`**: marca el subpaquete de dominio, donde vivirá toda la lógica de negocio independiente de infraestructura.
- **`src/smart_parking/domain/vehicle.py`**: modelo de dominio `Vehicle` (dataclass inmutable) con los campos decididos en `design.md` (`id`, `user_id`, `plate`, `brand`, `model`, `color`, `created_at`) y un `UserId` tipado. No incluye aún normalización de patente, validaciones, servicios de aplicación, persistencia, autenticación ni tests, alineado con el objetivo de esta primera iteración.

---

# Observaciones del ingeniero

- Se respetó el alcance definido para la primera iteración.
- No se implementó infraestructura ni persistencia.
- No se implementó API ni autenticación.
- Se creó únicamente la estructura inicial del proyecto y el modelo de dominio `Vehicle`.
- La implementación quedó alineada con las decisiones definidas en `design.md`.

---

# Aprendizajes

- Es conveniente limitar explícitamente el alcance de `/opsx:apply` para evitar implementaciones demasiado grandes.
- Solicitar la exportación de la respuesta en un único bloque Markdown facilita el archivado de la conversación técnica.
- Documentar conjuntamente el **prompt** y la **respuesta** permite construir un historial de ingeniería de prompts reutilizable en futuras iteraciones del laboratorio.