# AGENTS.md

# Reglas para Agentes de IA

Este repositorio desarrolla **Smart Parking Platform** como laboratorio de aprendizaje utilizando **Specification-Driven Development (SDD)**.

El objetivo no es únicamente desarrollar software funcional, sino también documentar y preservar todo el proceso de ingeniería.

---

# Principios generales

- La calidad del diseño tiene prioridad sobre la velocidad de implementación.
- El código debe reflejar las reglas del negocio, no las decisiones de infraestructura.
- Siempre privilegiar soluciones simples y fáciles de comprender.
- Evitar complejidad innecesaria.
- Explicar las decisiones cuando exista más de una alternativa razonable.

---

# Arquitectura

El proyecto sigue una arquitectura por capas.

```
Dominio
    ↓
Servicios de aplicación
    ↓
Persistencia
    ↓
API / Interfaces
```

Las reglas de negocio nunca deben depender de la base de datos, del framework ni de la interfaz de usuario.

---

# Base de datos

La base de datos oficial del proyecto es **PostgreSQL**.

No proponer SQLite u otra tecnología salvo que el ingeniero lo solicite explícitamente.

---

# Stack tecnológico

El lenguaje de programación oficial del proyecto es **Python**.

Las implementaciones deberán realizarse utilizando Python salvo que el ingeniero decida explícitamente otro lenguaje.

Cuando sea necesario proponer librerías o frameworks, priorizar el ecosistema Python.

No sugerir implementaciones en otros lenguajes a menos que exista una justificación técnica clara o una solicitud explícita del ingeniero.

---

# Tecnologías seleccionadas

Las tecnologías definidas actualmente para el proyecto son:

- Lenguaje: **Python**
- Base de datos: **PostgreSQL**
- Metodología: **Specification-Driven Development (OpenSpec)**
- Control de versiones: **Git + GitHub**

Estas decisiones constituyen la arquitectura base del proyecto y no deberán modificarse sin una decisión explícita del ingeniero.

---

# Idioma

Toda la documentación técnica debe escribirse en español.

Se permite mantener nombres técnicos en inglés cuando sean estándares de la industria.

Los mensajes de commit permanecerán en inglés.

---

# Specification-Driven Development

Seguir el flujo de OpenSpec:

```
Exercise
    ↓
Explore
    ↓
Review
    ↓
Propose
    ↓
Design
    ↓
Tasks
    ↓
Apply
    ↓
Retrospective
```

No omitir etapas.

---

# Conservación de documentación

Nunca eliminar documentación existente.

Nunca sobrescribir documentos previamente elaborados por el ingeniero.

Cuando una especificación evolucione:

- agregar nuevas secciones;
- crear nuevos documentos;
- registrar nuevas versiones;
- anexar información al final del documento cuando corresponda.

La trazabilidad completa del proyecto debe preservarse.

---

# Trazabilidad

Todo documento generado durante el desarrollo constituye evidencia del proceso de ingeniería.

Los documentos históricos forman parte del proyecto y deben conservarse.

---

# Alcance de los cambios

Implementar únicamente lo solicitado.

No agregar funcionalidades no especificadas.

Si se detecta una mejora posible:

- documentarla;
- proponerla;
- no implementarla automáticamente.

---

# Estilo de implementación

Priorizar:

- código legible;
- nombres descriptivos;
- funciones pequeñas;
- alta cohesión;
- bajo acoplamiento.

Evitar optimizaciones prematuras.

---

# Validaciones

Las reglas del negocio deben implementarse en el dominio o en los servicios de aplicación.

No depender exclusivamente de validaciones de la interfaz de usuario.

---

# Decisiones de arquitectura

Cuando existan varias alternativas razonables:

1. Explicar ventajas y desventajas.
2. Justificar la recomendación.
3. Esperar la decisión del ingeniero antes de modificar la arquitectura.

---

# Rol del agente

El agente actúa como asistente técnico.

Puede:

- analizar;
- proponer;
- diseñar;
- implementar;
- revisar código;
- detectar riesgos.

No debe tomar decisiones funcionales por cuenta propia.

La responsabilidad final sobre el diseño pertenece siempre al ingeniero.

---

Todo el código fuente (clases, funciones, atributos, variables y nombres de archivos) deberá escribirse en inglés. La documentación funcional y metodológica permanecerá en español.