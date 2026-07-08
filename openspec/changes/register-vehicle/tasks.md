# Tareas de implementación

## 1. Preparación del proyecto

- [ ] 1.1 Inicializar la estructura base del proyecto (gestor de paquetes, punto de entrada y framework de pruebas).
- [ ] 1.2 Configurar el entorno de desarrollo y los scripts principales (inicio, pruebas y migraciones).
- [ ] 1.3 Incorporar un middleware de autenticación simulado (stub) que inyecte un usuario autenticado fijo durante el desarrollo y las pruebas.

---

## 2. Capa de persistencia

- [ ] 2.1 Crear una tabla (o registro inicial) de usuarios que permita cumplir la relación de pertenencia del vehículo.
- [ ] 2.2 Crear la estructura de la entidad **Vehículo** con los siguientes atributos:
  - id
  - user_id
  - patente
  - marca
  - modelo
  - color
  - fecha_alta
- [ ] 2.3 Definir una restricción **UNIQUE** sobre la patente normalizada.
- [ ] 2.4 Implementar el repositorio `VehicleRepository` con, al menos, las siguientes operaciones:
  - `save(vehicle)`
  - `existsByPlate(normalizedPlate)`

---

## 3. Dominio y validaciones

- [ ] 3.1 Implementar el componente `PlateNormalizer`, encargado de:
  - eliminar espacios al principio y al final;
  - convertir la patente a mayúsculas;
  - eliminar espacios internos.
- [ ] 3.2 Implementar la validación de los campos obligatorios:
  - patente;
  - marca;
  - modelo;
  - color.

  Las validaciones deberán verificar:
  - que el campo no esté vacío;
  - que no contenga únicamente espacios;
  - que no supere los 100 caracteres.

- [ ] 3.3 Definir los errores de dominio:
  - `ValidationError`
  - `DuplicatePlateError`
  - `AuthenticationRequiredError`

---

## 4. Servicio de aplicación

- [ ] 4.1 Implementar `VehicleRegistrationService.register(userId, input)` con el siguiente flujo:

  1. Normalizar la patente.
  2. Validar los datos.
  3. Verificar que la patente no exista.
  4. Persistir el vehículo.

- [ ] 4.2 Garantizar que el vehículo siempre quede asociado al usuario autenticado obtenido del contexto, nunca desde los datos enviados por el cliente.

- [ ] 4.3 Devolver una respuesta estructurada con la información del vehículo registrado.

---

## 5. API HTTP

- [ ] 5.1 Implementar el endpoint `POST /vehicles`.
- [ ] 5.2 Devolver **HTTP 201** cuando el registro sea exitoso.
- [ ] 5.3 Devolver **HTTP 400** para errores de validación, indicando los campos afectados.
- [ ] 5.4 Devolver **HTTP 409** cuando la patente ya exista, mostrando el mensaje:

```
La patente ya está registrada.
```

- [ ] 5.5 Devolver **HTTP 401** cuando el usuario no se encuentre autenticado.

---

## 6. Pruebas

- [ ] 6.1 Verificar el registro exitoso de un vehículo.
- [ ] 6.2 Verificar que no sea posible registrar una patente duplicada, incluso cuando existan diferencias de mayúsculas o espacios.
- [ ] 6.3 Verificar la ausencia de cada campo obligatorio y los casos con espacios en blanco.
- [ ] 6.4 Verificar que una solicitud sin autenticación responda con **HTTP 401**.
- [ ] 6.5 Verificar que el vehículo quede asociado correctamente al usuario autenticado.

---

## 7. Verificación final

- [ ] 7.1 Ejecutar toda la batería de pruebas y comprobar que todos los escenarios definidos por la especificación se cumplen.
- [ ] 7.2 Realizar una prueba manual del registro de vehículos utilizando la API (por ejemplo mediante `curl` o un cliente HTTP).
- [ ] 7.3 Actualizar el estado del ejercicio en:

`docs/exercises/001-register-vehicle/exercise.md`

marcándolo como completado una vez finalizada la implementación.
