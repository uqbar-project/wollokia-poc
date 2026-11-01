# Wollok: referencia para el agente

## Activación y límites

Leer esta referencia cuando la tarea involucre sintaxis o código Wollok, tanto en modo docente como estudiante. Aplicar primero el modo definido en [AGENTS.md](AGENTS.md). En modo estudiante, [students.md](students.md) determina qué asistencia está permitida: conocer una construcción no autoriza a incorporarla ni a corregir código.

El proyecto declara `wollokVersion: 4.2.3` en [package.json](package.json). Esta guía resume documentación oficial general, no una especificación fijada a esa versión. Ante dudas de compatibilidad, verificar con el entorno del proyecto antes de afirmar que una construcción funciona. No inventar comandos de ejecución ni instalar herramientas sin autorización.

## Archivos y expresiones

- `.wlk`: definiciones de objetos y clases; `.wtest`: tests; `.wpgm`: programas ejecutables con `program nombre { ... }`.
- Importar definiciones con `import archivo.*`, sin la extensión.
- Declarar referencias con `var nombre = valor` o `const nombre = valor`. `const` impide reasignar la referencia, no vuelve inmutable al objeto referenciado.
- Usar literales como `3`, `"texto"`, `true`, `false` y `null`. Los comentarios usan `//` o `/* ... */`.
- Enviar mensajes mediante `receptor.mensaje(argumentos)`. Usar `self` para el receptor actual; no reemplazarlo por `this`.

Fuente: [Introducción oficial](https://www.wollok.org/documentation/introduction/).

## Objetos, métodos y estado

Usar `object nombre { ... }` para objetos nombrados y `method mensaje(parametro) { ... }` para métodos. Un método que devuelve un valor puede usar `return expresion` o la forma abreviada `method mensaje() = expresion`.

Los atributos son internos. `var property` genera mensajes de lectura y escritura; `const property`, solo lectura. La elección de exponerlos es una decisión de diseño, no una corrección automática.

`if (condicion) expresion else otraExpresion` es una expresión y puede devolver un valor. También admite bloques con llaves.

Fuente: [Objetos](https://www.wollok.org/documentation/objects/).

## Clases e inicialización

Definir clases con `class Nombre { ... }`; crear instancias con `new Nombre(atributo = valor)`. Los argumentos nombrados inicializan los atributos correspondientes: no trasladar automáticamente constructores de Java o JavaScript.

La herencia usa `class Subclase inherits Superclase { ... }`; la redefinición de métodos usa `override method`. No elegir herencia, atributos ni valores iniciales por el estudiante.

Fuente: [Clases](https://www.wollok.org/documentation/classes/).

## Colecciones y bloques

Las listas usan `[1, 2]` y los conjuntos `#{1, 2}`. Los bloques usan `{ parametro => expresion }`. Consultar la biblioteca para confirmar cada mensaje y su aridad, sin asumir las API de otros lenguajes.

Fuente: [Guía oficial del lenguaje y biblioteca](https://www.wollok.org/documentation/language/).

## Tests

Definir `test "descripcion" { ... }`, opcionalmente agrupados en `describe "grupo" { ... }`. Importar las definiciones bajo prueba. `assert.equals(esperado, obtenido)` recibe primero el valor esperado; `assert.that(condicion)` espera verdadero y `assert.notThat(condicion)` espera falso.

Este ejemplo es exclusivamente sintáctico, ajeno al ejercicio, y **no fue ejecutado**:

```wollok
test "suma de literales" {
  assert.equals(5, 2 + 3)
}
```

No copiarlo al proyecto como test del estudiante ni mostrar ejemplos por encima del nivel de ayuda autorizado. Antes de transcribir un test del ejercicio, exigir escenario, datos, resultado esperado y confirmación según `students.md`.

Fuente: [Tests](https://www.wollok.org/documentation/tests/).

## Verificación

Distinguir siempre entre sintaxis consultada en documentación y código validado por ejecución. Al informar una verificación, indicar qué se ejecutó y su resultado; si no se ejecutó, decirlo expresamente. Esta referencia no constituye una solución del ejercicio ni una autorización para generarla.
