# Registro de interacciones con IA

- **Proyecto:** prueba-ia-pdep
- **Estudiante:** _(completar)_
- **Objetivo del experimento:** analizar cómo se usa la asistencia de IA en el aprendizaje de diseño de software.
- **Formato:** un turno por entrada, en orden cronológico.

---

## Turno 001 — 2026-11-09T17:25:12-03:00

**Nivel de ayuda:** A0

**Archivos involucrados:** enunciado.md, interacciones-ia.md

**Mensaje del estudiante:**

> Quiero resolver el enunciado. Nivel A0.

**Respuesta del agente:**

> Estamos en nivel **A0**: solo te hago preguntas, repreguntas y devoluciones sobre lo que vos definas; no propongo nombres, conceptos ni diseño.
>
> Para arrancar, contame:
>
> 1. ¿Qué conceptos del enunciado reconocés como candidatos a objeto o clase, y cómo se llama **exactamente** cada uno (con el identificador que querés usar)?
> 2. Para cada uno: ¿qué responsabilidad tiene y qué mensajes debería entender?
> 3. ¿Por cuál de los requerimientos querés empezar y qué situación concreta querés poder resolver primero?
>
> No hace falta que respondas todo junto: empezá por los conceptos y sus nombres, con tus palabras.

**Decisiones de diseño tomadas por el estudiante:**

- Ninguna todavía.

**Código escrito:** no

```wollok
_(sin código)_
```

**Verificación:** no aplica

---

## Turno 002 — 2026-11-09T17:26:09-03:00

**Nivel de ayuda:** A0

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> Me parece que hay pedidos, productos e ítems. Los llamaría Pedido, Producto e Item. Quiero empezar por saber si un pedido se puede entregar; por ahora no tengo claro qué le corresponde hacer a cada uno.

**Respuesta del agente:**

> Registro lo que definiste hasta ahora: los conceptos se llaman **Pedido**, **Producto** e **Item**, y querés empezar por saber si un pedido se puede entregar.
>
> Para avanzar sin decidir por vos, necesito que definas:
>
> 1. ¿Cada uno es una clase o un objeto? ¿Por qué?
> 2. ¿Qué representa cada uno con tus palabras y qué responsabilidad tiene?
> 3. Para responder si un pedido se puede entregar: ¿qué mensaje querés enviar, a quién se lo enviarías y qué debería devolver?
> 4. ¿Qué información necesita tener cada concepto para cumplir esa responsabilidad?
> 5. ¿Cómo se relacionan Pedido con Item, y Item con Producto?
>
> Empezá por lo que tengas más claro; lo que no, lo dejamos para después.

**Decisiones de diseño tomadas por el estudiante:**

- Conceptos: `Pedido`, `Producto` e `Item` (nombres definidos; tipo todavía no definido).
- Requerimiento elegido: saber si un pedido se puede entregar.
- Mensajes, métodos, datos, relaciones y responsabilidades: pendientes de definir.

**Código escrito:** no

```wollok
_(sin código)_
```

**Verificación:** no aplica

---

## Turno 003 — 2026-11-09T17:27:16-03:00

**Nivel de ayuda:** A0

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> Los haría clases, porque puede haber varios pedidos, productos e ítems distintos. Un Pedido reúne lo que se quiere entregar y debería saber si puede entregarse. Un Item relaciona un producto con la cantidad pedida. Producto representa lo que vende el corralón y conoce su stock. Lo de los mensajes todavía no lo tengo claro.

**Respuesta del agente:**

> Registro lo que definiste: `Pedido`, `Producto` e `Item` son clases. Un `Pedido` reúne lo que se quiere entregar y debe saber si puede entregarse; un `Item` relaciona un producto con la cantidad pedida; un `Producto` representa lo que vende el corralón y conoce su stock.
>
> Para definir los mensajes, contame:
>
> 1. ¿Qué mensaje exacto querés enviarle a un `Pedido` para preguntarle si se puede entregar, y qué debería devolver?
> 2. ¿Qué necesita saber el `Pedido` de cada `Item` para responder eso, y qué mensaje exacto le enviaría a un `Item`?
> 3. ¿Qué necesita saber un `Item` de su `Producto` para responder, y qué mensaje exacto le enviaría?
> 4. ¿Cómo guarda el `Pedido` sus items? ¿Cómo guarda el `Item` su producto y su cantidad? ¿Cómo se inicializan?
> 5. Además del stock, ¿qué otras condiciones del enunciado influyen en si un pedido puede entregarse, y en qué clase las ubicarías?
>
> No hace falta que definas todo junto: empezá por el mensaje del `Pedido` y seguimos desde ahí.

