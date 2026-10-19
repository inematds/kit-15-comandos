# CLAUDE.md — só ponteiros

> Modelo. O CLAUDE.md não guarda o conhecimento: diz onde ele está. O agente lê o arquivo certo só quando precisa.

## Projeto
Loja Exemplo — vendas online e balcão. Autor dos commits: <nome> <email>.

## Onde está cada coisa (leia só quando a tarefa pedir)
- Tom de voz e marca → `contexto/marca.md`
- Produtos, preços e exceções → `contexto/produtos.md`
- Processo de pedido e devolução → `contexto/processos/pedidos.md`
- Clientes especiais → `contexto/clientes.md`
- Erros já cometidos e a correção → `LICOES.md` (uma linha por lição)

## Regras que não podem falhar
Viram hook, não frase aqui (ver `../07-stop-hook/`).

## Trabalho longo
Antes de limpar a conversa, grave `handoffs/ultimo.md` (modelo em `HANDOFF.md`) e retome lendo esse arquivo.
