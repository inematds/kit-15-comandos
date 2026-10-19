# FALHAS — kit-15-comandos

| data | o que quebrou | menor correção | tipo |
|---|---|---|---|
| 2026-10-19 | montagem v1 do 16:9 parou: sem templates/pt/scene-01.html | monta.sh roda build_scene_templates.py antes do produce_blocks | prompt |
| 2026-10-19 | `pkill -f` com o caminho do monta.sh derrubou o próprio shell (exit 144) | matar por PID vindo de `pgrep -af` | prompt |
