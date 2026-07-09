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

## Convenciones de idioma

- Todo el código fuente (clases, funciones, métodos, atributos, variables, módulos, paquetes y nombres de archivos) deberá escribirse en **inglés**.
- Toda la documentación funcional, metodológica y de ingeniería deberá escribirse en **español**.
- Todos los mensajes dirigidos al usuario (mensajes de error, respuestas de la API, mensajes informativos, texto mostrado por consola para validación funcional, etc.) deberán escribirse en **español**.
- Los comentarios del código deberán escribirse en **español**, salvo que exista un motivo técnico para hacerlo en inglés.
- Nunca mezclar idiomas dentro de un mismo mensaje. Los identificadores internos permanecen en inglés y los textos visibles para el usuario en español.

### Ejemplos

**Correcto**

- Variable: `plate`
- Clase: `VehicleRepository`
- Método: `exists_by_plate()`
- Mensaje al usuario: `"La patente ya está registrada."`
- Respuesta HTTP: `"Autenticación requerida."`

**Incorrecto**

- `"Plate already exists."`
- `"Vehicle registered successfully."`
- `"Please enter brand."`

---

Toda decisión tomada durante el laboratorio tiene prioridad sobre las convenciones por defecto del modelo. Si existe una decisión documentada en AGENTS.md, el asistente deberá respetarla en todas las iteraciones siguientes, salvo instrucción explícita del ingeniero.

---

# Granularidad de las iteraciones

Cada Apply deberá implementar una única responsabilidad claramente identificable.

Las iteraciones deberán ser pequeñas, fácilmente revisables y con un impacto arquitectónico acotado.

Si una implementación requiere múltiples responsabilidades, deberá dividirse en varios Apply.

---

# Objetivo de cada Apply

Cada Apply deberá:

- implementar únicamente la tarea correspondiente;
- respetar todas las decisiones arquitectónicas vigentes;
- mantener el proyecto compilable;
- no introducir deuda técnica innecesaria;
- dejar preparada la siguiente iteración.

---

# Documentación generada

Cuando el agente produzca documentación del laboratorio deberá:

- generar un único documento Markdown;
- no dividir la respuesta en múltiples bloques;
- conservar el orden cronológico de la explicación;
- incluir únicamente el contenido solicitado;
- evitar agregar secciones no requeridas.

El documento deberá quedar listo para copiar y pegar en el repositorio del laboratorio.

---

# Antes de implementar

Antes de generar código el agente deberá explicar brevemente:

- qué archivos creará;
- qué archivos modificará;
- por qué son necesarios esos cambios.

La explicación debe ser breve y orientada al diseño.

---

# Evolución incremental

No implementar componentes futuros.

No crear clases "por las dudas".

No agregar interfaces, servicios o repositorios que todavía no hayan sido especificados.

La arquitectura debe evolucionar exclusivamente mediante nuevas especificaciones.

---

# Criterio de calidad

Antes de considerar finalizada una implementación, verificar que:

- respeta Clean Architecture;
- mantiene bajo acoplamiento;
- posee alta cohesión;
- no rompe decisiones anteriores;
- resulta fácil de comprender por un desarrollador nuevo.

---

# Principio de mínima implementación

Cuando existan varias implementaciones posibles que satisfagan la especificación, elegir la más simple.

No incorporar flexibilidad, extensibilidad o abstracciones adicionales hasta que una especificación futura las justifique.

---

