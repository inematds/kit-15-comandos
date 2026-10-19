# Rotina que acorda com um evento

Rotinas rodam o Claude na nuvem (`/schedule`, alias `/routines`). Além de horário, podem começar por um
pedido web ou um evento do repositório (conferir na sua versão). O computador pode estar desligado.

## Montagem
1. **Nome e pedido.** O pedido tem objetivo, pronto e limites (modelo em `../05-plano-curto.md`).
2. **Repositório** onde ela trabalha.
3. **Gatilho:** horário, API (URL + token) ou evento do GitHub.
4. **Conectores:** deixe só os que esta rotina usa. Cada conector a mais é contexto e risco a mais.
5. **Verificação antes de soltar:** checa.sh + hook de Stop (pastas 04 e 07).

## Disparar pelo gatilho de API (exemplo)
```bash
# URL e TOKEN vêm da tela da rotina. Guarde o token como senha (arquivo .env fora do git).
curl -s -X POST "$ROTINA_URL" \
  -H "Authorization: Bearer $ROTINA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"texto": "pedido novo #123: 2 bolos de chocolate para sábado"}'
```
O formato exato do corpo e do cabeçalho está na tela da rotina: siga o que ela mostrar.

## Ideias de evento para negócio
- pedido novo no site → agente confere estoque e prepara a resposta (rascunho);
- mensagem nova no canal de feedback → agente classifica e resume;
- pull request novo → agente revisa e comenta.

## Cuidados
- URL + token disparam o agente: quem tiver os dois roda a sua rotina.
- Ponha teto (voltas, tempo, gasto) e saída como **rascunho** para tudo que fala com cliente.
