---
name: relatorio-semanal
description: Relatório semanal de vendas da loja. Use quando pedirem o relatório da semana, o fechamento semanal ou o resumo de vendas.
---

# Relatório semanal — só o que o agente erra sem esta skill

> Modelo de skill enxuta. Troque o exemplo pelo seu caso. Regra: cada linha abaixo nasceu de um erro real
> que o agente cometeu quando fez a tarefa SEM skill. O resto ele já sabe fazer.

## Dados
- Os números vêm de `dados/vendas.csv`. Nunca da memória nem de estimativa.
- Semana = segunda a domingo (o agente usa domingo a sábado se não for avisado).
- Devolução entra como venda negativa; não pode sumir do total.

## Nomes e formato
- Nome de produto exatamente como está na planilha, sem traduzir nem abreviar.
- Valores em R$ com vírgula decimal.

## Fecho
- Termina sempre com 3 ações para a próxima semana, cada uma com um responsável.

## Como manter
- Troca de modelo? Rode a avaliação (`../02-avaliar-skill/`). Linha que ele passou a acertar sozinho sai daqui.
