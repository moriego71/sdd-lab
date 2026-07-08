
Modo exploración — Ejercicio 001: Registrar un vehículo

Revisé el ejercicio, la metodología del lab y el estado del repo. No hay cambios OpenSpec activos ni código de aplicación todavía; esto es el primer módulo de Smart Parking. Buen punto de partida para SDD.

Lo que ya está sólido
Tu análisis funcional (Fase 1) está bien encaminado. Tienes:

Actor claro: conductor registrado
Dos propósitos distintos del dato (no es lo mismo):
Lógico → patente para identificación automática
Visual → marca, modelo, color para inspectores
Invariantes de dominio explícitas:
1 usuario → N vehículos
1 vehículo → 1 usuario
patente única en el sistema
Eso ya define un agregado bastante claro:

┌─────────────────────────────────────────────────────────┐
│              SMART PARKING — dominio inicial            │
└─────────────────────────────────────────────────────────┘
   ┌──────────┐         1:N          ┌──────────┐
   │  Usuario │◄─────────────────────│ Vehículo │
   │ (auth)   │                      │          │
   └──────────┘                      └──────────┘
        │                                  │
   precondición                      patente (única)
   del ejercicio                      marca, modelo, color
Hilos que merecen explorar
1. La patente: única, pero ¿con qué reglas?
Decidiste que la patente identifica unívocamente al vehículo. Falta definir cómo se valida:

Pregunta	Por qué importa
¿Formato argentino? (ej. AA 123 BB, ABC 123)
Afecta regex, normalización y mensajes de error
¿Mayúsculas/minúsculas? abc123 = ABC123
Si no normalizas, la unicidad falla en la práctica
¿Espacios y guiones? AA123BB vs AA 123 BB
Mismo vehículo, dos registros distintos
¿Patentes extranjeras o solo locales?
Scope del primer ejercicio
Caso borde típico:

Usuario A registra: "ABC 123"
Usuario B intenta:  "abc123"  → ¿error de duplicado o mismo registro?
Si no lo defines ahora, OpenSpec lo inferirá (y quizá mal).

2. Marca, modelo, color: obligatorios, pero ¿qué tan estructurados?
Para inspectores tiene sentido exigirlos. Lo abierto es el tipo de dato:

Opción A — texto libre          Opción B — catálogo
─────────────────────          ─────────────────────
marca: "Toyota"                marca: id → "Toyota"
modelo: "Corolla"              modelo: id → "Corolla" (por marca)
color: "Blanco"                color: id → "Blanco"
+ rápido para MVP              + consistente para inspectores
+ menos fricción               + más trabajo inicial
- "TOYOTA" / "toyota"          - requiere seed/admin
- "blanco perla" vs "Blanco"
Para el primer ejercicio del lab, texto libre encaja bien. Pero conviene decidir si normalizas (trim, capitalización) o aceptas tal cual.

Caso borde visual:

Dos vehículos del mismo usuario: Toyota Corolla Blanco + Toyota Corolla Blanco
La patente los distingue en el sistema.
¿Los inspectores tienen suficiente con marca/modelo/color, o necesitan algo más (año, foto)?

No hace falta resolverlo ahora; sí dejarlo explícito como fuera de alcance o decisión futura.

3. Precondiciones vs. realidad del repo
Las precondiciones dicen:

usuario autenticado
usuario registrado
Pero no existe módulo de auth todavía. Eso abre dos caminos:

Camino A — Auth primero (módulo 000)
────────────────────────────────────
  Login/Register → luego Vehicle Registration
  Más realista, más scope
Camino B — Auth simulado en este ejercicio
──────────────────────────────────────────
  "Usuario ya existe" como dato dado
  Stub/fixture de sesión
  Enfocado en aprender SDD + dominio Vehicle
Camino C — Auth mínimo embebido
───────────────────────────────
  Solo lo necesario para cumplir precondiciones
  User hardcodeado o seed en DB
Para un lab de SDD, B o C son razonables si el objetivo es aprender el flujo OpenSpec, no construir auth completo. Vale la pena decidirlo antes de /opsx:propose.

4. Alcance: ¿solo crear, o CRUD?
El ejercicio habla de registrar. No menciona:

