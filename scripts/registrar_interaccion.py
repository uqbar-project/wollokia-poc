"""Deterministic student-turn logging and narrowly scoped Git commits."""
import argparse
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

LOG = 'interacciones-ia.md'
HEADER = '''# Registro de interacciones con IA

- **Proyecto:** prueba-ia-pdep
- **Estudiante:** _(completar)_
- **Objetivo del experimento:** analizar cómo se usa la asistencia de IA en el aprendizaje de diseño de software.
- **Formato:** un turno por entrada, en orden cronológico.

---
'''


class TurnError(Exception):
    pass


def require(condition, message):
    if not condition:
        raise TurnError(message)


def git(*args, check=True):
    result = subprocess.run([os.environ.get('GIT', 'git'), *args], capture_output=True)
    if check and result.returncode:
        raise TurnError('Git falló: ' + result.stderr.decode(errors='replace').strip())
    return result


def text(data, key):
    value = data.get(key)
    require(isinstance(value, str) and value.strip(), f'{key}: se requiere texto no vacío.')
    require('\x00' not in value, f'{key}: no se admite NUL.')
    return value


def metadata_path(value):
    require(isinstance(value, str), 'Las rutas deben ser texto.')
    path = PurePosixPath(value)
    require(value and not path.is_absolute() and '..' not in path.parts
            and str(path) == value and not value.startswith('-')
            and re.fullmatch(r'[\w ./-]+', value),
            f'Ruta no permitida: {value!r}; usar una ruta relativa sin caracteres de control.')
    return value


def code_path(value):
    metadata_path(value)
    path = PurePosixPath(value)
    require(path.suffix in {'.wlk', '.wtest'}, 'changes solo admite archivos .wlk o .wtest.')
    require(not any(part.startswith('.') for part in path.parts), 'No se admiten rutas ocultas.')
    require(path.parts[0] not in {'instructions', 'skills', 'scripts', 'tests', 'docs'},
            'No se permite incluir configuración, instrucciones ni herramientas en un commit estudiantil.')
    for parent in [Path(value), *Path(value).parents]:
        require(not parent.is_symlink(), f'No se admiten enlaces simbólicos: {value}')
    return value


def tracked_file(path):
    """Reject directory pathspec expansion and nonregular or hidden index entries."""
    for parent in PurePosixPath(path).parents:
        if str(parent) == '.':
            continue
        ancestor = git('ls-tree', '-z', 'HEAD', '--', str(parent)).stdout
        require(not ancestor or ancestor.startswith(b'040000 tree '),
                f'{path} reemplazaría un archivo antecesor no declarado: {parent}.')
    tree = git('ls-tree', '-z', 'HEAD', '--', path).stdout
    if tree:
        entries = tree.rstrip(b'\0').split(b'\0')
        require(len(entries) == 1, f'{path} no es una ruta exacta de archivo.')
        info, name = entries[0].split(b'\t', 1)
        mode, kind, _oid = info.split(b' ', 2)
        require(name == os.fsencode(path) and kind == b'blob' and mode in (b'100644', b'100755'),
                f'{path} no es un archivo regular exacto en HEAD; no se admiten directorios ni reemplazos de directorios.')
    index = git('ls-files', '-v', '-z', '--', path).stdout
    require(not index or index == b'H ' + os.fsencode(path) + b'\0',
            f'{path} tiene descendientes o flags especiales del índice; revisar antes de continuar.')
    return bool(tree)


