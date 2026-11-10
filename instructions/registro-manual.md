# Registrar un turno sin Python ni scripts

Si Python falta, es incompatible o falla su ejecución, el agente puede registrar y commitear el turno manualmente con un editor y Git. **No hace falta instalar Python para continuar.** Este procedimiento conserva el formato y las restricciones del [registro automático](registro-automatico.md); no permite eludir un error de seguridad o autorización.

## 1. Revisar antes de reintentar o pasar al registro manual

No ejecutar otra vez el script ni agregar un turno hasta inspeccionar el estado real:

```sh
git branch --show-current
git rev-parse HEAD
git status
git diff -- interacciones-ia.md
git diff --cached
git log -1 --format='%H %s' --name-only
```

Leer también el registro completo o, si ya se conoce su historial, las últimas entradas y cualquier agregado pendiente. `git diff` no muestra el contenido de un archivo nuevo no versionado: si el estado indica `?? interacciones-ia.md`, abrirlo en el editor. Si el registro existe en HEAD, comparar con `git show HEAD:interacciones-ia.md` sin reemplazar el archivo de trabajo.

Comparar HEAD con el hash capturado antes del turno o con `expected_head` del JSON, si hubo intento automático. Si cambió, comprobar si el nuevo commit es justamente el turno ya completado; si el cambio tiene otra causa o no se puede explicar, detenerse y revisar antes de continuar.

Distinguir el motivo del fallo:

- **Problema de ejecución de Python:** comando inexistente, versión anterior a 3.9, error de importación/zona horaria, excepción interna no atribuible a los datos o interrupción. Se permite la vía manual, pero primero verificar si hubo cambios o un commit. Un código de salida no exitoso no prueba que el turno esté sin registrar.
- **Rechazo de las condiciones del turno:** falta de autorización, rama incorrecta, cambios staged ajenos, registro modificado, HEAD inesperado, JSON incompleto o inválido, rutas/hashes/identificador inválidos, flags especiales u operación Git pendiente. Resolver la causa y revisar el turno; **no usar el registro manual para saltear el rechazo**. Si Git no funciona, tampoco puede completarse el commit manual.

Usar el mismo identificador estable del turno si ya se preparó un JSON; si no, elegir uno nuevo y conservarlo durante los reintentos. Buscarlo en los comentarios del registro y comparar además el texto completo del estudiante y de la respuesta:

- Si el turno exacto ya está registrado en un commit, no volver a agregarlo ni crear otro commit.
- Si solo quedó un agregado local completo y verificablemente perteneciente al mismo turno, conservarlo y terminar únicamente su commit, tras revisar el diff. No duplicar el agregado.
- Si hay un fragmento incompleto, contenido distinto con el mismo identificador, cambios previos ajenos o dudas sobre qué se ejecutó, detenerse y pedir revisión. No borrar ni reescribir entradas para recuperar el flujo.

## 2. Aplicar las mismas restricciones

Solo para interacciones **estudiantiles**, en una rama `poc/NN/resolution` con `NN` numérico y con autorización explícita para el commit. No cambiar de rol, instalar herramientas ni hacer push para resolver el fallo.

Antes de continuar, el índice debe estar libre de cambios ajenos, no debe haber merge/rebase/cherry-pick/revert pendiente ni otra ejecución del script o de Git. No usar `GIT_INDEX_FILE`, `GIT_DIR` o `GIT_WORK_TREE` que redirijan la operación. Si quedó `.git/student-interaction.lock`, verificar que no haya otro proceso antes de retirarlo. Los hooks locales deben ser de confianza y no alterar archivos ni incluir cambios ajenos.

Definir la lista exacta de archivos de código de este turno (`.wlk` o `.wtest`) y revisar su diff completo. Los archivos solo leídos, como `enunciado.md`, se mencionan en el registro pero **no se agregan al commit**. No incluir instrucciones, herramientas, archivos privados ni cambios previos de otras tareas. Si un archivo mezcla cambios ajenos con los del turno, separarlos antes de continuar, sin descartarlos ni commitearlos por comodidad.

Para el registro y cada ruta a commitear, comprobar entradas y flags; por ejemplo, si el turno cambió `pedidos.wlk`:

```sh
git ls-tree HEAD -- interacciones-ia.md pedidos.wlk
git ls-files -v -- interacciones-ia.md pedidos.wlk
git diff -- pedidos.wlk
```

