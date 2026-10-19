#!/usr/bin/env bash
# espera avatar e imagens do r7ex e monta: cena -> render -> revisar
cd ~/projetos/r7ex; P=edicoes/2026-10-18-claude-15-comandos
while pgrep -f "r7ex.py (avatar|imagens) $P" >/dev/null; do sleep 30; done
[ -s $P/avatar/avatar.mp4 ] || { echo "FALHOU: sem avatar"; exit 1; }
python3 r7ex.py cena $P && python3 r7ex.py render $P && python3 r7ex.py revisar $P && echo "== FIM"