def validate(data):
    require(isinstance(data, dict), 'La entrada debe ser un objeto JSON.')
    fields = {'interaction_id', 'role', 'expected_head', 'level', 'student', 'assistant',
              'files', 'changes', 'decisions', 'code_written', 'code', 'verification'}
    require(set(data) == fields, 'Campos JSON incorrectos; consultar instructions/registro-automatico.md.')
    require(data['role'] == 'student', 'Solo se admiten interacciones estudiantiles.')
    require(re.fullmatch(r'[A-Za-z0-9_-]{1,80}', text(data, 'interaction_id')), 'interaction_id inválido.')
    require(re.fullmatch(r'[0-9a-f]{40,64}', text(data, 'expected_head')), 'expected_head inválido.')
    require(data['level'] in ('A0', 'A1', 'A2', 'A3'), 'level debe ser A0, A1, A2 o A3.')
    for key in ('student', 'assistant', 'verification'):
        text(data, key)
    require(isinstance(data['files'], list) and all(isinstance(p, str) for p in data['files']),
            'files debe ser una lista de rutas.')
    for path in data['files']:
        metadata_path(path)
    require(isinstance(data['changes'], dict), 'changes debe ser un objeto ruta: SHA-256 (o null para borrar).')
    for path, digest in data['changes'].items():
        code_path(path)
        require(path in data['files'], f'changes incluye una ruta ausente en files: {path}')
        require(digest is None or (isinstance(digest, str) and re.fullmatch(r'[0-9a-f]{64}', digest)),
                f'SHA-256 inválido: {path}')
    require(isinstance(data['decisions'], list) and all(isinstance(x, str) and x.strip() for x in data['decisions']),
            'decisions debe ser una lista de textos (vacía si no hubo decisiones).')
    require(type(data['code_written']) is bool and isinstance(data['code'], str), 'code_written/code inválidos.')
    require(data['code_written'] or not data['code'], 'No incluir código si code_written es false.')
    require(not data['changes'] or data['code_written'], 'Hay cambios de código pero code_written es false.')


def quote(value):
    return '\n'.join('> ' + line if line else '>' for line in value.split('\n'))


def outside_fenced_code(history):
    """Keep top-level metadata, respecting fence character and minimum length."""
    lines = []
    fence = None
    for line in history.splitlines():
        if fence:
            closing = re.fullmatch(r' {0,3}([`~]+)[ \t]*', line)
            if closing and set(closing[1]) == {fence[0]} and len(closing[1]) >= fence[1]:
                fence = None
            continue
        opening = re.fullmatch(r' {0,3}(`{3,}|~{3,})(.*)', line)
        if opening and not (opening[1][0] == '`' and '`' in opening[2]):
            fence = (opening[1][0], len(opening[1]))
        else:
            lines.append(line)
    require(fence is None, 'El registro contiene una cerca de código sin cerrar; requiere revisión humana.')
    return '\n'.join(lines)


def render(data, number, timestamp, marker):
    files = list(dict.fromkeys([*data['files'], LOG]))
    decisions = '\n'.join('- ' + item.replace('\n', '\n  ') for item in data['decisions']) or '- Ninguna.'
    code = ''
    if data['code']:
        fence = '`' * max(3, 1 + max((len(x) for x in re.findall(r'`+', data['code'])), default=0))
        code = f'\n\n{fence}wollok\n{data["code"]}\n{fence}'
    verification = data['verification'].replace('\n', '\n  ')
    return f'''{marker}
## Turno {number:03d} — {timestamp}

**Nivel de ayuda:** {data['level']}

**Archivos involucrados:** {', '.join(files)}

**Mensaje del estudiante:**

{quote(data['student'])}

**Respuesta del agente:**

{quote(data['assistant'])}

**Decisiones de diseño tomadas por el estudiante:**

{decisions}

**Código escrito:** {'sí' if data['code_written'] else 'no'}{code}

**Verificación:** {verification}

---
'''


def run(args):
    require(args.allow_commit, 'Falta --allow-commit: obtener autorización explícita antes de registrar y commitear.')
    require(not any(os.environ.get(key) for key in ('GIT_INDEX_FILE', 'GIT_DIR', 'GIT_WORK_TREE')),
            'Quitar GIT_INDEX_FILE/GIT_DIR/GIT_WORK_TREE antes de registrar en el repositorio actual.')
    source = Path(args.input).resolve()
    data = json.loads(source.read_text(encoding='utf-8'))
    root = Path(git('rev-parse', '--show-toplevel').stdout.decode().strip())
    os.chdir(root)
    validate(data)
    branch = git('symbolic-ref', '--quiet', '--short', 'HEAD', check=False).stdout.decode().strip()
    require(re.fullmatch(r'poc/\d+/resolution', branch), 'Ejecutar solo en poc/NN/resolution, nunca en guardrails ni HEAD separado.')
    for state in ('MERGE_HEAD', 'CHERRY_PICK_HEAD', 'REVERT_HEAD', 'rebase-merge', 'rebase-apply', 'sequencer'):
        state_path = Path(git('rev-parse', '--git-path', state).stdout.decode().strip())
        require(not state_path.exists(), f'Hay una operación Git pendiente ({state}); resolverla antes de registrar.')
    lock = Path(git('rev-parse', '--git-path', 'student-interaction.lock').stdout.decode().strip())
    try:
        lock.mkdir()
    except FileExistsError:
        raise TurnError(f'Hay otra ejecución o un bloqueo pendiente: {lock}. Verificar antes de retirarlo.')
    try:
        process(data)
    finally:
        lock.rmdir()


