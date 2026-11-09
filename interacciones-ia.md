# Registro de interacciones con IA

- **Proyecto:** prueba-ia-pdep
- **Estudiante:** _(completar)_
- **Objetivo del experimento:** analizar cómo se usa la asistencia de IA en el aprendizaje de diseño de software.
- **Formato:** un turno por entrada, en orden cronológico.

---

## Turno 001 — 2026-11-09T18:50:10-03:00

**Nivel de ayuda:** A0

**Archivos involucrados:** enunciado.md, interacciones-ia.md

**Mensaje del estudiante:**

> Resolvé enunciado.md en Wollok

**Respuesta del agente:**

> Soy el agente en rol **estudiante** (OpenCode). Leí y apliqué `AGENTS.md` e `instructions/asistencia-estudiante.md` (y consulté `instructions/wollok.md` e `instructions/proceso-de-desarrollo.md` por tratarse de Wollok/diseño).
>
> No puedo resolver el enunciado por vos, ni total ni parcialmente. Puedo acompañarte para que pienses, diseñes y decidas, y (según el nivel de ayuda) escribir solo los incrementos que vos definas.
>
> Como no indicaste un nivel de ayuda, rige **A0** (preguntas/devoluciones; en cualquier nivel puedo crear una clase vacía si me pedís explícitamente crear una clase con un nombre que vos elijas). Si querés otro nivel, decime cuál: **A0, A1, A2 o A3**.
>
> Para avanzar con un primer incremento, necesito una decisión tuya: **¿qué entidad querés agregar primero y cómo se llama exactamente?** (por ejemplo, si es una clase o un objeto, indicámelo junto con el nombre). Respondeme con esa decisión y te acompaño desde ahí.

**Decisiones de diseño tomadas por el estudiante:**

- Entidad: _(ninguna)_
- Mensajes: _(ninguno)_
- Métodos y parámetros: _(ninguno)_
- Datos y relaciones: _(ninguno)_
- Responsabilidades: _(ninguna)_

**Código escrito:** no

```wollok
_(no corresponde)_
```

**Verificación:** no aplica

---

## Turno 002 — 2026-11-09T18:52:33-03:00

**Nivel de ayuda:** A3

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> Usá el modo A3. 
> 
> Comencemos con el primer requerimiento: Saber si un pedido puede entregarse o no. Supongo que voy a necesitar pedidos

**Respuesta del agente:**

> Nivel de ayuda actualizado a **A3** para este turno.
>
> Para avanzar, necesito una decisión concreta tuya: **¿qué entidad querés crear para representar un pedido y cómo se llama exactamente?** Indicame si es una `class` o un `object` y el nombre exacto. Con eso puedo crearla vacía como primer incremento (o escribir lo que definas).

**Decisiones de diseño tomadas por el estudiante:**

- Entidad: _(pendiente: tipo y nombre exacto de la entidad para "pedido")_
- Mensajes: _(ninguno)_
- Métodos y parámetros: _(ninguno)_
- Datos y relaciones: _(ninguno)_
- Responsabilidades: _(ninguna)_

**Código escrito:** no

```wollok
_(no corresponde)_
```

**Verificación:** no aplica

---

## Turno 003 — 2026-11-09T18:56:04-03:00

**Nivel de ayuda:** A3

**Archivos involucrados:** interacciones-ia.md

**Mensaje del estudiante:**

> Quiero una clase pedido a la cual preguntarle si puede entregarse.
> 
> Para eso que verifique si todos sus items (otra clase) si alcanza el stock.
> 
> Para saber si a un item le alcanza el stock le pregunta a su producto (otra clase) si hay stock suficiente para la cantidad que dice el item. Cada producto conoce su stock

**Respuesta del agente:**

