#!/bin/sh
# Keep transcript contents in the input file, not in command-line arguments.
set -eu
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec python3 "$SCRIPT_DIR/registrar_interaccion.py" "$@"
