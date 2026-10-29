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

## Turno 004 — 2026-10-29T00:32:12-03:00

**Nivel de ayuda:** A3

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> 1. items
> 2. No necesitamos constructoes, porque Wollok me los da automáticamente. Los parámetros de construcción son nombrados, no tiene sentido preguntar el orden.
> 3. Por ahora dejamos producto vacio, ya lo iremos completando.
> 4. No hace falta preguntar tipos porque Wollok no exige ese tipo de información para declarar atributos, es más interesante preguntar si es var o const.
> 5. Arranquemos poniendo todo en un único archivo llamado corralon.wlk.

**Respuesta del agente:**

> Repito tus decisiones, con tus nombres:
>
> - Archivo único: `corralon.wlk`.
> - Clase `Pedido` con parámetros nombrados `distancia` e `items`.
> - Clase `Item` con parámetros nombrados `producto` y `cantidad`.
> - Clase `Producto` vacía por ahora.
> - Sin constructores explícitos: los parámetros se declaran en la clase.
>
> Falta una sola definición tuya: ¿cada atributo es `var` o `const`?
>
> 1. `distancia`
> 2. `items`
> 3. `producto`
> 4. `cantidad`
>
> Decime `var` o `const` para cada uno. Con eso repito la lista final y te pido confirmación explícita antes de transcribir.

**Decisiones de diseño tomadas por el estudiante:**

- Concepto: clase `Pedido` con parámetros `distancia` e `items`.
- Concepto: clase `Item` con parámetros `producto` y `cantidad`.
- Concepto: clase `Producto`, vacía por ahora.
- Archivo: `corralon.wlk` (todo en un único archivo).
- Datos: sin constructores explícitos; parámetros nombrados.
- `var` / `const`: pendiente de definir para cada atributo.
- Mensajes, métodos y responsabilidades: pendientes de definir.

**Código escrito:** no

**Verificación:** no aplica

---

## Turno 005 — 2026-10-29T00:32:50-03:00

**Nivel de ayuda:** A3

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> todos const.

**Respuesta del agente:**

> Lista final de lo que voy a transcribir en `corralon.wlk`:
>
> ```wollok
> class Pedido(const distancia, const items)
>
> class Item(const producto, const cantidad)
>
> class Producto {}
> ```
>
> Nota: `const` impide reasignar el atributo, pero la colección `items` igual puede modificarse.
>
> ¿Confirmás que escriba exactamente eso, con esos nombres y esas responsabilidades, sin agregar nada más?

**Decisiones de diseño tomadas por el estudiante:**

- Archivo: `corralon.wlk`.
- Clase `Pedido` con `const distancia` y `const items`.
- Clase `Item` con `const producto` y `const cantidad`.
- Clase `Producto` vacía.
- Sin constructores explícitos.
- Mensajes, métodos y responsabilidades: pendientes de definir.

**Código escrito:** no (pendiente de confirmación explícita)

**Verificación:** no aplica

---

## Turno 006 — 2026-10-29T00:34:22-03:00

**Nivel de ayuda:** A3

**Archivos involucrados:** corralon.wlk, interacciones-ia.md

**Mensaje del estudiante:**

> Correcto

**Respuesta del agente:**

> Transcribí exactamente lo confirmado en `corralon.wlk`, pero no parsea. El error es:
>
> ```
> Failed to parse corralon.wlk:
> > 1 | class Pedido(const distancia, const items)
>     |             ^
> Expected one of the following:
> 'inherits', '{', whitespace
> ```
>
> La versión instalada es Wollok-TS v4.3.0. En esa versión los atributos se declaran dentro del cuerpo con `const property`, y la construcción es nombrada (`new Pedido(distancia = ..., items = ...)`).
>
> ¿Confirmás que reemplace el contenido por esta traducción sintáctica de lo que ya definiste, sin cambiar nombres ni responsabilidades?
>
> ```wollok
> class Pedido {
>   const property distancia
>   const property items
> }
>
> class Item {
>   const property producto
>   const property cantidad
> }
>
> class Producto {}
> ```

**Decisiones de diseño tomadas por el estudiante:**

- Archivo: `corralon.wlk`.
- Clase `Pedido` con `const distancia` y `const items`.
- Clase `Item` con `const producto` y `const cantidad`.
- Clase `Producto` vacía.
- Sin constructores explícitos; construcción nombrada.
- Mensajes, métodos y responsabilidades: pendientes de definir.

**Código escrito:** sí

```wollok
class Pedido(const distancia, const items)

class Item(const producto, const cantidad)

class Producto {}
```

**Verificación:** `wollok test` → falla el parseo de `corralon.wlk` (se esperaba `{`, `inherits` o whitespace). Sin corrección aplicada, pendiente de confirmación.

---
