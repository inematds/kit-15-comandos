# Delegar: subagente, fork ou workflow

| Situação | Use | Por quê |
|---|---|---|
| Tarefa isolada (gerar imagem, buscar um dado, ler um arquivo grande) | **subagente** | começa limpo e devolve só o resultado; a conversa principal não enche |
| Tarefa paralela que precisa de tudo o que já foi dito | **fork** | cópia da conversa, aproveita o mesmo cache |
| Pesquisa, comparação ou verificação cruzada com muitas fontes | **workflow de vários agentes** | vários ângulos, cruza fontes, descarta o que não se sustenta |
| Pergunta simples | **nenhum** | faça na conversa mesmo |

## Cuidados
- O Claude já escolhe entre subagente e fork sozinho. Interfira só quando souber que precisa do histórico.
- Subagente pode não ler o seu CLAUDE.md: passe no pedido as regras que importam.
- Antes de pedir workflow: `/config` → *Dynamic workflow size* → pequeno (menos de cinco agentes).
- Diga o que conta como resposta boa e quais fontes valem. Confira o custo depois da primeira rodada (`/usage`).
