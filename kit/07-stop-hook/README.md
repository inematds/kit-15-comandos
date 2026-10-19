# Hook de Stop que confere antes de parar

Hook roda sempre, no momento certo. No evento **Stop** (quando o Claude tenta terminar) você pode pôr uma
verificação. Se ela reprovar, o motivo volta como próxima instrução e o Claude continua.

## Jeito mais fácil: peça ao próprio Claude
```
Adicione um hook de Stop neste projeto. Quando você tentar parar, um verificador deve:
(1) ler docs/padrao.md, (2) ler o último arquivo em relatorios/, (3) dizer se o relatório quebra alguma regra
do padrão. Se quebrar, você continua corrigindo. Mostre o trecho do settings.json antes de gravar.
```

## Tipos
- **command** — roda um script (ex.: `checa.sh` da pasta 04). Determinístico, o mais confiável.
- **prompt** — um modelo lê a conversa e decide. Rápido e barato.
- **agent** — um agente abre arquivos e confere de verdade. Experimental: confira na sua versão.

## Exemplo (formato típico — valide com a doc da sua versão)
Veja `settings.exemplo.json`. Ele combina um hook `command` (checa.sh) com um `prompt`.
Copie só o bloco `hooks` para `.claude/settings.json` do projeto.

## Bons usos
- "Nunca mandar e-mail ao cliente; só rascunho" (bloqueio antes da ferramenta, não só no Stop).
- "Não termina sem os testes passarem."
- "Relatório segue o padrão da marca."
