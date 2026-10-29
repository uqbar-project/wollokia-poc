# Resolución del enunciado del corralón en Wollok

## 1. Objetivo

Resolver el sistema de pedidos a domicilio del corralón **Armando Paredes** descripto en
`enunciado.md`, implementando los tres requerimientos y una suite de tests que cubra todos
los escenarios mencionados.

Requerimientos:

1. Saber si un pedido puede entregarse.
2. Registrar la entrega de un pedido, descontando stock y guardándolo entre los pedidos
   entregados.
3. Calcular el precio de un pedido.

## 2. Archivos generados

| Archivo | Contenido |
|---|---|
| `corralon.wlk` | Modelo de dominio: productos, items, pedidos y corralón. |
| `corralon.wtest` | 21 tests que cubren los tres requerimientos y los ejemplos del enunciado. |
| `PROCESO.md` | Este documento, con el proceso de deducción y las dificultades encontradas. |

No se modificaron `example.wlk` ni `testExample.wtest`; sus tests siguen pasando.

## 3. Relevamiento inicial

Primero leí:

- `enunciado.md`, para extraer conceptos, reglas y ejemplos numéricos.
- `example.wlk` y `testExample.wtest`, para ver el estilo de código y de tests ya usado.
- `package.json`, para conocer la versión declarada de Wollok.
- `.github/workflows/ci.yml`, para saber cómo se ejecutan los tests en integración continua.

El CI ejecuta:

```bash
wollok test --skipValidations -p ./
```

Las versiones locales encontradas fueron:

- Wollok CLI 1.1.0.
- Wollok-TS 4.3.0.
- Wollok-Lang 4.0.0.
- `package.json` declara `wollokVersion: 4.2.3`.

Esa diferencia entre la versión declarada y la versión efectivamente instalada fue relevante
para interpretar la sintaxis disponible.

## 4. Deducción del modelo

### 4.1. Conceptos del enunciado

El enunciado menciona estos conceptos:

- **Producto**: tiene stock y precio base.
- **Material**: es un producto con costo de transporte por kilómetro y una restricción de
  cantidad mínima.
- **Herramienta**: es un producto con una restricción de distancia máxima.
- **Herramienta electrónica**: es una herramienta con un costo adicional por garantía.
- **Item de pedido**: relaciona una cantidad con un producto.
- **Pedido**: tiene una distancia al punto de entrega y varios items.
- **Pedidos entregados**: colección donde el sistema registra los pedidos ya entregados.

### 4.2. Decisión de responsabilidades

| Concepto | Responsabilidad principal |
|---|---|
| `Producto` | Conocer stock y precio base, saber si hay stock, descontar stock y calcular el precio unitario. |
| `Material` | Agregar costo por kilómetro y exigir cantidad mayor o igual a 2. |
| `Herramienta` | Exigir distancia menor o igual a 50 km. |
| `HerramientaElectronica` | Sumar 500 pesos de garantía de transporte. |
| `ItemPedido` | Relacionar producto y cantidad; delegar en el producto las reglas y el precio. |
| `Pedido` | Agrupar items, evaluar si todos pueden entregarse, sumar precios y confirmar la entrega. |
| `Corralon` | Validar la entrega, descontar stock y registrar el pedido entregado. |

La idea central fue que el **producto** sea quien conozca sus propias reglas de entrega y sus
costos adicionales. Así, `ItemPedido` y `Pedido` delegan y no necesitan preguntar de qué tipo
es cada producto.

### 4.3. Fórmulas de precio

El enunciado muestra que el costo adicional se aplica antes de multiplicar por la cantidad:

```text
precioUnitario = precioBase + costoAdicional(distancia)
precioItem     = precioUnitario * cantidad
precioPedido   = suma de precios de todos los items
```

Casos concretos:

- Material: `2 * (100 + 3 * 35) = 410`.
- Herramienta: `3 * 50 = 150`.
- Herramienta electrónica: `1 * (1000 + 500) = 1500`.
- Pedido de ejemplo: `410 + 150 + 1500 = 2060`.

### 4.4. Entrega atómica

