# Decisión de Ingeniería 001

# Estrategia de especificación para los prompts de OpenSpec

## Estado

Aceptada.

---

## Contexto

Durante las primeras iteraciones del laboratorio (Apply 001 a Apply 003), cada prompt enviado a OpenSpec incluía tanto la especificación de la iteración como un conjunto importante de reglas permanentes:

- convenciones de idioma;
- reglas de arquitectura;
- formato de la documentación;
- restricciones generales;
- estructura de la respuesta;
- instrucciones para exportar Markdown.

Aunque este enfoque producía buenos resultados, generaba una importante duplicación de información entre iteraciones.

Además, al crecer el laboratorio, mantener sincronizadas esas reglas en todos los prompts aumentaría el costo de mantenimiento y el riesgo de inconsistencias.

---

## Decisión

A partir del Apply 004, las reglas permanentes del laboratorio se centralizan en `AGENTS.md`.

Los prompts de cada Apply deberán contener únicamente:

- el objetivo de la iteración;
- las tareas específicas a implementar;
- la referencia a los documentos de especificación correspondientes (`AGENTS.md`, `proposal.md`, `design.md` y `tasks.md`).

De esta manera, `AGENTS.md` pasa a constituir la fuente única de verdad para todas las reglas generales del laboratorio.

---

## Motivación

Esta decisión busca:

- eliminar duplicación de información;
- simplificar el mantenimiento de los prompts;
- mejorar la consistencia entre iteraciones;
- facilitar la evolución de las reglas metodológicas;
- mantener separadas las decisiones permanentes de las decisiones específicas de cada Apply.

---

## Relación con Specification-Driven Development

Esta decisión no modifica la filosofía de Specification-Driven Development.

Por el contrario, refuerza uno de sus principios fundamentales:

> Mantener una única fuente de verdad para las reglas permanentes del proyecto.

Las especificaciones continúan siendo completas; simplemente se evita repetir información que ya forma parte de la especificación base del laboratorio.

---

## Cambios incorporados en AGENTS.md

Se incorporan como reglas permanentes:

- granularidad de los Apply;
- objetivo de cada Apply;
- documentación generada;
- explicación previa a la implementación;
- evolución incremental de la arquitectura;
- criterio de calidad;
- principio de mínima implementación;
- convenciones de idioma.

---

## Impacto

A partir del Apply 004 los prompts serán significativamente más pequeños.

La reducción del tamaño del prompt no implica una pérdida de información, ya que todas las reglas generales permanecen definidas en `AGENTS.md`.

Esto mejora la mantenibilidad del laboratorio y reduce la duplicación de especificaciones.

---

## Consecuencias

### Positivas

- Menor duplicación.
- Mayor consistencia.
- Mantenimiento más sencillo.
- Mejor alineación con SDD.
- Evolución más controlada de las reglas metodológicas.

### Riesgos

La calidad de los prompts dependerá de mantener `AGENTS.md` actualizado.

Por ello, toda nueva regla permanente deberá incorporarse primero en `AGENTS.md` antes de comenzar nuevas iteraciones.

---

## Fecha

Julio de 2026.