**Decisiones de diseño tomadas por el estudiante:**

- Conceptos: `Pedido`, `Producto` e `Item` son clases.
- Responsabilidades: `Pedido` reúne lo que se quiere entregar y sabe si puede entregarse; `Item` relaciona un producto con la cantidad pedida; `Producto` representa lo que vende el corralón y conoce su stock.
- Mensajes, métodos, datos, relaciones e inicialización: pendientes de definir.

**Código escrito:** no

```wollok
_(sin código)_
```

**Verificación:** no aplica

---

## Turno 004 — 2026-11-09T17:28:10-03:00

**Nivel de ayuda:** A0

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> Al Pedido le preguntaría puedeEntregarse. Quiero que responda verdadero si se pueden entregar todos sus ítems, y falso si alguno no se puede entregar.

**Respuesta del agente:**

> Registro: el `Pedido` entiende `puedeEntregarse` (sin parámetros) y devuelve verdadero si todos sus items pueden entregarse, falso si alguno no.
>
> Para seguir definiendo:
>
> 1. ¿Qué mensaje exacto le envía el `Pedido` a cada `Item` para saber si ese item puede entregarse? ¿Qué devuelve?
> 2. ¿Cómo guarda el `Pedido` sus items y cómo se inicializan?
> 3. Para que un `Item` responda si puede entregarse, ¿qué información necesita y a quién se la pide? ¿Qué mensaje exacto usa y qué devuelve?
> 4. ¿Cómo guarda el `Item` su producto y su cantidad? ¿Cómo se inicializan?
> 5. Además del stock, el enunciado menciona otras condiciones para poder entregar. ¿Cuáles son y en qué clase las ubicarías?

**Decisiones de diseño tomadas por el estudiante:**

- Mensaje `puedeEntregarse` en `Pedido`, sin parámetros; devuelve verdadero si todos sus items pueden entregarse y falso si alguno no.
- Mensajes entre `Pedido` e `Item`, datos, relaciones e inicialización: pendientes de definir.

**Código escrito:** no

```wollok
_(sin código)_
```

**Verificación:** no aplica

---

## Turno 005 — 2026-11-09T17:29:09-03:00

**Nivel de ayuda:** A0

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> A cada Item también le preguntaría puedeEntregarse, para que me conteste verdadero o falso por ese ítem. El Pedido guardaría sus ítems en una lista que se le pase al crearlo; no quiero que empiece siempre vacío.

**Respuesta del agente:**

> Registro: `Item` también entiende `puedeEntregarse` y devuelve verdadero o falso para ese item. El `Pedido` guarda sus items en una lista que recibe al crearse, y no empieza vacío.
>
> Para seguir:
>
> 1. ¿`puedeEntregarse` recibe algún parámetro en `Pedido` o en `Item`? Si sí, ¿cuál y qué representa?
> 2. Para que un `Item` responda `puedeEntregarse`, ¿qué información necesita y a quién se la pide? ¿Qué mensaje exacto le envía a su `Producto` y qué devuelve?
> 3. ¿Cómo guarda el `Item` su producto y su cantidad? ¿Cómo se inicializan?
> 4. Además del stock, el enunciado menciona otras condiciones para poder entregar. ¿Cuáles son, quién debería evaluarlas y qué información necesita cada una?
> 5. ¿Cómo recorre el `Pedido` su lista de items para responder `puedeEntregarse`?

**Decisiones de diseño tomadas por el estudiante:**

- Mensaje `puedeEntregarse` en `Item`, que devuelve verdadero o falso para ese item.
- `Pedido` guarda sus items en una lista recibida al crearse; no empieza vacío.
- Parámetros de `puedeEntregarse`, mensaje `Item`→`Producto`, datos e inicialización del `Item`, otras condiciones y recorrido de la lista: pendientes de definir.

**Código escrito:** no

```wollok
_(sin código)_
```

**Verificación:** no aplica

---

## Turno 006 — 2026-11-09T17:30:24-03:00

**Nivel de ayuda:** A0

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> Creo que al Pedido no tendría que pasarle nada, porque ya conoce sus ítems y la distancia. Al Item sí tendría que pasarle la distancia. El Item guardaría el producto y la cantidad, recibidos al crearlo, y le preguntaría al Producto si puede entregarse esa cantidad a esa distancia. A ese mensaje también lo llamaría puedeEntregarse.

**Respuesta del agente:**

