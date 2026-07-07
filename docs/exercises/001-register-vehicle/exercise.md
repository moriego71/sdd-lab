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

El sistema Smart Parking permitirá que un conductor registrado asocie uno o más vehículos a su cuenta para utilizarlos dentro de la plataforma.

Además de la identificación automática mediante la patente, los inspectores de tránsito deberán poder verificar visualmente que el vehículo estacionado corresponde al registrado.

---

# Objetivo

Permitir registrar un vehículo asociado a un conductor, almacenando toda la información necesaria para su identificación lógica dentro del sistema y su identificación visual por parte de los inspectores de tránsito.
---

# Historia de Usuario

> Como conductor registrado,
quiero registrar un vehículo indicando su patente, marca, modelo y color,
para que el sistema pueda identificarlo automáticamente mediante la patente y los inspectores puedan corroborar visualmente, a través de la marca, modelo y color, que el vehículo estacionado corresponde al registrado.

---

# Precondiciones

- El usuario debe haber iniciado sesión.
- El usuario debe encontrarse registrado en el sistema.

---

# Reglas de negocio

- Un usuario puede registrar más de un vehículo.
- Un vehículo solamente puede pertenecer a un usuario.
- La patente identifica unívocamente al vehículo.

---

# Criterios de aceptación

1. El usuario puede registrar un vehículo.
2. Los siguientes campos son obligatorios:
   - Patente
   - Marca
   - Modelo
   - Color
3. La patente debe ser única dentro del sistema.
4. El vehículo queda asociado al usuario que realizó el registro.
5. El vehículo se almacena correctamente en la base de datos.
6. El sistema informa claramente si el registro fue exitoso.
7. Si ocurre un error de validación, el sistema informa el motivo.

---

# Decisiones de diseño

- La patente identifica de forma única al vehículo.
- Marca, modelo y color son obligatorios para facilitar la identificación visual por parte de los inspectores.
- No se admiten registros incompletos.

---

# Estado

🟡 Pendiente de exploración con OpenSpec.