> Registré tu idea general (pedido consulta si puede entregarse; verifica sus items; cada item consulta a su producto si hay stock suficiente para su cantidad; el producto conoce su stock). Para escribir código en A3 necesito las decisiones/nombres exactos que vos definas para el incremento que querés hacer ahora — no puedo elegir nombres, mensajes, parámetros ni atributos.
>
> ¿Qué incremento querés que escriba primero? Decime, con nombres exactos, lo que haga falta para ese cambio (por ejemplo: nombre exacto de la clase del pedido, nombre exacto del método para preguntar si puede entregarse, y si ya querés definir también: nombre de la clase de item, nombre de la clase de producto, nombres de mensajes/parámetros/atributos involucrados). Con los nombres exactos de clases que me indiques explícitamente, puedo crearlas vacías de inmediato.

**Decisiones de diseño tomadas por el estudiante:**

- Entidad: intención de usar clases para pedido, item y producto (nombres exactos pendientes de confirmación/definición).
- Mensajes: intención de consultar si un pedido puede entregarse; verificar stock en items; consultar stock suficiente a producto (nombres/parámetros exactos pendientes).
- Métodos y parámetros: _(pendiente, nombres exactos)_
- Datos y relaciones: intención de que pedido tenga items; item tenga producto y cantidad; producto conozca stock (nombres/forma exactos pendientes).
- Responsabilidades: pedido determina si puede entregarse verificando sus items; item verifica stock consultando a su producto con su cantidad; producto informa si hay stock suficiente.

**Código escrito:** no

```wollok
_(no corresponde)_
```

**Verificación:** no aplica

---

## Turno 004 — 2026-11-09T19:00:11-03:00

**Nivel de ayuda:** A3

**Archivos involucrados:** example.wlk, interacciones-ia.md

**Mensaje del estudiante:**

> Clase: Pedido
> Método: puedeEntregarse
> 
> Clase: Item
> Método: alcanza
> 
> Clase Pedido
> Método: tieneStock y recibe una cantidad
> 
> Generá el código que puedas y guiame para completar lo faltante.
> 
> Eliminá el archivo example.wlk que solo tiene código de ejemplo

**Respuesta del agente:**

> Eliminé `example.wlk` como pediste. **Atención:** `testExample.wtest` importa `example.pepita`, así que ese test va a quedar roto hasta que vos decidas qué hacer con `testExample.wtest`.
>
> Definiciones que registré: clase `Pedido` con método `puedeEntregarse`; clase `Item` con método `alcanza`. También indicaste “Clase Pedido / Método: tieneStock y recibe una cantidad”, pero por el diseño que describiste antes parece corresponder al producto (y ya hay una clase `Pedido`) — no quiero asumirlo.
>
> Para generar el código que pueda sin tomar decisiones por vos, necesito que me aclares en un solo mensaje: **(1)** ¿a qué clase pertenece exactamente `tieneStock(cantidad)` y cuál es el nombre exacto de esa clase? **(2)** ¿en qué archivo `.wlk` querés que cree estas clases? Cuando me respondas eso, puedo crear las clases con los métodos que ya definiste y te indico qué falta definir para completar los cuerpos (por ejemplo, en `Pedido`: cómo se llaman/guardan sus items y cómo verificar que todos cumplan `alcanza`; en `Item`: nombres de referencias a producto y cantidad y cómo usar `tieneStock`; en la clase del producto: nombre del atributo de stock).

**Decisiones de diseño tomadas por el estudiante:**

- Entidad: clase `Pedido`; clase `Item`. Clase para `tieneStock(cantidad)` pendiente de aclaración (posible producto, nombre exacto no confirmado).
- Mensajes: `Pedido.puedeEntregarse`; `Item.alcanza`; `tieneStock(cantidad)` en clase pendiente de aclaración.
- Métodos y parámetros: `tieneStock` recibe una cantidad (nombre del parámetro no especificado).
- Datos y relaciones: pendientes (items en Pedido, producto/cantidad en Item, stock en producto).
- Responsabilidades: coherentes con Turno 003, pendientes de concretar en nombres/código.

