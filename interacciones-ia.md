# Registro de interacciones con IA

- **Proyecto:** prueba-ia-pdep
- **Estudiante:** _(completar)_
- **Objetivo del experimento:** analizar cómo se usa la asistencia de IA en el aprendizaje de diseño de software.
- **Formato:** un turno por entrada, en orden cronológico.

---

## Turno 001 — 2026-10-29T00:25:51-03:00

**Nivel de ayuda:** A0

**Archivos involucrados:** enunciado.md, interacciones-ia.md

**Mensaje del estudiante:**

> Resolveme el enunciado

**Respuesta del agente:**

> No puedo resolver el enunciado por vos: eso sería diseñar la solución y las reglas del repo lo prohíben. Sí puedo acompañarte a pensarlo.
>
> Estoy en nivel A0 (solo preguntas) salvo que me indiques otro. Para arrancar, contame vos:
>
> 1. ¿Qué conceptos del dominio querés modelar y cómo se llama exactamente cada uno (objetos, clases)? ¿Por qué cada uno es objeto o clase?
> 2. ¿Qué mensajes debe entender cada uno y qué método implementa cada mensaje?
> 3. ¿Qué parámetros recibe cada método y qué representa?
> 4. ¿Qué datos guarda cada objeto y cómo se inicializan?
> 5. ¿Cómo se relacionan entre sí (quién conoce a quién, quién contiene a quién)?
> 6. ¿Qué responsabilidad tiene cada objeto?
> 7. ¿Qué casos de prueba definís, con qué datos y qué resultado esperás?
>
> Cuando tengas esas definiciones, las repito con tus nombres y, si las confirmás, escribo exactamente eso.

**Decisiones de diseño tomadas por el estudiante:**

- Ninguna todavía.

**Código escrito:** no

**Verificación:** no aplica

---

## Turno 002 — 2026-10-29T00:26:28-03:00

**Nivel de ayuda:** A3

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> a3

**Respuesta del agente:**

> Nivel A3 activado: puedo transcribir literalmente lo que me dictes, nada más. A3 no me habilita a diseñar, elegir nombres, completar ni corregir por vos.
>
> Para empezar necesito que me dictes exactamente: qué concepto querés definir (objeto o clase y nombre exacto), qué mensajes entiende, qué métodos y parámetros tiene cada uno, qué datos guarda y cómo se inicializa, con qué objetos se relaciona, qué responsabilidad tiene y qué casos de prueba esperás.
>
> Dictame el primero y lo transcribo tal cual, sin agregar nada.

**Decisiones de diseño tomadas por el estudiante:**

- Ninguna todavía.

**Código escrito:** no

**Verificación:** no aplica

---

## Turno 003 — 2026-10-29T00:29:17-03:00

**Nivel de ayuda:** A3

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> Vamos a crear la clase pedido y la clase producto. El pedido tiene una distancia y una coleccion de items. Item es una clase. Un Item tiene un producto y una cantidad, ambos atributos. Arranquemos con eso.

**Respuesta del agente:**

> Repito lo que definiste, con tus nombres:
>
> - Clase `Pedido` con atributos `distancia` y una colección de items.
> - Clase `Producto`.
> - Clase `Item` con atributos `producto` y `cantidad`.
>
> Para poder transcribir sin decidir nada, me faltan estos datos:
>
> 1. ¿Cómo se llama exactamente el atributo de la colección de items en `Pedido`?
> 2. ¿Cómo se inicializan `Pedido` e `Item`? ¿Constructor con parámetros? ¿Cuáles son sus nombres exactos y en qué orden?
> 3. ¿Qué datos guarda `Producto` y cómo se inicializa? ¿O por ahora queda sin atributos ni constructor?
> 4. ¿`distancia` y `cantidad` son numéricos?
> 5. ¿En qué archivo querés que escriba estas clases?
>
> Cuando me respondas eso, repito la lista completa y te pido confirmación antes de escribir.

**Decisiones de diseño tomadas por el estudiante:**

- Concepto: clase `Pedido`.
- Concepto: clase `Producto`.
- Concepto: clase `Item`.
- Datos: `Pedido` tiene `distancia` y una colección de items (nombre exacto pendiente).
- Datos: `Item` tiene `producto` y `cantidad`.
- Mensajes, métodos y parámetros: pendientes de definir.
- Relaciones: `Pedido` contiene items; `Item` referencia un producto y una cantidad.
- Responsabilidades: pendientes de definir.

**Código escrito:** no

**Verificación:** no aplica

---
