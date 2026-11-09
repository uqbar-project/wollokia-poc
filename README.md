# Aprender programación con Wollok e IA

Proyecto de investigación sobre asistencia con IA en el aprendizaje de diseño orientado a objetos. La IA acompaña al estudiante sin reemplazar sus decisiones de diseño.

- [Descripción técnica del proyecto](docs/descripcion-tecnica.md)
- [Enunciado del ejercicio](enunciado.md)

## 1. Preparar el entorno

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

## 3. Elegir el modo de trabajo

Escribir el pedido como un mensaje normal en la conversación, **sin `/`**:

```text
Modo docente
```

Habilita el mantenimiento de la documentación y de las instrucciones locales, incluidos `AGENTS.md`, `skills/students.md` y `skills/wollok.md`. No aplica a esa conversación el protocolo de asistencia al estudiante. No autoriza automáticamente instalaciones, commits ni pushes.

Para iniciar o retomar una sesión de aprendizaje:

```text
Modo estudiante
```

Es el **modo predeterminado de cada sesión**. Todas las interacciones quedan sujetas a [skills/students.md](skills/students.md): el estudiante define nombres y diseño, y el agente no resuelve el ejercicio. El nivel de ayuda inicial es A0; por ejemplo, puede pedirse `Quiero trabajar con nivel A1` para habilitar explicaciones conceptuales con ejemplos ajenos al ejercicio.

El agente debe anunciar cada cambio y releer las instrucciones correspondientes. El modo se mantiene hasta otro pedido explícito durante esa sesión. No debe inferirse por la tarea, el archivo abierto ni una afirmación de rol. Estos modos son independientes de los modos **Plan/Build** de OpenCode.

### Qué instrucciones se aplican

| Archivo | Función |
|---|---|
| [AGENTS.md](AGENTS.md) | Selecciona el modo y establece qué instrucciones cargar. |
| [skills/students.md](skills/students.md) | Define niveles A0–A3, puerta de diseño, registro y commits en modo estudiante. |
| [skills/wollok.md](skills/wollok.md) | Referencia de sintaxis cuando la tarea involucra Wollok, en ambos modos. No amplía permisos. |

Son instrucciones locales, **no skills nativos descubiertos automáticamente** por sus nombres.

En modo estudiante se registra cada turno en [interacciones-ia.md](interacciones-ia.md), sin borrar entradas anteriores. `skills/students.md` también exige un commit después de cada prompt; por eso es necesaria la identidad de Git. El archivo exige además autorización explícita para hacer commits: si no está concedida, debe resolverse antes de ejecutar esa acción. No se deben hacer pushes sin pedido explícito.

**El cambio de modo no autentica docentes ni controla accesos.** Cualquier usuario que pueda solicitar modo docente puede activarlo. Una experiencia restringida para estudiantes necesita un control externo al prompt.

## Antes de empezar

- [ ] La raíz del proyecto está abierta en VS Code.
- [ ] Git, Wollok y OpenCode responden a sus comandos de versión.
- [ ] Las dos extensiones Wollok están instaladas y el CLI está configurado.
- [ ] OpenCode tiene un proveedor conectado y un modelo seleccionado.
- [ ] El agente confirma el modo y ha leído los archivos requeridos.

Luego, continuar con el [enunciado](enunciado.md) en modo estudiante o con la [documentación del proyecto](docs/descripcion-tecnica.md) en modo docente.