> Registro: `Pedido.puedeEntregarse` no recibe parámetros y usa sus propios items y su distancia. `Item.puedeEntregarse(distancia)` recibe la distancia; el `Item` guarda el producto y la cantidad recibidos al crearse, y le pregunta a su `Producto` `puedeEntregarse` con la cantidad y la distancia.
>
> Para precisar lo que falta:
>
> 1. ¿El `Pedido` le pasa su distancia a cada `Item` al enviarle `puedeEntregarse`?
> 2. ¿Qué parámetros exactos recibe `puedeEntregarse` en `Producto` y cómo se llaman? ¿Qué devuelve?
> 3. ¿Qué condiciones evalúa el `Producto` para responder `puedeEntregarse`?
> 4. ¿Cómo guarda el `Producto` su stock y cómo se inicializa? ¿Es `var` o `const`?
> 5. ¿Cómo distingue un `Producto` si es herramienta o material? ¿Qué dato guarda y cómo se inicializa?
> 6. ¿Cómo guarda el `Pedido` su distancia y cómo se inicializa?

**Decisiones de diseño tomadas por el estudiante:**

- `Pedido.puedeEntregarse` sin parámetros; usa sus items y su distancia.
- `Item.puedeEntregarse(distancia)`; el `Item` guarda producto y cantidad recibidos al crearse.
- El `Item` le pregunta al `Producto` `puedeEntregarse` con cantidad y distancia.
- `Producto` también entiende `puedeEntregarse`.
- Firma exacta de `Producto.puedeEntregarse`, condiciones, stock, distinción herramienta/material e inicialización de distancia: pendientes de definir.

**Código escrito:** no

```wollok
_(sin código)_
```

**Verificación:** no aplica

---

## Turno 007 — 2026-11-09T17:31:15-03:00

**Nivel de ayuda:** A0

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> Sí, el Pedido le pasa su distancia a cada Item. En Producto los parámetros se llamarían cantidad y distancia, y devolvería verdadero o falso. Primero comprobaría que el stock alcance. Después habría que ver si es herramienta o material, pero no estoy seguro de cómo separar esos comportamientos.

**Respuesta del agente:**

> Registro: el `Pedido` le pasa su distancia a cada `Item`; `Producto.puedeEntregarse(cantidad, distancia)` devuelve verdadero o falso, primero controla el stock y después la condición de herramienta o material.
>
> Sobre cómo separar esos comportamientos, no puedo elegir el diseño por vos. Para pensarlo, contame:
>
> 1. ¿Qué condición exacta debe cumplir una herramienta para poder entregarse? ¿Y un material?
> 2. ¿Qué hace distinto cada uno? ¿Qué información necesita cada uno que el otro no necesita?
> 3. ¿Cómo querés que un `Producto` sepa si es herramienta o material? Proponé las alternativas que se te ocurran y las comparamos.
> 4. ¿Dónde te parece que debería vivir la decisión según el tipo, y por qué?
> 5. ¿Cómo guarda el `Producto` su stock y cómo se inicializa? ¿`var` o `const`?

**Decisiones de diseño tomadas por el estudiante:**

- El `Pedido` le pasa su distancia a cada `Item`.
- `Producto.puedeEntregarse(cantidad, distancia)` devuelve verdadero o falso.
- El `Producto` primero comprueba que el stock alcance; después evalúa la condición de herramienta o material.
- Condiciones exactas, separación de comportamientos, stock e inicialización: pendientes de definir.

**Código escrito:** no

```wollok
_(sin código)_
```

**Verificación:** no aplica

---

## Turno 008 — 2026-11-09T17:32:13-03:00

**Nivel de ayuda:** A0

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> Las herramientas tienen el límite de 50 km y los materiales el mínimo de 2 de cantidad. Se me ocurre hacer clases Herramienta y Material, para que cada una responda según su condición. El stock sería común a ambas. ¿Eso que estoy planteando se entiende o me falta definir algo?

**Respuesta del agente:**

> Se entiende la idea general: `Herramienta` y `Material` como clases, cada una con su condición, y un stock común. Pero para poder escribir código todavía faltan definiciones. Contame:
>
> 1. ¿`Herramienta` y `Material` heredan de `Producto`, o se relacionan de otra manera? ¿`Producto` sigue existiendo como clase?
> 2. ¿Qué mensaje implementa cada una? ¿Redefinen `puedeEntregarse(cantidad, distancia)` o usan otro nombre/firma?
> 3. ¿Dónde vive el control de stock y dónde la condición de cada tipo? ¿Cómo se combinan para devolver un solo verdadero o falso?
> 4. ¿Qué nombre exacto tiene el atributo del stock, cómo se inicializa y es `var` o `const`?
> 5. ¿`Herramienta` y `Material` tienen atributos propios además del stock?
>
> Con eso definido te repito todo y, si lo confirmás, recién ahí escribo.