def process(data):
    head = git('rev-parse', 'HEAD').stdout.decode().strip()
    tracked_log = tracked_file(LOG)
    baseline = git('show', f'HEAD:{LOG}').stdout if tracked_log else None
    log = Path(LOG)
    require(not log.is_symlink() and (not log.exists() or log.is_file()), 'El registro debe ser un archivo regular, no un enlace.')
    original = log.read_bytes() if log.exists() else None
    require(original == baseline, 'El registro tiene cambios locales o está borrado; resolverlos sin reescribir el historial antes de continuar.')
    require(not git('diff', '--cached', '--name-only', '-z').stdout, 'Hay cambios staged ajenos; dejarlos fuera del índice antes de continuar.')
    fingerprint = hashlib.sha256(json.dumps(data, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    marker = f'<!-- student-interaction:{data["interaction_id"]} sha256:{fingerprint} -->'
    history = (baseline or b'').decode('utf-8')
    metadata = outside_fenced_code(history)
    existing = re.findall(r'^<!-- student-interaction:' + re.escape(data['interaction_id']) + r' [^\n]* -->$', metadata, re.M)
    if existing:
        require(existing == [marker], 'interaction_id ya registrado manualmente o con otro contenido; no reutilizarlo.')
        print('La interacción ya está registrada y commiteada; no se duplicó.')
        return
    require(head == data['expected_head'], 'HEAD cambió; revisar el turno y actualizar expected_head antes de continuar.')
    for path, expected in data['changes'].items():
        current = Path(path)
        tracked = tracked_file(path)
        require((not current.exists()) if expected is None else
                (current.is_file() and hashlib.sha256(current.read_bytes()).hexdigest() == expected),
                f'El contenido de {path} no coincide con el declarado; revisar changes.')
        if expected is None:
            require(tracked,
                    f'No se puede borrar un archivo no versionado: {path}')
    numbers = [int(n) for n in re.findall(r'^## Turno (\d+) — ', metadata, re.M)]
    require(numbers == sorted(set(numbers)), 'Numeración del registro inválida; requiere revisión humana.')
    number = (numbers[-1] if numbers else 0) + 1
    timestamp = datetime.now(ZoneInfo('America/Argentina/Buenos_Aires')).isoformat(timespec='seconds')
    prefix = original if original is not None else HEADER.encode()
    appended = prefix + (b'\n' if prefix.endswith(b'\n') else b'\n\n') + render(data, number, timestamp, marker).encode()
    paths = [LOG, *data['changes']]
    log.write_bytes(appended)
    try:
        # --only excludes unrelated unstaged work and does not require broad git add.
        # New paths must first be known to the index; intent-to-add stores no contents.
        new_paths = [p for p in paths if git('ls-files', '--error-unmatch', '--', p, check=False).returncode]
        if new_paths:
            git('add', '--intent-to-add', '--', *new_paths)
        git('commit', '--only', '-m', f'chore: record student interaction {number:03d}', '--', *paths)
    except TurnError:
        if git('rev-parse', 'HEAD').stdout.decode().strip() == head:
            git('reset', '--quiet', 'HEAD', '--', *paths)
            if log.read_bytes() == appended:
                if original is None:
                    log.unlink()
                else:
                    log.write_bytes(original)
        raise
    print(f'Turno {number:03d} registrado y commiteado. No se hizo push.')


def main():
    parser = argparse.ArgumentParser(description='Registra y commitea un turno estudiantil desde un JSON privado.')
    parser.add_argument('--input', required=True, help='Ruta al JSON del turno; no incluir su contenido en argv.')
    parser.add_argument('--allow-commit', action='store_true', help='Confirma autorización explícita para este commit.')
    try:
        run(parser.parse_args())
    except (TurnError, OSError, ValueError, TypeError, ZoneInfoNotFoundError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
