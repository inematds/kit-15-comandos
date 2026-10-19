# Avaliar uma skill: com e sem

A pergunta é uma só: **a mesma tarefa sai melhor com a skill do que sem ela?**

## Caminho 1 — eval de plugin (Claude Code 2.1.303)

Se a sua skill está num plugin (ou numa pasta de skills que o Claude Code reconhece como plugin):

```bash
# casos em <plugin>/evals/**/case.yaml  ou  prompt.md + graders/*.md
claude plugin eval <caminho-ou-nome-do-plugin> --ablation with-without
```

O `--ablation with-without` roda um braço **sem** o plugin e mostra a diferença de nota.
Veja todas as opções com `claude plugin eval --help` (custo máximo, concorrência, modelo juiz).
Roda na sua máquina, com a sua conta: só avalie plugins em que você confia.

A pasta `evals/caso-01/` traz um caso de exemplo no formato prompt + critério (ajuste ao que a sua versão pede).

## Caminho 2 — manual, em 20 minutos

1. Escreva 3 a 5 pedidos reais da tarefa.
2. Para cada um, escreva o que conta como **bom** (3 critérios objetivos).
3. Rode cada pedido duas vezes, em sessões limpas: uma com a skill, outra sem (desative ou renomeie a pasta).
4. Dê nota 0–3 por critério, sem saber qual saída é qual (peça a outra pessoa ou a outro modelo).
5. Decida:

| Resultado | Ação |
|---|---|
| com skill ganha claramente | mantém; tira as linhas que não fizeram diferença |
| empate | enxuga pela metade e testa de novo |
| empate de novo, ou perde | apaga a skill e libera contexto |

Guarde os casos: eles são o teste da próxima versão da skill.