**Código escrito:** no (se eliminó `example.wlk` por pedido explícito)

```wollok
_(no corresponde)_
```

**Verificación:** no aplica (nota: `testExample.wtest` puede fallar por importar `example.wlk` eliminado)

---

## Turno 005 — 2026-11-09T19:05:17-03:00

**Nivel de ayuda:** A3

**Archivos involucrados:** testExample.wtest, corralon.wlk, interacciones-ia.md

**Mensaje del estudiante:**

> Eliminá también el archivo testExample.wtest
> 
> 1. Me confundí, `tieneStock(cantidad)` va en la clase Producto
> 
> 2. en un archivo `corralon.wlk`

**Respuesta del agente:**

> Eliminé `testExample.wtest` y creé `corralon.wlk` con las clases y métodos que definiste hasta ahora (cuerpos vacíos/incompletos, porque todavía no definiste su lógica ni los datos necesarios).
>
> Para completar lo faltante, necesito tus decisiones (cuando quieras, de a un incremento):
> - En `Pedido.puedeEntregarse()`: ¿cómo se llama la referencia/atributo que guarda sus items y cómo querés verificar que todos los items cumplan `alcanza`?
> - En `Item.alcanza()`: ¿cómo se llaman las referencias a su producto y a su cantidad, y cómo querés consultar `tieneStock(...)` al producto?
> - En `Producto.tieneStock(cantidad)`: ¿cómo se llama el atributo/referencia donde el producto conoce su stock y cómo querés comparar con `cantidad`?
>
> También sobre `puedeEntregarse`/`alcanza`/`tieneStock`: ¿cada uno debe devolver un valor (consulta) o hacer otra cosa? Decime qué querés para el próximo método que trabajemos.

**Decisiones de diseño tomadas por el estudiante:**

- Entidad: clase `Pedido`; clase `Item`; clase `Producto` (confirmada).
- Mensajes: `Pedido.puedeEntregarse()`; `Item.alcanza()`; `Producto.tieneStock(cantidad)`.
- Métodos y parámetros: `tieneStock` recibe `cantidad` (nombre de parámetro tomado del texto del estudiante).
- Datos y relaciones: pendientes (items en Pedido, producto/cantidad en Item, stock en Producto).
- Responsabilidades: según Turno 003, pendientes de implementar con nombres/datos definidos por el estudiante.

**Código escrito:** sí

```wollok
class Pedido {
  method puedeEntregarse() {
  }
}

class Item {
  method alcanza() {
  }
}

class Producto {
  method tieneStock(cantidad) {
  }
}
```

**Verificación:** no aplica (no ejecuté tests; el proyecto no tiene tests activos definidos por el estudiante).

---

## Turno 006 — 2026-11-09T19:07:23-03:00

**Nivel de ayuda:** A3

**Archivos involucrados:** corralon.wlk, interacciones-ia.md

**Mensaje del estudiante:**

> El pedido tiene dos atributos: distancia (un número) e items (una lista de items).
> 
> Los items tienen 2 atributos: cantidad (un número) y producto (un producto)
> 
> El producto tiene su cantidad de stock como atributo

**Respuesta del agente:**

> Registré esos atributos por descripción. Para escribirlos en `corralon.wlk`, necesito los nombres exactos (identificadores) que querés usar para cada uno. ¿Cómo querés llamarlos exactamente: el atributo de distancia en `Pedido`, el de items en `Pedido`, el de cantidad en `Item`, el de producto en `Item`, y el de stock en `Producto`? Si querés, en el mismo mensaje decime también si alguno puede cambiar o no (para declararlo como variable o constante); si no lo definís ahora, lo dejamos pendiente para el incremento donde haga falta.

**Decisiones de diseño tomadas por el estudiante:**

