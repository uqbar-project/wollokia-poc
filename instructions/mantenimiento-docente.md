# Mantenimiento docente del proyecto

## Activación y alcance

Aplicar estas instrucciones en el rol docente, según [AGENTS.md](../AGENTS.md), antes de responder o actuar. El objetivo es mantener las instrucciones, los guardrails y la documentación del proyecto según los pedidos docentes.

Leer los archivos afectados antes de revisarlos o editarlos. Leer íntegramente [asistencia-estudiante.md](asistencia-estudiante.md) antes de revisar o editar sus reglas: es material de configuración, no el protocolo de esta conversación.

No aplicar a los turnos docentes los niveles de ayuda, la puerta de diseño, el registro en `interacciones-ia.md` ni los commits automáticos del protocolo estudiantil. No borrar ni reescribir el registro existente.

## Cambios de guardrails

Para modificar las instrucciones o la documentación del proyecto:

1. Trabajar en la rama de guardrails `poc/NN/main`, que define el agente.
2. Aplicar y commitear allí los cambios a `AGENTS.md`, los archivos de `.opencode/agents/`, `opencode.json`, los archivos de `instructions/` u otros documentos de configuración.
3. No agregar las interacciones de modo docente a `interacciones-ia.md`; el historial de la rama de guardrails conserva el cambio.
4. Volver a la rama de resolución `poc/NN/resolution` y hacer rebase sobre `poc/NN/main`, para incorporar los nuevos commits de guardrails y continuar desde ahí.
5. Verificar que el registro no conserve turnos de modo docente y seleccionar el agente `estudiante` para continuar sobre la rama rebasada.

El rol docente no autoriza por sí solo instalaciones, commits, pushes ni otras acciones externas; respetar las autorizaciones y restricciones comunes de `AGENTS.md`.
