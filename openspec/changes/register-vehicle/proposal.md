# Propuesta de cambio

## ¿Por qué?

Smart Parking Platform necesita su primer módulo funcional para que los conductores registrados puedan asociar vehículos a su cuenta.

Sin el registro de vehículos, la plataforma no puede identificar automáticamente un vehículo mediante su patente ni permitir que los inspectores de tránsito realicen una verificación visual utilizando la marca, el modelo y el color.

Este constituye el módulo fundacional de la plataforma y el primer ejercicio del laboratorio de Specification-Driven Development (SDD).

---

## ¿Qué cambia?

Se incorporará la funcionalidad de registro de vehículos, permitiendo que un conductor autenticado registre un vehículo indicando:

- Patente
- Marca
- Modelo
- Color

Se aplicarán las siguientes reglas de negocio:

- Un usuario puede registrar uno o varios vehículos.
- Cada vehículo pertenece a un único usuario.
- La patente debe ser única en todo el sistema.
- Antes de persistir el vehículo, la patente será normalizada para garantizar la unicidad independientemente del uso de mayúsculas, minúsculas o espacios.
- El sistema devolverá mensajes claros tanto para los casos exitosos como para los errores de validación.

Se asume que la autenticación del usuario ya fue resuelta y no forma parte de este cambio.

---

## Fuera del alcance

Esta propuesta **no incluye**:

- Registro e inicio de sesión de usuarios.
- Listado de vehículos.
- Modificación de vehículos.
- Eliminación de vehículos.
- Transferencia de vehículos entre usuarios.
- Validación del formato oficial de las patentes argentinas (se implementará en una iteración futura).
- Catálogos de marcas, modelos o colores (en esta versión serán campos de texto libre).
- Interfaces o funcionalidades destinadas a los inspectores de tránsito.

---

# Capacidades

## Nueva capacidad

### Registro de vehículos

Permitir que un usuario autenticado registre un vehículo, aplicando las validaciones correspondientes, verificando la unicidad de la patente, almacenando la información de forma persistente y devolviendo respuestas estructuradas tanto para los casos exitosos como para los errores.

---

## Capacidades modificadas

Ninguna.

El proyecto aún no posee funcionalidades implementadas.

---

# Impacto

## Dominio

Se incorpora la entidad **Vehículo**, relacionada con la entidad **Usuario**.

La patente pasa a ser el identificador único del vehículo.

## API

Se incorporarán uno o más endpoints para el registro de vehículos.

Su definición exacta será desarrollada durante la etapa de diseño.

## Persistencia

Se incorpora el almacenamiento de vehículos con una restricción de unicidad sobre la patente normalizada.

## Integración con autenticación

Las operaciones requerirán un usuario autenticado.

Durante este ejercicio se asumirá la existencia de un mecanismo de autenticación (stub o middleware).

## Pruebas

Se deberán contemplar, como mínimo, los siguientes escenarios:

- Registro exitoso.
- Patente duplicada.
- Campos obligatorios faltantes.
- Usuario no autenticado.