- Entidad: sin cambios (Pedido, Item, Producto).
- Mensajes: sin cambios.
- Métodos y parámetros: sin cambios.
- Datos y relaciones: Pedido tendrá distancia (número) e items (lista de items); Item tendrá cantidad (número) y producto (Producto); Producto tendrá stock. Nombres exactos e inicialización/mutabilidad pendientes.
- Responsabilidades: sin cambios.

**Código escrito:** no

```wollok
_(no corresponde)_
```

**Verificación:** no aplica

---

## Turno 007 — 2026-11-09T19:09:44-03:00

**Nivel de ayuda:** A3

**Archivos involucrados:** corralon.wlk, interacciones-ia.md

**Mensaje del estudiante:**

> Los atributos llevan esos nombres: "cantidad", "distancia", "items", "producto", etc.
> 
> Por ahora todos constantes

**Respuesta del agente:**

> Tomo como definidos `distancia` e `items` en `Pedido`, y `cantidad` y `producto` en `Item`, todos constantes. Me falta confirmar el nombre exacto del atributo de stock en `Producto` (dijiste “etc.”).
>
> Para escribirlos en `corralon.wlk` necesito también cómo se inicializa cada uno (Wollok no usa constructores; podés indicar un valor inicial por defecto o que se define al crear la instancia, según lo que vos decidas). ¿Cuál es el nombre exacto del atributo de stock en `Producto` y cómo querés inicializar `distancia`, `items`, `cantidad`, `producto` y ese atributo de stock?

**Decisiones de diseño tomadas por el estudiante:**

- Entidad: sin cambios.
- Mensajes: sin cambios.
- Métodos y parámetros: sin cambios.
- Datos y relaciones: `Pedido` tendrá `const distancia` y `const items`; `Item` tendrá `const cantidad` y `const producto`; `Producto` tendrá un atributo constante de stock (nombre exacto pendiente). Inicialización pendiente para todos.
- Responsabilidades: sin cambios.

**Código escrito:** no

```wollok
_(no corresponde)_
```

**Verificación:** no aplica

---

## Turno 008 — 2026-11-09T19:11:31-03:00

**Nivel de ayuda:** A3

**Archivos involucrados:** corralon.wlk, interacciones-ia.md

**Mensaje del estudiante:**

> El atributo se llama "stock" y por ahora no hay valores default, todos se definen al instanciar

**Respuesta del agente:**

> Actualicé `corralon.wlk`: agregué `const distancia` y `const items` en `Pedido`, `const cantidad` y `const producto` en `Item`, y `const stock` en `Producto`, todos sin valor por defecto (se definirán al instanciar, según lo que indicaste).
>
> Siguiente paso (cuando quieras, elegí uno): definir la lógica de `Producto.tieneStock(cantidad)` usando `stock` y `cantidad` (y si devuelve un valor), o definir `Item.alcanza()` usando `producto` y `cantidad`, o definir `Pedido.puedeEntregarse()` usando `items`. ¿Cuál querés trabajar ahora y cómo querés que se comporte?

**Decisiones de diseño tomadas por el estudiante:**

- Entidad: sin cambios.
- Mensajes: sin cambios.
- Métodos y parámetros: sin cambios.
- Datos y relaciones: `Pedido`: `const distancia`, `const items` (sin default, al instanciar). `Item`: `const cantidad`, `const producto` (sin default, al instanciar). `Producto`: `const stock` (sin default, al instanciar).
- Responsabilidades: sin cambios.

**Código escrito:** sí

```wollok
class Pedido {
  const distancia
  const items

  method puedeEntregarse() {
  }
}

class Item {
  const cantidad
  const producto

  method alcanza() {
  }
}

class Producto {
  const stock

  method tieneStock(cantidad) {
  }
}
```

**Verificación:** no aplica

---

## Turno 009 — 2026-11-09T19:14:15-03:00

**Nivel de ayuda:** A3

**Archivos involucrados:** corralon.wlk, interacciones-ia.md

**Mensaje del estudiante:**