**Decisiones de diseño tomadas por el estudiante:**

- Condición de `Herramienta`: distancia de hasta 50 km.
- Condición de `Material`: cantidad de 2 o más.
- `Herramienta` y `Material` serían clases; el stock sería común a ambas.
- Relación con `Producto`, mensajes/firmas, ubicación del control de stock, nombre e inicialización del stock y atributos propios: pendientes de definir.

**Código escrito:** no

```wollok
_(sin código)_
```

**Verificación:** no aplica

---

## Turno 009 — 2026-11-09T17:33:18-03:00

**Nivel de ayuda:** A0

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> Sí, Herramienta y Material heredan de Producto, que seguiría existiendo. Cada una respondería puedeEntregarse con la cantidad y la distancia: tiene que alcanzar el stock y además cumplirse su condición. El dato común se llamaría stock, se recibe al crear el producto y debe poder cambiar cuando se entrega. No sé cómo se expresa eso con var o const. Por ahora no les pondría otros datos propios.

**Respuesta del agente:**

> Registro: `Herramienta` y `Material` heredan de `Producto`, que sigue existiendo. Las dos entienden `puedeEntregarse(cantidad, distancia)` y responden verdadero solo si alcanza el `stock` y se cumple su condición. `stock` se recibe al crear el producto y debe poder cambiar al entregar. Sin otros datos propios por ahora.
>
> Sobre `var` o `const`: en A0 no te lo explico, pero te pregunto: si `stock` tiene que poder cambiar después de crear el producto, ¿qué diferencia ves entre `var` y `const`? ¿Cuál elegirías y por qué? Si querés que te explique el concepto, decime que pasamos a A1.
>
> Para terminar de definir lo necesario para escribir:
>
> 1. ¿`Producto` define algún método para el control de stock, o cada subclase repite ese control?
> 2. ¿Un `Producto` genérico puede crearse? Si sí, ¿qué debería responder a `puedeEntregarse`?
> 3. ¿Qué nombre exacto tienen los atributos del `Pedido` para la lista de items y la distancia? ¿Se reciben al crearlo?
> 4. ¿Qué nombre exacto tienen los atributos del `Item` para el producto y la cantidad? ¿Se reciben al crearlo?
> 5. ¿Qué caso de prueba querés usar para verificar el requerimiento? Definí el escenario, los datos y el resultado esperado.

**Decisiones de diseño tomadas por el estudiante:**

- `Herramienta` y `Material` heredan de `Producto`; `Producto` sigue existiendo.
- `Herramienta.puedeEntregarse(cantidad, distancia)` y `Material.puedeEntregarse(cantidad, distancia)`: stock suficiente y condición propia.
- Atributo común `stock`, recibido al crear el producto y mutable al entregar.
- Sin atributos propios adicionales por ahora.
- Ubicación del control de stock, instanciación de `Producto`, nombres de atributos de `Pedido` e `Item` y caso de prueba: pendientes de definir.

**Código escrito:** no

```wollok
_(sin código)_
```

**Verificación:** no aplica

---

## Turno 010 — 2026-11-09T17:34:44-03:00

**Nivel de ayuda:** A0

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> No tengo clara la diferencia entre var y const. Lo que quiero es que stock pueda cambiar, no que quede fijo. ¿No alcanza con que te diga eso para que escribas esa parte? Prefiero seguir con el nivel que elegí y resolverlo de a poco.

**Respuesta del agente:**

> Quedamos en A0. Lo que definiste —que `stock` pueda cambiar y no quede fijo— es una decisión de comportamiento, pero para escribirlo necesito que elijas la declaración exacta: `var` o `const`. No puedo elegirla por vos.
>
> Te lo pregunto de otra forma: si un atributo tiene que poder recibir un valor nuevo después de creado el objeto, ¿cuál de las dos opciones te parece que lo permite, y por qué?
>
> Además, para escribir el requerimiento todavía faltan las respuestas a las preguntas anteriores: dónde vive el control de stock, si `Producto` genérico puede crearse, los nombres exactos de los atributos de `Pedido` e `Item` y un caso de prueba. Podemos ir de a una.

**Decisiones de diseño tomadas por el estudiante:**

- `stock` debe poder cambiar después de creado el producto; no debe quedar fijo.
- Declaración exacta (`var` o `const`), ubicación del control de stock, instanciación de `Producto`, nombres de atributos de `Pedido` e `Item` y caso de prueba: pendientes de definir.

**Código escrito:** no

```wollok
_(sin código)_
```

**Verificación:** no aplica

---
