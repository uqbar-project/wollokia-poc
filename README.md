# Aprender programación con Wollok e IA

Proyecto de investigación sobre asistencia con IA en el aprendizaje de diseño orientado a objetos. La IA acompaña al estudiante sin reemplazar sus decisiones de diseño.

- [Descripción técnica del proyecto](docs/descripcion-tecnica.md)
- [Enunciado del ejercicio](enunciado.md)

## 1. Preparar el entorno

Para el recorrido de aprendizaje se necesitan Git, VS Code, Node.js/npm, Wollok y OpenCode, según los pasos siguientes. **Python es opcional**: solo se utiliza para automatizar el registro; el [registro manual](instructions/registro-manual.md) funciona con un editor y Git, sin Python ni scripts.

Instalar [Git](https://git-scm.com/downloads), [Visual Studio Code](https://code.visualstudio.com/download) y [Node.js con npm](https://nodejs.org/en/download). Para elegir la versión de Node compatible con Wollok, seguir la [guía oficial de instalación](https://www.wollok.org/getting_started/installation_recomended/).

Clonar el repositorio desde su URL en GitHub o abrir una copia local que conserve su carpeta `.git`. En VS Code, usar **Archivo → Abrir carpeta** y seleccionar la raíz `prueba-ia-pdep`, donde están `AGENTS.md` y `package.json`.

En una terminal, comprobar las herramientas y configurar la identidad que utilizarán los commits de este repositorio:

```sh
git --version
node --version
npm --version
git config user.name "Nombre del participante"
git config user.email "correo-del-participante@example.com"
```

### Wollok en VS Code

1. Instalar el intérprete y comprobar que está disponible:

   ```sh
   npm install -g wollok-ts-cli
   wollok --version
   ```

2. En **Extensiones** de VS Code, instalar las dos extensiones de Uqbar: [Wollok IDE (`uqbar.wollok-lsp-ide`)](https://marketplace.visualstudio.com/items?itemName=uqbar.wollok-lsp-ide) y [Wollok Highlight (`uqbar.wollok-highlight`)](https://marketplace.visualstudio.com/items?itemName=uqbar.wollok-highlight).
3. En **Configuración**, buscar `wollok` e indicar `wollok` como ruta del CLI. Si no se encuentra, revisar el `PATH` o indicar la ruta completa del ejecutable.

La [guía oficial de Wollok](https://www.wollok.org/getting_started/installation/) describe estos componentes por separado: las extensiones no sustituyen al intérprete. El proyecto declara `wollokVersion: "4.2.3"` en `package.json`; no es el número de versión del paquete CLI. No hay scripts npm ni dependencias declaradas que requieran ejecutar `npm install` dentro del proyecto.

### Python opcional para automatizar el registro

El script requiere **Python 3.9 o superior**, `python3` disponible en la terminal, la biblioteca estándar y datos de zona horaria. No requiere paquetes `pip`, entorno virtual ni instalar dependencias Python del proyecto.

Si se quiere usar la automatización, instalar una versión de Python 3 con mantenimiento vigente desde [python.org](https://www.python.org/downloads/) usando el instalador del sistema correspondiente (Windows o macOS), o mediante el gestor de paquetes de la distribución en Linux. Cerrar y abrir la terminal después de instalar y comprobar:

```sh
python3 --version
python3 -c 'import sys; assert sys.version_info >= (3, 9), "Se requiere Python >= 3.9"; import zoneinfo; print(zoneinfo.ZoneInfo("America/Argentina/Buenos_Aires"))'
```

Ambos comandos deben terminar correctamente antes de usar el script. Los datos de zona horaria deben estar disponibles para [`zoneinfo`](https://docs.python.org/3/library/zoneinfo.html); si faltan, no hace falta instalar un paquete adicional para seguir trabajando: usar la vía manual. Si el instalador solo deja disponible otro nombre de comando, no asumir que `python3` existe: comprobarlo o usar también la vía manual.

**No instalar Python como condición para continuar.** Ante comando inexistente, versión incompatible o error de ejecución, seguir el [procedimiento manual y de recuperación](instructions/registro-manual.md). Si el intento automático pudo modificar el repositorio, inspeccionar primero HEAD, índice y registro para no duplicar el turno. Un error de autorización o seguridad debe resolverse, no evitarse con el procedimiento manual.

## 2. Instalar e iniciar OpenCode

Este recorrido usa **OpenCode 1**, siguiendo su [documentación oficial](https://opencode.ai/docs/). OpenCode 2 comparte el comando `opencode`, pero tiene otra instalación: no instalar ambos bajo ese nombre.

```sh
npm install -g opencode-ai
opencode --version
```

En VS Code, abrir **Terminal → Nueva terminal**, comprobar que la ubicación es la raíz del proyecto e iniciar:

```sh
opencode
```

Dentro de OpenCode:

1. Ejecutar `/connect` y completar la conexión con el proveedor de modelos elegido. Se necesita una cuenta y credenciales válidas para ese proveedor; revisar sus costos antes de usarlo.
2. Ejecutar `/models` y elegir un modelo disponible, según la [guía de modelos](https://opencode.ai/docs/models/).

Las claves se ingresan en el flujo de conexión: **no guardarlas en el repositorio, el chat ni el registro de interacciones**.

OpenCode carga las reglas del `AGENTS.md` del proyecto; este archivo le indica qué otros documentos leer. Las referencias Markdown no se incorporan automáticamente: el agente debe leerlas según esas instrucciones. Ver [reglas de OpenCode](https://opencode.ai/docs/rules/). **No ejecutar `/init`** para este recorrido: las instrucciones ya existen y ese comando puede modificarlas.

## 3. Elegir el agente

`opencode.json` selecciona `estudiante` por defecto al iniciar OpenCode en este proyecto. También puede seleccionarse explícitamente:

```sh
opencode --agent estudiante
```

El agente `estudiante` aplica [instructions/asistencia-estudiante.md](instructions/asistencia-estudiante.md): el estudiante define nombres y diseño, y el agente no resuelve el ejercicio. El nivel de ayuda inicial es A0; por ejemplo, puede pedirse `Quiero trabajar con nivel A1` para habilitar explicaciones conceptuales con ejemplos ajenos al ejercicio.

Para mantener las instrucciones y la documentación del proyecto, iniciar el agente docente:

```sh
opencode --agent docente
```

El agente `docente` aplica [instructions/mantenimiento-docente.md](instructions/mantenimiento-docente.md) para mantener `AGENTS.md`, los agentes de `.opencode/agents/`, `opencode.json` y las instrucciones del proyecto. No aplica a sus turnos el protocolo de asistencia al estudiante. No autoriza automáticamente instalaciones, commits ni pushes.

OpenCode permite seleccionar otro agente durante la sesión con `Tab`; al activarse, el agente anuncia su rol y relee sus instrucciones, sin heredar autorizaciones del anterior. Para separar los historiales de aprendizaje y mantenimiento, se recomienda usar sesiones distintas.

### Qué instrucciones se aplican

| Archivo | Función |
|---|---|
| [AGENTS.md](AGENTS.md) | Establece la selección de rol y las instrucciones comunes. |
| [.opencode/agents/estudiante.md](.opencode/agents/estudiante.md) | Adaptador mínimo del rol estudiante para OpenCode; carga su política. |
| [.opencode/agents/docente.md](.opencode/agents/docente.md) | Adaptador mínimo del rol docente para OpenCode; carga su política. |
| [opencode.json](opencode.json) | Selecciona `estudiante` como agente predeterminado del proyecto. |
| [instructions/asistencia-estudiante.md](instructions/asistencia-estudiante.md) | Política única de asistencia: niveles A0–A3, puerta de diseño, protección de reglas, registro y commits. |
| [instructions/mantenimiento-docente.md](instructions/mantenimiento-docente.md) | Política única de mantenimiento docente y flujo de ramas de guardrails. |
| [instructions/wollok.md](instructions/wollok.md) | Referencia de sintaxis compartida por ambos roles. No amplía permisos. |

OpenCode descubre ambos agentes por sus archivos en `.opencode/agents/`. Los documentos de `instructions/` son instrucciones locales, **no skills nativos**: deben leerse obligatoriamente según `AGENTS.md`, no cargarse bajo demanda. Otras herramientas leen directamente las mismas políticas, sin depender de los adaptadores de OpenCode.

En modo estudiante se registra cada turno en [interacciones-ia.md](interacciones-ia.md), sin borrar entradas anteriores, y se crea un commit con autorización explícita e identidad de Git configurada. Usar el [comando automático](instructions/registro-automatico.md) si Python está disponible, o el [registro manual sin Python ni scripts](instructions/registro-manual.md) si falta o falla. Ambas vías conservan el mismo formato y las restricciones de seguridad; nunca deben duplicar un turno ya registrado ni incluir cambios ajenos. No hacen push.

**La selección de agente no autentica docentes ni controla accesos.** Quien tenga acceso a esa selección puede elegir `docente` u otro agente. Una experiencia restringida para estudiantes necesita un control externo al prompt.

## Antes de empezar

- [ ] La raíz del proyecto está abierta en VS Code.
- [ ] Git, Wollok y OpenCode responden a sus comandos de versión.
- [ ] Las dos extensiones Wollok están instaladas y el CLI está configurado.
- [ ] OpenCode tiene un proveedor conectado y un modelo seleccionado.
- [ ] El agente confirma el modo y ha leído los archivos requeridos.

Luego, continuar con el [enunciado](enunciado.md) en modo estudiante o con la [documentación del proyecto](docs/descripcion-tecnica.md) en modo docente.
