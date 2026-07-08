# Apply 001

## Objetivo

Continuar la implementación del Ejercicio 001 desarrollando exclusivamente la capa de dominio.

En esta segunda iteración se incorporan las reglas de negocio fundamentales del vehículo: normalización de la patente, validación de los datos de entrada y definición de los errores de dominio, manteniendo la independencia respecto de la persistencia, la API HTTP y la infraestructura.

---

# Prompt enviado a OpenSpec
/opsx:apply

Continuemos con la segunda iteración del Ejercicio 001.

Respetá las decisiones definidas en:

- AGENTS.md
- proposal.md
- design.md
- tasks.md

Stack tecnológico:

- Lenguaje: Python
- Base de datos: PostgreSQL

En esta iteración implementá únicamente el dominio.

Objetivos:

1. Implementar `PlateNormalizer`.
2. Implementar la validación de los campos del vehículo.
3. Definir los errores de dominio (`ValidationError`, `DuplicatePlateError`, `AuthenticationRequiredError`).
4. Mantener el modelo `Vehicle` consistente con las reglas definidas en el diseño.
5. No implementar todavía repositorios.
6. No implementar todavía PostgreSQL.
7. No implementar todavía servicios de aplicación.
8. No implementar todavía API HTTP.
9. No implementar todavía tests.

Antes de generar el código, explicá brevemente qué archivos vas a crear o modificar y por qué.

Al finalizar, exportá toda la respuesta en un único bloque Markdown para poder archivarla como documentación del laboratorio. No agregues contenido nuevo; únicamente reformatéala en un único bloque Markdown.

# Respuesta de OpenSpec
```markdown
Implementación - Iteración 2 (solo dominio) | Ejercicio 001

### Archivos creados / modificados (y por qué)

Modifiqué:
- `src/smart_parking/domain/vehicle.py`: para alinear el modelo `Vehicle` con el diseño (`patente`, `marca`, `modelo`, `color`, `fecha_alta`) y hacer explícito que `patente` debe ser el valor normalizado.

Creé:
- `src/smart_parking/domain/types.py`: para centralizar tipos del dominio (`UserId`, `NormalizedPlate`) y evitar dependencias circulares entre módulos.
- `src/smart_parking/domain/errors.py`: para definir los errores de dominio solicitados:
  - `ValidationError`
  - `DuplicatePlateError`
  - `AuthenticationRequiredError`
- `src/smart_parking/domain/plate_normalizer.py`: para implementar `PlateNormalizer` con las transformaciones definidas en el diseño (strip, uppercase, eliminar espacios internos).
- `src/smart_parking/domain/validation.py`: para implementar la validación de campos requeridos del registro del vehículo (no vacío tras trim, y máximo 100 caracteres), devolviendo una estructura validada.
- `src/smart_parking/domain/__init__.py`: para exportar los componentes del dominio de manera consistente.

### Qué se implementó

- `PlateNormalizer.normalize(raw_plate) -> NormalizedPlate`
  - Elimina espacios al inicio/fin.
  - Convierte a mayúsculas.
  - Elimina espacios internos (por `split()` + join).
- Validación de campos:
  - `validate_vehicle_registration_fields(patente, marca, modelo, color)`
  - Verifica:
    - `patente` no vacía (ya normalizada).
    - `marca`, `modelo`, `color` requeridos, no vacíos tras `strip()`.
    - que cada campo no supere `100` caracteres.
  - Retorna `ValidatedVehicleRegistrationInput` con los datos listos para etapas posteriores.
- Errores de dominio:
  - `ValidationError(field, message)` con `field` y `message`.
  - `DuplicatePlateError` (definido para la siguiente etapa cuando haya repositorio).
  - `AuthenticationRequiredError` (definido para la siguiente etapa cuando se modele autenticación).
- Modelo `Vehicle` actualizado:
  - Campos: `id`, `user_id`, `patente`, `marca`, `modelo`, `color`, `fecha_alta`.
  - Comentario/docstring aclara la expectativa de `patente` normalizada.

### Restricciones respetadas
- No se implementaron repositorios.
- No se implementó PostgreSQL.
- No se implementaron servicios de aplicación.
- No se implementó API HTTP.
- No se implementaron tests.

Verificación: `ReadLints` no encontró errores en `src/smart_parking/domain`.
```

---

# Observaciones del ingeniero

- La implementación respetó el alcance definido para la segunda iteración.
- La lógica de dominio quedó correctamente desacoplada de la infraestructura.
- Se separaron las responsabilidades en componentes específicos (normalización, validación, tipos y errores), mejorando la mantenibilidad del código.
- No se incorporaron elementos fuera del alcance (API, persistencia, autenticación o tests).
- Se detectó una decisión de diseño a revisar: el código generado utiliza nombres de atributos en español (`patente`, `marca`, `modelo`, etc.). Se propone adoptar el inglés como idioma oficial para todo el código fuente y mantener el español únicamente para la documentación funcional y metodológica. Esta decisión se incorpora a `AGENTS.md` antes de continuar con las siguientes iteraciones.

---

# Aprendizajes

- Dividir `/opsx:apply` en iteraciones pequeñas permite revisar con detalle cada decisión técnica antes de incorporarla al proyecto.
- Es conveniente solicitar primero una explicación de los archivos que se crearán y luego revisar el código generado.
- Documentar el prompt junto con la respuesta de OpenSpec genera un historial de ingeniería de prompts útil tanto para el aprendizaje como para la trazabilidad del proyecto.
- Definir tempranamente convenciones globales, como el idioma del código fuente, evita refactorizaciones innecesarias en etapas posteriores.