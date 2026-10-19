# Cola — 15 comandos do Claude Code (out/2026)

Conferidos no Claude Code 2.1.303. Marcados com (conferir) os que podem variar na sua versão: rode `claude --help` e `/help`.

| # | Comando | Para quê | Regra de bolso |
|---|---|---|---|
| 1 | `/model` · `claude --model` | escolher o modelo | escolha no começo e fique; trocar no meio relê tudo sem cache |
| 2 | `/context` | ver o que ocupa a janela | olhe antes de colar mais coisa |
| 3 | `/goal <condição>` | continuar até cumprir | a condição precisa de prova (script que passa + saída na conversa + limite de voltas) |
| 4 | `claude --cloud "tarefa"` · `claude --teleport` | rodar na nuvem e trazer de volta | notebook fechado, tarefa seguindo |
| 5 | `/effort` · `claude --effort low\|medium\|high` | regular o esforço | baixe o esforço em vez de trocar de modelo |
| 6 | hook de `Stop` (tipo prompt; tipo agent em conferir) | conferir antes de deixar parar | regra que não pode falhar vira hook, não frase no CLAUDE.md |
| 7 | `/compact` | resumir a conversa | prefira handoff em arquivo para trabalho longo |
| 8 | `/clear` + handoff + `/prime` | recomeçar sem perder o fio | grave o estado em arquivo antes de limpar |
| 9 | `/usage` (`/cost`) | ver gasto e limite | olhe depois de cada tarefa grande |
| 10 | `/advisor` | modelo forte só nas decisões difíceis | experimental; não quebra o cache |
| 11 | fork da conversa | tarefa paralela que precisa do histórico | herda tudo e aproveita o cache |
| 12 | subagente (`--agents`, agentes do projeto) | tarefa isolada | começa limpo, devolve só o resultado; passe as regras no pedido |
| 13 | `/schedule` (`/routines`) | rotinas na nuvem | gatilho por API/evento: (conferir); token = senha |
| 14 | `claude plugin eval --ablation with-without` | avaliar com e sem skill | não ganhou? enxugue ou apague |
| 15 | Shift+Tab · `--permission-mode plan` | plano antes de editar | plano é para você aprovar objetivo, limites e pronto |

Extra: `/config` → *Dynamic workflow size* pequeno antes de pedir pesquisa com vários agentes.

Guia completo: https://inematds.github.io/kit-15-comandos/guia/ · INEMA.CLUB
