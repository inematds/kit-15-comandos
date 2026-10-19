#!/usr/bin/env bash
# ilustrações do kit-15-comandos (página + vídeo), 3 por vez
G=~/projetos/kit-15-comandos/video/gerar_img.sh; O=~/projetos/output/explica-kit-15-comandos
run(){ "$G" "$O" "$@"; }
run 01-capa "Escritório claro e moderno. A PROFISSIONAL, tranquila, de braços cruzados, observa o ROBÔ trabalhar sozinho numa bancada; ao lado do robô, uma pilha de caixas entregues, cada uma com um selo verde de verificado. Deixe o terço de cima da imagem com fundo limpo para o título." "MENOS INSTRUÇÃO, MAIS PROVA" &
run 02-tese "Três pedestais lado a lado numa sala clara: no primeiro uma pasta de arquivos pequena e organizada, no segundo uma engrenagem girando, no terceiro um grande selo de verificado; a PROFISSIONAL aponta para os três enquanto o ROBÔ observa." &
run c1-skills "O ROBÔ sentado numa mesa clara; à esquerda, um manual de papel enorme, grosso e fechado, empurrado para o canto; à direita, na mão do robô, um único cartão pequeno com três linhas curtas desenhadas (sem letras legíveis). A PROFISSIONAL entrega o cartão." &
wait
run c2-modelo "Painel de controle claro na parede com um único seletor grande de modelo travado por um cadeado pequeno, e ao lado um botão redondo de intensidade que a PROFISSIONAL gira para o meio; o ROBÔ trabalha tranquilo ao fundo. Sem letras nem números." &
run c3-prova "Bancada de inspeção clara: o ROBÔ entrega uma caixa à PROFISSIONAL, que confere com uma lupa grande; sobre a caixa, um carimbo verde de aprovado; ao fundo, uma tela mostra uma lista com marcas de verificado (sem letras)." &
run c4-contexto "Um arquivo de gavetas pequenas de madeira clara, cada gaveta com um ícone simples diferente (sem letras); o ROBÔ puxa só uma gaveta aberta e lê uma ficha; ao lado, uma janela gigante transbordando de papéis soltos, bagunçada, mostrando o contraste." &
wait
run c5-sem-voce "Escritório à noite com luz fria: um notebook FECHADO sobre a mesa vazia; na parede, uma tela grande mostra três ROBÔS trabalhando numa sala de servidores clara, cada um numa tarefa; um pequeno ícone de nuvem no canto da tela." &
run c6-fim "A PROFISSIONAL e o ROBÔ lado a lado diante de um quadro branco com três ícones grandes desenhados: uma pasta, uma engrenagem e um selo de verificado; clima de time, escritório claro." &
run 07-goal "O ROBÔ levanta um cartaz em branco como quem diz que terminou; atrás dele, a PROFISSIONAL segura uma prancheta com uma lista e uma marca vermelha num item, e aponta para uma tela de terminal que mostra linhas de teste verdes e uma vermelha (ilegíveis)." &
wait
run 08-hook "Porta de saída de um escritório claro com uma catraca; o ROBÔ tenta passar com uma caixa, e um segundo ROBÔ inspetor, idêntico mas de colete amarelo, para a catraca e confere a caixa com um scanner; uma luz verde e uma vermelha na catraca." &
run 10-delegar "Sala clara: à esquerda, a PROFISSIONAL entrega uma ficha pequena a um ROBÔ que sai por uma porta (começa do zero); à direita, um segundo ROBÔ idêntico ao lado dela, lendo o mesmo caderno grande aberto que ela segura (herda tudo)." &
wait
echo FIM
