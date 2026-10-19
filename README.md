# Kit 15 Comandos — o Claude mudou

**Menos instrução, menos tokens, mais prova.** Guia grátis do INEMA.CLUB com 15 mudanças no jeito de trabalhar com o
Claude Code (e outros agentes), como implementar cada uma, cuidados, próximos kits e o que a comunidade já tem.

- Guia: https://inematds.github.io/kit-15-comandos/guia/ ([EN](https://inematds.github.io/kit-15-comandos/guia/en/) · [ES](https://inematds.github.io/kit-15-comandos/guia/es/))
- Kit para baixar: [kit-15-comandos.zip](https://github.com/inematds/kit-15-comandos/releases/download/kit-v1.0.0/kit-15-comandos.zip) · pasta [`kit/`](kit/)

## As cinco camadas
1. **Skills** — skill menor (só correções), avaliar com e sem, gravar a tarefa.
2. **Modelo e configurações** — trocar de modelo custa cache, esforço é a alavanca, advisor, padrões melhoraram.
3. **Plano e prova** — plano é para o humano, `/goal` com prova, hook de Stop que confere.
4. **Contexto e delegação** — janela grande não é memória, subagente ou fork, workflows de vários agentes.
5. **Rodando sem você** — rotinas por evento, sessões na nuvem.

Comandos conferidos no Claude Code 2.1.303 (out/2026); os que podem variar estão marcados no guia.

## Estrutura
- `src/{pt,en,es}.json` — todo o texto · `src/build.py` — gera `guia/` · `kit/` — modelos do kit
- `video/` — scripts do explicativo e das imagens

Licença MIT · [INEMA.CLUB](https://inema.club)