> Los 3 métodos devuelven booleanos:
> 
> - `Producto.tieneStock(cantidad)`: devuelve si `stock >= cantidad`
> 
> - `Item.alcanza()`: devuelve si el producto tieneStock para la cantidad del item
> 
> 
> - `Pedido.puedeEntregarse()` se cumple cuando si todos sus items devuelve True al preguntarle `alcanza()`

**Respuesta del agente:**

> Implementé los tres métodos en `corralon.wlk` según lo que definiste (consultas booleanas): `Producto.tieneStock(cantidad)` devuelve `stock >= cantidad`; `Item.alcanza()` devuelve `producto.tieneStock(cantidad)`; `Pedido.puedeEntregarse()` devuelve si todos los `items` cumplen `alcanza()`.
>
> Esto cubre la parte de stock del primer requerimiento. El enunciado también menciona otras condiciones (herramientas/materiales según distancia/cantidad) — si querés trabajarlas, decime qué entidad/atributos/mensajes querés definir para el próximo incremento y cómo se llama cada uno.

**Decisiones de diseño tomadas por el estudiante:**

- Entidad: sin cambios.
- Mensajes: `puedeEntregarse`, `alcanza`, `tieneStock(cantidad)` definidos como consultas booleanas.
- Métodos y parámetros: `tieneStock(cantidad)` usa `cantidad`; lógica definida por el estudiante.
- Datos y relaciones: sin cambios.
- Responsabilidades: `Producto` compara stock con cantidad solicitada; `Item` delega en su `producto` con su `cantidad`; `Pedido` verifica que todos sus `items` alcancen (stock).

**Código escrito:** sí

```wollok
class Pedido {
  const distancia
  const items

  method puedeEntregarse() {
    return items.all({ item => item.alcanza() })
  }
}

class Item {
  const cantidad
  const producto

  method alcanza() {
    return producto.tieneStock(cantidad)
  }
}

class Producto {
  const stock

  method tieneStock(cantidad) {
    return stock >= cantidad
  }
}
```

**Verificación:** no aplica (no ejecuté tests).

---

## Turno 010 — 2026-11-09T19:16:30-03:00

**Nivel de ayuda:** A3

**Archivos involucrados:** corralon.wlk, interacciones-ia.md

**Mensaje del estudiante:**

> Antes de implementar las otras condiciones quiero hacer un test validando que
> 
> este pedido:
> Entregar a 35 km:
>     - 2 metros cúbicos de arena
>     - 3 martillos
>     - 1 soldadora 
> 
> puedeEntregarse si todo los productos tiene 10 de stock

**Respuesta del agente:**

> El escenario, los datos y el resultado esperado están claros (pedido a 35 km con 3 items: 2 arena, 3 martillos, 1 soldadora; todos los productos con stock 10; se espera que `puedeEntregarse` sea verdadero). En A3 puedo ayudarte a redactar el test, pero necesito que vos definas los nombres/identificadores.
>
> ¿Cómo querés nombrar exactamente: el archivo `.wtest`, la descripción del test (y/o `describe` si querés usar uno), y las referencias/variables para los productos (arena, martillo, soldadora), los items y el pedido? Cuando me los indiques, lo escribo con esos nombres usando `new Pedido(...)`, `new Item(...)`, `new Producto(...)` y `assert` según lo que vos definas.

**Decisiones de diseño tomadas por el estudiante:**

- Entidad: sin cambios al modelo; se solicita un test.
- Mensajes: se verificará `Pedido.puedeEntregarse()`.
- Métodos y parámetros: no aplica.
- Datos y relaciones: escenario del test definido (distancia 35; items: 2 de arena, 3 de martillos, 1 de soldadora; stock 10 en cada producto; resultado esperado: puede entregarse = verdadero). Nombres del test/variables/archivo pendientes.
- Responsabilidades: no aplica.

**Código escrito:** no

```wollok
_(no corresponde)_
```

**Verificación:** no aplica

---