listar mis vehículos
editar marca/modelo/color
eliminar o dar de baja
transferir vehículo a otro usuario
       ┌─────────────┐
       │  Registrar  │  ← explícito en el ejercicio
       └──────┬──────┘
              │
   ┌──────────┼──────────┐
   ▼          ▼          ▼
Listar     Editar     Eliminar
implícito?  ?          ?
Recomendación para SDD: mantener scope en "create" y documentar el resto como no-objetivos. OpenSpec tiende a expandir scope si no lo acotas.

5. Criterios de aceptación: del funcional al verificable
Algunos criterios son claros; otros necesitan precisión para specs y tests:

Criterio	Estado	Para especificar bien
Usuario puede registrar
✅ claro
Happy path
Campos obligatorios
✅ claro
¿vacío, solo espacios, null?
Patente única
✅ claro
Mensaje exacto al duplicar
Asociado al usuario
✅ claro
No se puede asignar a otro
Almacena en BD
⚠️ técnico
Mejor como consecuencia del diseño
Informa éxito
⚠️ vago
¿Qué ve el usuario? ¿Qué datos devuelve?
Error de validación con motivo
⚠️ vago
¿Por campo? ¿Código HTTP? ¿Formato?
Escenarios que faltan explícitos:

┌────────────────────────────────────────────────────────┐
│              MAPA DE ESCENARIOS (borrador)             │
├────────────────────────────────────────────────────────┤
│ ✓ Registro exitoso                                     │
│ ✗ Campo obligatorio faltante (cada uno)                │
│ ✗ Patente duplicada                                    │
│ ✗ Usuario no autenticado                               │
│ ? Patente con formato inválido                         │
│ ? Todos los campos vacíos                              │
│ ? Límite de caracteres excedido                        │
└────────────────────────────────────────────────────────┘
6. Flujo de la operación
Borrador del flujo que OpenSpec debería capturar:

Conductor autenticado
        │
        ▼
  Completa formulario
  (patente, marca, modelo, color)
        │
        ▼
   ┌─────────┐     no     ┌──────────────────┐
   │ ¿Campos │───────────►│ Error por campo  │
   │ válidos?│            │ (motivo claro)   │
   └────┬────┘            └──────────────────┘
        │ sí
        ▼
   ┌─────────┐     sí     ┌──────────────────┐
   │ ¿Patente│───────────►│ Error: patente   │
   │ existe? │            │ ya registrada    │
   └────┬────┘            └──────────────────┘
        │ no
        ▼
   Persistir vehículo
   vinculado al usuario
        │
        ▼
   Confirmar éxito
   (con datos del vehículo)
Riesgos si pasamos directo a propose sin cerrar esto
Auth fantasma — precondiciones sin módulo que las cumpla
Validación de patente ambigua — bugs de unicidad por normalización
Scope creep — listar/editar/eliminar colándose en la implementación
Criterio 5 demasiado técnico — mezcla funcional con infraestructura
Primer módulo = fundación — decisiones de entidades y API condicionan todo lo que sigue
Lo que ya podrías decidir (sin implementar)
Decisión	Opción razonable para el lab
Auth
Stub/seed: usuario fijo autenticado
Scope
Solo create; listar/editar fuera de alcance
Patente
Normalizar a mayúsculas, sin espacios
Formato patente
Validación básica o "cualquier string no vacío" en v1
Marca/modelo/color
Texto libre, trim, longitud máxima
Éxito
Mensaje + datos del vehículo creado
Error duplicado
"La patente ya está registrada"
Siguiente paso natural en OpenSpec
Cuando esto te cierre, el flujo sería:

/opsx:propose register-vehicle
Eso generaría algo como:

proposal.md — qué y por qué (desde tu exercise.md)
design.md — entidades, API, validaciones, decisión de auth stub
tasks.md — pasos de implementación
specs/vehicle-registration/spec.md — escenarios verificables
¿Por dónde seguimos?
Algunos hilos que puedo profundizar contigo:

Auth — ¿stub, mínimo embebido, o módulo previo?
Validación de patente — ¿formato argentino estricto o MVP permisivo?
API vs UI — ¿qué capa implementas primero en el lab?
Escenarios de error — armar la tabla completa de casos borde
Modelo de datos — entidades, relaciones, constraints
¿Cuál te interesa explorar primero? Si ya tenés decisiones en mente, las vamos cerrando y cuando esté listo pasamos a /opsx:propose register-vehicle.