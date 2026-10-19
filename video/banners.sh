#!/usr/bin/env bash
R=~/projetos/kit-15-comandos; G=~/.claude/skills/projetos-landing-guia/assets/gerar-banner.sh
SIDES="um robô humanoide branco fosco estilo Tesla Optimus, liso; a FRENTE da cabeça do robô é um VISOR PRETO brilhante (faixa escura onde ficam os olhos), bem visível, nunca a cabeça toda branca, sem rosto de tela nem olhos desenhados; ele digita num terminal com linhas amarelas, cercado de quinze pequenos cartões de luz flutuando"
pt(){ bash $G --repo $R --title "O CLAUDE MUDOU: 15 COMANDOS" --destaque "COMANDOS" --sub "Menos instrução, menos tokens, mais prova." --line "15 dicas, como implementar e kit para baixar" --tiles "Skills,Modelo,Prova,Contexto,Delegar,Sem você" --sides "$SIDES" "$@"; }
en(){ bash $G --repo $R --lang en --title "CLAUDE CHANGED: 15 COMMANDS" --destaque "COMMANDS" --sub "Less instruction, fewer tokens, more proof." --line "15 tips, how to apply them and a kit to download" --tiles "Skills,Model,Proof,Context,Delegate,Without you" --sides "$SIDES" "$@"; }
es(){ bash $G --repo $R --lang es --title "CLAUDE CAMBIÓ: 15 COMANDOS" --destaque "COMANDOS" --sub "Menos instrucciones, menos tokens, más pruebas." --line "15 consejos, cómo aplicarlos y kit para descargar" --tiles "Skills,Modelo,Prueba,Contexto,Delegar,Sin ti" --sides "$SIDES" "$@"; }
pt & en --saida banner-en & es --saida banner-es & wait
pt --estilo grade --saida banner-grade & en --estilo grade --saida banner-grade-en & es --estilo grade --saida banner-grade-es & wait
echo FIM
