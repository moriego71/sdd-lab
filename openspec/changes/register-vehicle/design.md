# Diseño

## Contexto

Smart Parking Platform es un proyecto nuevo (greenfield).

Este cambio implementa el primer módulo funcional: el registro de vehículos para conductores autenticados.

### Documentación de referencia

- `docs/exercises/001-register-vehicle/exercise.md` — análisis funcional original.
- `docs/exercises/001-register-vehicle/explore.md` — resultado de la exploración realizada con OpenSpec.
- `docs/exercises/001-register-vehicle/review.md` — decisiones tomadas por el ingeniero antes de generar la propuesta.

### Restricciones definidas

- La autenticación se considera resuelta y no forma parte de este módulo.
- El alcance comprende únicamente el registro de vehículos.
- La patente debe ser única en todo el sistema y será normalizada antes de almacenarse.
- En esta primera versión no se validará el formato oficial de las patentes argentinas.
- Marca, modelo y color son campos obligatorios de texto libre.
- La tecnología de persistencia será una decisión de implementación y no forma parte de esta especificación.

---

# Modelo de dominio inicial

```
Usuario (1) ─────────< Vehículo (N)

Vehículo

- id
- userId
- patente
- marca
- modelo
- color
- fechaAlta
```

---

# Objetivos

- Permitir que un conductor autenticado registre un vehículo indicando:
  - patente
  - marca
  - modelo
  - color

- Garantizar la unicidad de la patente mediante normalización y una restricción de unicidad.

- Asociar el vehículo al usuario que realiza el registro.

- Devolver respuestas claras tanto para operaciones exitosas como para errores de validación.

- Establecer una arquitectura por capas que sirva de base para los módulos futuros.

---

# Fuera del alcance

No forman parte de este módulo:

- Registro e inicio de sesión de usuarios.
- Operaciones de modificación, listado o eliminación.
- Validación del formato oficial de la patente argentina.
- Catálogos de marcas, modelos o colores.
- Interfaces para inspectores.
- Gestión de estacionamientos.
- Pagos.
- Fotografías del vehículo.
- Año del vehículo u otros datos descriptivos.

---

# Decisiones de diseño

## 1. Registro de vehículos

El módulo implementará únicamente la funcionalidad de registrar un vehículo.

No se desarrollarán otras operaciones sobre la entidad Vehículo.

**Motivo**

Mantener el alcance reducido y completamente verificable.

---

## 2. Usuario autenticado

Se asumirá que el usuario ya se encuentra autenticado.

Mientras no exista el módulo de autenticación se utilizará un usuario simulado (stub).

**Motivo**

Cumplir la precondición definida en la especificación sin aumentar innecesariamente el alcance.

---

## 3. Normalización de la patente

Antes de validar y almacenar una patente se realizarán las siguientes transformaciones:

1. Eliminar espacios al comienzo y al final.
2. Convertir todos los caracteres a mayúsculas.
3. Eliminar espacios internos.

La comparación y almacenamiento utilizarán siempre el valor normalizado.

**Motivo**

Evitar registros duplicados producidos por diferencias de escritura.

Ejemplo:

```
ABC123
abc123
ABC 123
```

Representan el mismo vehículo.

---

## 4. Marca, modelo y color

Los tres atributos serán:

- obligatorios;
- de texto libre;
- sin espacios únicamente;
- con una longitud máxima de 100 caracteres.

**Motivo**

Permitir la identificación visual sin incorporar todavía catálogos de datos.

---

## 5. Arquitectura

El módulo seguirá una arquitectura por capas.

```
Controlador
        │
        ▼
Servicio de Registro de Vehículos
        │
        ├── Normalizador de Patentes
        ├── Validador de Campos
        ▼
Repositorio de Vehículos
```

**Motivo**

Separar claramente:

- transporte;
- reglas de negocio;
- persistencia.

Esta estructura podrá reutilizarse en futuros módulos.

---

## 6. Control de unicidad

La unicidad de la patente se verificará en dos niveles.

Primer nivel:

- validación desde la lógica de negocio.

Segundo nivel:

- restricción UNIQUE en la persistencia.

**Motivo**

Obtener mensajes de error claros y evitar condiciones de carrera.

---

## 7. Respuestas del sistema

El sistema devolverá respuestas estructuradas para:

- registro exitoso;
- errores de validación;
- patente duplicada;
- usuario no autenticado.

La estructura concreta de las respuestas dependerá de la tecnología utilizada durante la implementación.

---

## 8. Persistencia

La tecnología de persistencia queda abierta.

Durante la implementación podrá utilizarse:

- SQLite;
- PostgreSQL;
- otra alternativa adecuada.

Como mínimo será necesario almacenar:

- id
- usuario
- patente
- marca
- modelo
- color
- fecha de alta

---

# Riesgos conocidos

- El usuario simulado deberá reemplazarse posteriormente por el módulo real de autenticación.
- Los campos de texto libre pueden generar inconsistencias de escritura.
- La ausencia de validación del formato de patente permitirá valores inválidos durante el MVP.
- La restricción UNIQUE protegerá frente a registros duplicados simultáneos.

---

# Plan de implementación

Al tratarse de un proyecto nuevo:

1. Crear la estructura de persistencia.
2. Incorporar un usuario de prueba.
3. Implementar el registro de vehículos.
4. Ejecutar las pruebas correspondientes.

---

# Decisiones pendientes

Antes de comenzar la implementación será necesario decidir:

- tecnología de persistencia;
- stack tecnológico;
- mecanismo temporal para el usuario autenticado;
- estructura definitiva de la API.