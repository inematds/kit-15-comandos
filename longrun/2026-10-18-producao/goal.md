# Goal — kit-15-comandos (18/10/2026)

Pedido do Nei: projeto novo com as 15 mudanças do Claude Code (como implementar cada uma), landing page,
outras considerações, kits que podemos criar e o que a comunidade INEMA já tem. Mais: explicavideo detalhado
(explicavideos v2, avatar do Nei pelo estúdio) e r7ex viral "O Claude mudou: 15 comandos para dominar e economizar
tokens" (os 15 na tela, CTA "tá no inema.club, baixe o kit"). Publicar no lives4, bot v3 (só arquivos), portal e
Telegram INEMA.CCODE. O pedido já é o OK do HeyGen para esta produção (16:9 + reel), pelo estúdio.

Regra de conteúdo: sem citar a fonte (nada de apresentador, academia, curso de terceiros, nomes da equipe
Anthropic, anedotas). Tese INEMA: de prompt detalhado para contexto, execução e verificação. Cada comando com chip
"confirmado" (visto na instalação/doc) ou "conferir na sua versão". Nunca inventar comando.

## Pronto quando (comando → saída esperada)
1. `gh repo view inematds/kit-15-comandos --json visibility -q .visibility` → `PUBLIC`
2. `curl -s -o /dev/null -w '%{http_code}' https://inematds.github.io/kit-15-comandos/guia/` (e en/ es/) → `200`
3. `curl -sIL https://github.com/inematds/kit-15-comandos/releases/download/kit-v1.0.0/kit-15-comandos.zip | grep -c "200"` → ≥1
4. `grep -ciE "agentic academy|boris|tarik|cherny" guia/index.html guia/en/index.html guia/es/index.html` → 0 em cada
5. `ffprobe` do 16:9 → 1920x1080, duração ≥ 240 s; do r7ex → 1080x1920, < 60 s
6. YouTube lives4: ID do 16:9 (yt-pubx) + r7ex na fila do r7ex com canal lives4
7. portal: commit com `kit-15-comandos` + vídeos; push no origin
8. Telegram INEMA.CCODE: link do tópico + msg do MENU
9. bot v3: 2 arquivos; inemaytbot: links + "lives4"
