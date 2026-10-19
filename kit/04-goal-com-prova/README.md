# /goal com prova

O `/goal` faz o agente continuar até cumprir uma condição. Quem confere a condição olha a conversa:
se o agente só escrever "terminei", pode passar. Então a prova tem de **aparecer na conversa**.

## Passo 1 — o script de checagem
Peça ao agente, ANTES do goal:

> Crie `checa.sh` com regras objetivas para considerar esta tarefa pronta: os testes passam, o arquivo X existe,
> o arquivo Y não mudou. Ele termina com código 0 só se tudo passar e imprime cada regra com OK ou FALHOU.

Modelo de partida: `checa.sh` nesta pasta.

## Passo 2 — o goal
```
/goal o ./checa.sh termina com código 0 e você cola a saída completa aqui; nada fora de src/ foi alterado; pare depois de 15 voltas e diga o que faltou
```

## Boas condições
- verificável por comando (teste, contagem, arquivo existe);
- o que **não** pode mudar;
- limite de voltas;
- o que fazer se não der (parar e relatar, não inventar).

## Condições ruins
- "o relatório está pronto" · "ficou bom" · "terminar a tarefa"
