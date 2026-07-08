# SDD Lab

Laboratorio personal para aprender **Specification-Driven Development (SDD)** utilizando **OpenSpec**, **Cursor** y asistentes de IA.

El objetivo de este repositorio no es únicamente desarrollar software, sino construir una metodología de trabajo profesional que combine análisis funcional, especificaciones, desarrollo asistido por IA y buenas prácticas de ingeniería.

---

# Filosofía de trabajo

> **La IA acelera mi desarrollo, pero la responsabilidad del análisis, las decisiones de diseño, la calidad del software y el resultado final siguen siendo mías.**

---

# Metodología de trabajo

## Fase 1 – Análisis 

Antes de utilizar cualquier herramienta de IA realizo el análisis funcional de la necesidad.

### 1. Analizo el problema

Comprendo qué necesidad se intenta resolver y cuál es el contexto del negocio.

---

### 2. Identifico el origen del requisito

El requisito puede surgir de distintas fuentes:

- Idea del producto.
- Necesidad de un usuario.
- Investigación.
- Cambio normativo.
- Mejora técnica.
- Otro.

**Observaciones**

Documento brevemente por qué este requisito existe.

---

### 3. Defino el contexto

Describo el escenario donde aparece la necesidad.

---

### 4. Defino el objetivo

Especifico qué se pretende lograr con esta funcionalidad.

---

### 5. Escribo la Historia de Usuario

Formato:

> Como **<rol>**, quiero **<funcionalidad>** para **<beneficio>**.

---

### 6. Defino las precondiciones (si existen)

Documento qué debe cumplirse antes de ejecutar la funcionalidad.

Ejemplos:

- El usuario debe haber iniciado sesión.
- Debe existir una cuenta activa.
- El vehículo debe estar registrado previamente.

Si la funcionalidad no tiene precondiciones, este paso se omite.

---

### 7. Defino los criterios de aceptación

Documento las condiciones que deben cumplirse para considerar terminada la funcionalidad.

---

### 8. Documento las decisiones de diseño

Registro las decisiones funcionales importantes y su justificación.

Ejemplos:

- Por qué un campo es obligatorio.
- Restricciones del negocio.
- Reglas de validación.
- Justificación de las decisiones adoptadas.

---

# Fase 2 – Especificación asistida por IA (OpenSpec)

Una vez finalizado el análisis funcional utilizo OpenSpec para transformar los requisitos en una especificación técnica.

La IA me ayuda a:

- Explorar el problema.
- Detectar requisitos faltantes.
- Detectar inconsistencias.
- Identificar casos borde.
- Elaborar la especificación funcional.
- Elaborar el diseño técnico.
- Dividir el trabajo en tareas.
- Mantener sincronizadas las especificaciones.
- Generar una implementación inicial cuando corresponda.

Todo el contenido generado es revisado antes de continuar.

---

# Fase 3 – Implementación

Durante esta etapa:

- Reviso la implementación propuesta.
- Realizo los ajustes necesarios.
- Escribo o adapto las pruebas.
- Verifico el cumplimiento de todos los criterios de aceptación.
- Realizo el commit correspondiente.

---

# Fase 4 – Retrospectiva

Al finalizar cada funcionalidad documento brevemente:

- ¿Qué aprendí?
- ¿Qué hizo OpenSpec?
- ¿Qué decisiones tomé yo?
- ¿Qué corregí sobre la propuesta de la IA?
- ¿Qué haría distinto la próxima vez?

---

# Principios del laboratorio

- El análisis funcional lo realizo yo.
- Las decisiones de negocio las tomo yo.
- La IA me ayuda a explorar, diseñar e implementar.
- Toda propuesta generada por IA debe ser revisada.
- Todo aprendizaje debe quedar documentado.
- Cada funcionalidad debe ser trazable desde su origen hasta su implementación.

---

# Regla N.º 1 del laboratorio: 

Antes de ejecutar un comando que modifique el estado del proyecto mediante OpenSpec (explore, propose, apply, etc.), realizar un commit de todo el trabajo previo.


# Regla N° 2 del Laboratorio:

## Conservación de la documentación

OpenSpec nunca debe sobrescribir documentación previamente elaborada por el ingeniero.

Cuando una especificación evolucione deberá:

- agregar nuevas secciones;
- crear nuevos documentos;
- registrar revisiones;
- anexar información al final del documento;

pero nunca reemplazar ni eliminar contenido existente, salvo que el ingeniero lo solicite explícitamente.

El objetivo es preservar la trazabilidad completa de las decisiones tomadas durante el proceso de desarrollo.


# Regla N° 3 del Laboratorio:

## Principio de trazabilidad
Todo artefacto generado durante el proceso de SDD constituye evidencia del proceso de ingeniería.

Ningún documento se elimina.

Ningún documento se sobrescribe.

Las decisiones evolucionan mediante nuevos artefactos o nuevas versiones, manteniendo siempre el historial completo del proyecto.
