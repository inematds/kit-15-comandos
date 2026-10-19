#!/usr/bin/env bash
# checa.sh — modelo de checagem objetiva para usar com /goal. Ajuste as regras ao seu projeto.
# Sai 0 só se todas passarem. Imprime OK/FALHOU por regra (é isso que aparece na conversa como prova).
falhas=0
regra(){ if eval "$2" >/dev/null 2>&1; then echo "OK      $1"; else echo "FALHOU  $1"; falhas=$((falhas+1)); fi; }

regra "testes passam"                    "npm test --silent"            # ou: pytest -q
regra "relatório gerado"                 "test -s relatorios/semana.md"
regra "relatório tem 3 ações"            "[ \$(grep -c '^- \\[ação\\]' relatorios/semana.md) -eq 3 ]"
regra "modelo não foi alterado"          "git diff --quiet -- templates/"

echo "---"; [ $falhas -eq 0 ] && echo "PRONTO" || echo "FALTAM $falhas"
exit $falhas
