# Decisiones del laboratorio

## Modelos utilizados en OpenSpec

Para mantener consistencia durante el aprendizaje, se utilizarán los siguientes modelos por defecto:

| Etapa | Modelo |
|--------|---------|
| Explore | GPT 5.5 |
| Propose | GPT 5.5 |
| Apply | Codex 5.3 (o GPT 5.5 si se busca comparar resultados) |
| Sync | GPT 5.5 |
| Archive | GPT 5.5 |

> Esta configuración podrá revisarse durante el laboratorio si aparecen nuevos modelos o se detecta que alguno ofrece mejores resultados para una etapa específica.

Idioma del laboratorio: toda la interacción con OpenSpec se realizará en español. Los commits permanecerán en inglés siguiendo la convención habitual de Git. El código podrá utilizar nombres en inglés cuando resulte conveniente.


Decisión de arquitectura: La base de datos elegida para Smart Parking Platform será PostgreSQL, debido a la experiencia previa del desarrollador y porque representa una solución robusta para un entorno productivo.


# Sesión 002

## Estado

Se completó la fase de especificación del Ejercicio 001 utilizando OpenSpec.

Artefactos generados:

- Exercise
- Explore
- Review
- Proposal
- Design
- Tasks

Además se incorporó:

- AGENTS.md
- mejoras en la metodología del laboratorio.

## Próxima sesión

Comenzar la implementación mediante:

/opsx:apply

Antes de implementar se respetará el enfoque definido para el laboratorio:

Dominio → Persistencia → Servicio → API → Infraestructura → Tests.

