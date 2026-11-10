# Registrar y commitear un turno estudiantil

Con Python disponible, después de cada interacción estudiantil ejecutar **un solo comando** desde el repositorio, con autorización explícita para el commit:

```sh
sh scripts/registrar-interaccion.sh --input /ruta/privada/turno.json --allow-commit
```

Requiere Python 3.9 o superior (biblioteca estándar con datos de zona horaria) y Git con identidad configurada. No instala dependencias, no usa un modelo y nunca hace push. `GIT=/ruta/al/git` permite indicar otro ejecutable si el Git del sistema no funciona.

Si Python no está disponible, es incompatible o falla su ejecución, usar el [procedimiento manual sin Python ni scripts](registro-manual.md). Antes de reintentar o cambiar de procedimiento, inspeccionar HEAD, índice y registro para evitar duplicados. Los rechazos de autorización o de seguridad no habilitan a eludir restricciones por la vía manual.

## Preparar la entrada

Guardar el JSON fuera del repositorio, en un directorio privado, con permisos de lectura restringidos. Usar un identificador estable y distinto por interacción, por ejemplo un UUID. No poner el contenido del turno en argumentos de terminal. El agente prepara los datos del turno: el script no interpreta decisiones, no revisa la asistencia ni evalúa la privacidad.

```json
{
  "interaction_id": "sesion-2026-11-09-turno-1",
  "role": "student",
  "expected_head": "REEMPLAZAR_POR_GIT_REV_PARSE_HEAD",
  "level": "A0",
  "student": "Texto exacto del estudiante.\nSegunda línea.",
  "assistant": "Texto exacto de la respuesta que verá el estudiante.",
  "files": [],
  "changes": {},
  "decisions": [],
  "code_written": false,
  "code": "",
  "verification": "no aplica"
}
```

- `expected_head`: resultado de `git rev-parse HEAD`, capturado antes del trabajo del turno. Si cambió, revisar antes de actualizarlo.
- `student` y `assistant`: textos exactos, incluidos saltos de línea y líneas vacías. No resumirlos. El script aplica las citas Markdown del registro.
- `files`: rutas relativas de archivos involucrados, aunque solo se hayan leído. Son solo metadatos: pueden incluir `enunciado.md` u otros archivos del repositorio y nunca determinan qué se commitea. Se rechazan rutas absolutas, recorridos `..` y caracteres de control; `interacciones-ia.md` se agrega automáticamente.
- `changes`: **solo** archivos de código modificados por este turno, con su SHA-256 actual. Ejemplo: `{"pedidos.wlk": "64_digitos_hexadecimales"}`. Para una eliminación autorizada, usar `null`. No incluir archivos con cambios previos ajenos; si se mezclaron en el mismo archivo, separarlos antes de ejecutar. El hash confirma el contenido declarado, no su autoría.
- `decisions`: lista de decisiones efectivamente tomadas por el estudiante, con sus nombres. Lista vacía si no hubo. Puede conservarse el detalle del formato habitual: entidad, mensajes, métodos/parámetros, datos/relaciones y responsabilidades. No exigir decisiones adicionales solo para llenar el registro.
- `code_written` y `code`: indicar si se escribió código e incluir el fragmento exacto correspondiente; si no se escribió, usar `false` y `""`.
- `verification`: pruebas realmente ejecutadas y resultado, o el motivo por el que no se ejecutaron. No inventar evidencia.

Antes de guardar la entrada, aplicar la política de privacidad: no incorporar credenciales, datos personales sensibles ni detalles internos de herramientas. La automatización no los detecta ni elimina. Eliminar los archivos temporales privados según corresponda después del éxito; el script no los borra.

## Qué automatiza

Calcula el siguiente número de turno y la fecha/hora de Buenos Aires, conserva el registro anterior byte por byte, agrega el turno con el formato existente y crea un commit convencional. Incluye únicamente el registro y las rutas declaradas en `changes`; los cambios no relacionados permanecen fuera del commit. También sirve cuando no hubo código o el pedido fue rechazado.

Un comentario HTML con el identificador y la huella de la entrada permite reintentos: repetir **el mismo JSON** después de un éxito no agrega otro turno ni commit. Reutilizar el identificador con otro contenido o después de un registro manual se rechaza. Tras un éxito no agregar manualmente el turno ni ejecutar otro `git add`/`git commit` para el mismo registro. Si hay un fallo de ejecución, inspeccionar primero el estado según el procedimiento manual antes de decidir cómo continuar.

## Condiciones de seguridad y errores

- Ejecutar solo para estudiantes y en `poc/NN/resolution`. En ramas de guardrails o HEAD separado se rechaza, incluso si la entrada declara otro rol.
- Obtener autorización explícita antes de usar `--allow-commit`. La bandera declara esa autorización; no autentica al docente ni al estudiante.
- El índice debe estar vacío de cambios staged y el registro debe coincidir con HEAD (o no existir aún). No hacer stash, reset general ni borrar entradas para sortear un error.
- Las rutas de código deben ser relativas, explícitas y corresponder a archivos regulares exactos, nunca a directorios o prefijos. No se admiten enlaces simbólicos, rutas ocultas, flags especiales del índice (tampoco en el registro), reemplazos archivo/directorio ni carpetas de instrucciones/herramientas. El script no modifica código.
- No editar archivos ni ejecutar Git concurrentemente. El bloqueo en `.git/student-interaction.lock` evita dos ejecuciones simultáneas del script. Si queda tras una interrupción, verificar que no haya otra ejecución antes de retirarlo.
- Un fallo normal de commit restaura el registro anterior y retira del índice solo las rutas del turno; conserva el código sin commitear. Una interrupción abrupta puede dejar el registro pendiente: revisar el diff antes de recuperar, sin repetir ciegamente ni reescribir historial. Los hooks locales de Git deben ser de confianza y no cambiar contenido ni agregar archivos ajenos.
- Si hay cambios previos en el registro o un error de identidad, permisos, hashes o HEAD, corregir la causa indicada y volver a intentar. Nunca resolverlo incluyendo cambios ajenos.

La respuesta preparada en `assistant` debe coincidir con la que se envía después de completar el registro y su commit, por la vía automática o manual. Si falla, resolver el registro antes de continuar con la interacción, según la política de asistencia.
