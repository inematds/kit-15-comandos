#!/usr/bin/env bash
# refaz só a fase 2 (visual) do 16:9 a partir de visual/pt-b01.json
set -euo pipefail
EV=~/projetos/explicavideos; D=~/projetos/output/explica-kit-15-comandos
cd $EV; export EXPLICAVIDEOS_CONFIG=$EV/examples/kit-15-comandos-v2.json
cp $D/visual/pt-b01.json $D/v2/visual-v2/pt-b01.json
python3 engine/v2/build_block.py 1 --strict
engine/v2/run_lane.sh 1
python3 engine/assemble_languages.py
echo "== FIM $(date +%T)"; ls -la $D/v2/final/*.mp4
