# Ejercicio 001

# Registrar un vehículo

## Objetivo de aprendizaje

Aprender el flujo completo de Specification-Driven Development (SDD) utilizando OpenSpec.

---

# Origen del requisito

**Fuente**

- [x] Idea del producto
- [ ] Necesidad de un usuario
- [ ] Investigación
- [ ] Cambio normativo
- [ ] Mejora técnica
- [ ] Otro

**Observaciones**

Esta funcionalidad constituye el primer módulo del proyecto Smart Parking Platform.

---

# Contexto

El sistema permitirá que un conductor registre uno o más vehículos propios para utilizarlos dentro de la plataforma de Smart Parking.

Además de la identificación automática mediante la patente, los inspectores de tránsito deberán poder verificar visualmente que el vehículo estacionado corresponde al registrado.

---

# Objetivo

Permitir registrar un vehículo con toda la información necesaria para su identificación lógica y visual.

---

# Historia de Usuario

> Como conductor registrado,
> quiero registrar un vehículo indicando su patente, marca, modelo y color,
> para que el sistema pueda identificarlo automáticamente y los inspectores puedan verificar visualmente que el vehículo corresponde al registrado.

---

# Precondiciones

- El usuario debe haber iniciado sesión.

---

# Criterios de aceptación

- El usuario puede registrar un vehículo.
- Todos los campos son obligatorios.
- La patente debe ser única.
- El vehículo queda asociado al usuario.
- El sistema informa claramente si el registro fue exitoso o si ocurrió un error.

---

# Decisiones de diseño

- La patente identifica de forma única al vehículo.
- Marca, modelo y color son obligatorios para facilitar la identificación visual por parte de los inspectores.
- No se admiten registros incompletos.

---

# Estado

🟡 Pendiente de exploración con OpenSpec.