La entrega se implementó en dos pasos:

1. Verificar que **todo** el pedido pueda entregarse.
2. Recién entonces descontar stock y registrar el pedido.

Esto evita que un pedido inválido descuente parcialmente el stock de algunos productos.
Si el pedido no puede entregarse, se lanza un error de dominio con `self.error(...)`.

## 5. Cobertura de tests

Se agregaron 21 tests en total, contando el test existente de `pepita`.

### Requerimiento 1: puede entregarse

- Item con stock suficiente.
- Item que pide exactamente el stock disponible.
- Item que pide más stock del disponible.
- Herramienta a 50 km.
- Herramienta a 51 km.
- Material con cantidad 2.
- Material con cantidad 1.
- Pedido de ejemplo a 35 km.
- Pedido de ejemplo a 70 km.
- Pedido donde un solo item inválido invalida el pedido completo.

### Requerimiento 2: entrega

- Descuento de stock de cada producto.
- Registro del pedido entregado.
- Conocimiento de todos los pedidos entregados.
- Pedido sin stock: error, stock sin cambios y sin registro.
- Pedido con herramienta a más de 50 km: error, stock sin cambios y sin registro.
- Pedido con un solo material: error, stock sin cambios y sin registro.

### Requerimiento 3: precio

- Precio de material con costo por kilómetro: 410.
- Precio de herramienta: 150.
- Precio de herramienta electrónica: 1500.
- Precio total del pedido de ejemplo: 2060.

## 6. Dificultades encontradas

### 6.1. La documentación de constructores no coincidía con la versión instalada

La primera dificultad fue la sintaxis de creación de objetos. La documentación consultada vía
Context7 mostraba, por un lado, una sección de inicialización con un esquema del tipo
`constructor()` + `initialize` (la propia fuente lo marcaba como deprecado) y, por otro, un
ejemplo de instanciación con argumentos nombrados: `new Dog(name = "Rex")`.

A partir de esa idea probé un constructor explícito con parámetros, equivalente a este
ejemplo mínimo:

```wollok
class Base {
  var valor = 0

  constructor(unValor) {
    valor = unValor
  }
}
```

y luego:

```wollok
new Base(10)
```

Ese fragmento es una **reconstrucción mínima** del intento, no una copia textual de la
documentación. El intento real se hizo en un archivo scratch temporal que después fue
sobrescrito con otras pruebas.

Al probar esa forma en este entorno, el código no funcionó como se esperaba. Aparecieron
errores de validación/parseo y, al intentar `new Base(10)`, el runtime respondió:

```text
Could not resolve reference to new
```

El problema no era el concepto de herencia ni la instanciación con argumentos nombrados
(`new Dog(name = "Rex")` sí es válida en esta versión), sino que **la versión instalada no
acepta declaraciones explícitas de `constructor(...)` con parámetros de la forma en que las
estaba probando**.

### 6.2. Cómo se dedujo la forma correcta

Para no basarme en suposiciones, hice una prueba mínima en un proyecto temporal aparte. La
estrategia fue:

1. Probar una clase simple con `constructor(...)`.
2. Probar `new Base(10)`.
3. Probar `new Base(valor = 10)`.
4. Revisar los ejemplos y el código del paquete Wollok instalado.
5. Confirmar el comportamiento con `wollok lint` y `wollok test`.

La forma que funcionó fue declarar los atributos y pasarlos como **argumentos nombrados** al
crear la instancia:

```wollok
class Material inherits Producto {
  const costoPorKm = 0
}

const arena = new Material(stock = 10, precioBase = 100, costoPorKm = 3)
```

Es decir, en esta versión la inicialización se hace por nombre de atributo, no mediante una
declaración explícita de constructor.

### 6.3. Herramientas de diagnóstico usadas

Además de las pruebas empíricas, revisé el paquete instalado:

- Ejemplos de clases y objetos:
  `$(npm root -g)/wollok-ts-cli/examples/ast-examples/ok-project/example.wlk`
- Ejemplos de instanciación con argumentos nombrados:
  `$(npm root -g)/wollok-ts-cli/examples/diagram-examples/fish.wlk`