Cada entrada existente en HEAD debe ser un **blob regular exacto** (`100644` o `100755`) con esa ruta; nunca un directorio/prefijo, enlace simbólico o submódulo. Para un archivo nuevo no habrá entrada en HEAD. Las entradas del índice deben comenzar con `H ` y coincidir exactamente con las rutas: no continuar con `S`, `h` ni descendientes inesperados. Tampoco reemplazar un archivo antecesor por un directorio para crear una ruta nueva: si hay carpetas intermedias, verificar que sean directorios en HEAD. Estas comprobaciones también rigen para eliminaciones. El archivo de trabajo y sus antecesores no pueden ser enlaces simbólicos.

## 3. Agregar la entrada, sin tocar el historial

Si todavía no hay un agregado del turno, crear `interacciones-ia.md` con el **encabezado inicial de la sección 8** de [asistencia-estudiante.md](asistencia-estudiante.md#8-registro-obligatorio-de-interacciones), solo si no existe. Luego agregar al final, sin reemplazar sus bytes anteriores.

Tomar el último número real de turno, sumarle uno y usar al menos tres dígitos (`001` si no había turnos). No contar encabezados dentro de citas o fragmentos de código. Obtener la hora de Buenos Aires, no la zona del equipo:

```sh
TZ=America/Argentina/Buenos_Aires date '+%Y-%m-%dT%H:%M:%S%z' | sed -E 's/([+-][0-9]{2})([0-9]{2})$/\1:\2/'
```

Usar el resultado real en el encabezado. El siguiente es un **ejemplo de formato**, no un turno para copiar al historial:

```markdown
<!-- student-interaction:sesion-ejemplo-turno-8 manual -->
## Turno 008 — 2026-11-10T09:20:00-03:00

**Nivel de ayuda:** A0

**Archivos involucrados:** enunciado.md, interacciones-ia.md

**Mensaje del estudiante:**

> Todavía no sé por dónde empezar.
>
> Quiero seguir en A0.

**Respuesta del agente:**

> ¿Qué requerimiento querés abordar primero?

**Decisiones de diseño tomadas por el estudiante:**

- Ninguna.

**Código escrito:** no

**Verificación:** no aplica

---
```

Reemplazar todos los datos por los del turno real. Conservar exactamente ambos textos, sus saltos de línea y líneas vacías, usando `>` en cada línea de la cita. No resumir ni corregir lo que se dijo. Registrar las decisiones reales (entidad, mensajes, parámetros, datos/relaciones y responsabilidades, cuando las haya), sin pedir nuevas definiciones para llenar campos.

Si se escribió código, indicar `**Código escrito:** sí` y agregar debajo un bloque `wollok` con el fragmento exacto; usar una cerca más larga si el texto contiene acentos graves consecutivos. Registrar la verificación realmente realizada o por qué no hubo pruebas. Si el pedido fue rechazado o no produjo código, registrarlo igual. El comentario con el identificador permite reconocer el mismo turno en un reintento; no reutilizarlo para otro contenido.

No incluir credenciales, datos personales sensibles ni detalles internos de herramientas. Preparar la respuesta exacta que verá el estudiante y enviarla sin cambios después de completar el registro. No guardar archivos temporales privados en el repositorio.

## 4. Commitear únicamente el turno

Revisar el diff del registro: solo puede agregarse el turno actual. Si se está recuperando un fallo previo, revisar también lo que ya esté staged antes de agregar nada. Con autorización explícita, agregar las rutas exactas que se verificaron; **nunca `git add .` ni `git add -A`**.

Ejemplo de turno sin código:

```sh
git add -- interacciones-ia.md
git diff --cached --name-only
git diff --cached
git diff --cached --check
```

Si el turno además modificó `pedidos.wlk`, usar `git add -- interacciones-ia.md pedidos.wlk` en lugar del primer comando. La lista staged y su contenido deben coincidir únicamente con el registro y los cambios autorizados de este turno. Si aparece otra ruta, un borrado inesperado o historial modificado, detenerse; no commitear ni limpiar cambios a ciegas.

Después de verificar el contenido, ejecutar una sola vez, reemplazando `008` por el número real:

```sh
git commit -m "chore: record student interaction 008"
git log -1 --format='%H %s' --name-only
git show --format= --stat HEAD
git status --short
```

Verificar que el commit incluya el turno exacto y solo las rutas previstas; los cambios ajenos deben seguir fuera. Si el commit falla o se interrumpe, volver a la inspección de la sección 1, no agregar otro turno. Si tuvo éxito, no ejecutar luego la automatización para ese mismo turno ni crear un segundo commit; usar un identificador nuevo para la próxima interacción. **No hacer push.**