- Código del intérprete:
  `$(npm root -g)/wollok-ts-cli/node_modules/wollok-ts/dist/interpreter/runtimeModel.js`
- Comentario de la librería estándar sobre ausencia de constructores vararg:
  `$(npm root -g)/wollok-ts-cli/node_modules/wollok-ts/dist/wre/wollok/lang.wlk`

En el intérprete aparecía un mensaje clave:

```text
cannot be instantiated, you must pass values to the following attributes
```

Ese mensaje confirmó que la instanciación se basa en atributos inicializados por nombre.

### 6.4. `super` en métodos sobrescritos

También fue necesario validar la llamada al método de la clase base. La forma que funcionó
fue:

```wollok
override method puedeEntregarse(cantidad, distancia) =
  super(cantidad, distancia) && cantidad >= 2
```

Y para el costo adicional de la herramienta electrónica:

```wollok
override method costoAdicional(distancia) = super(distancia) + 500
```

La prueba mínima confirmó que `super(...)` funciona tanto con argumentos como sin ellos,
según la firma del método base.

### 6.5. Warnings de lint

El primer lint no falló, pero emitió advertencias del tipo:

```text
Variable should be const
```

Se resolvieron convirtiendo a `const` los atributos que no se reasignan después de la
inicialización:

- `precioBase`
- `costoPorKm`
- `producto`
- `cantidad`
- `distancia`
- `items`
- `pedidosEntregados`

Las listas `items` y `pedidosEntregados` quedaron como `const` porque no se reasigna la
referencia, aunque su contenido sí se modifica con `add`. Después de ese cambio, el lint quedó
limpio.

### 6.6. Detalle de la CLI con rutas absolutas

También hubo una dificultad menor al intentar crear un proyecto temporal con `wollok init` y
una ruta absoluta: la herramienta la interpretó como una ruta relativa dentro del directorio
actual. Se resolvió usando la ruta de trabajo (`workdir`) y limpiando los directorios
generados por error.

## 7. Fuentes de información

La información se obtuvo combinando estas fuentes:

1. **El enunciado del ejercicio**: `enunciado.md`.
2. **El scaffold del repositorio**: `example.wlk`, `testExample.wtest`, `package.json` y el
   workflow de CI.
3. **Documentación vía Context7**: la biblioteca `Wollok Language`, útil para conceptos
   generales, tests y manejo de errores, aunque su esquema de inicialización con
   `constructor()` estaba marcado como deprecado y no coincidía con la versión instalada.
4. **El paquete Wollok instalado localmente**:
   - Ejemplos de código de la CLI.
   - Código del intérprete y mensajes de error.
   - Librería estándar incluida en `wollok-ts`.
5. **Pruebas empíricas controladas**: pequeños archivos `.wlk` y `.wtest` en un proyecto
   temporal, ejecutados con `wollok lint` y `wollok test`, para validar cada construcción
   antes de usarla en la solución final.

La conclusión importante es que, ante una diferencia entre documentación y comportamiento,
la fuente de verdad fue el runtime instalado y la ejecución real del código.

## 8. Verificación final

Comandos ejecutados en el proyecto:

```bash
wollok test --skipValidations -p ./
wollok lint -p ./
```

Resultados:

- `wollok test --skipValidations -p ./`: **21 tests pasan**.
- `wollok lint -p ./`: **sin errores ni warnings**.
- `git status`: la solución (`corralon.wlk` y `corralon.wtest`) está versionada en el commit
  `Resolución`; este documento (`PROCESO.md`) queda como archivo nuevo, todavía sin agregar.

## 9. Notas y posibles mejoras

- Si se actualiza a una versión de Wollok que sí soporte constructores explícitos, se podría
  reemplazar la inicialización por argumentos nombrados por constructores con validación.
- Se podría encapsular mejor la lista de pedidos entregados para no exponer la lista mutable.
- Se podría definir un tipo de error de dominio específico en lugar de usar `self.error(...)`.
- El commit `Resolución` contiene el código y los tests; `PROCESO.md` aún no fue agregado al
  repositorio.
