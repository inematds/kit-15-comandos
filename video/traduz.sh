#!/usr/bin/env bash
# traduz src/pt.json -> src/<lang>.json (codex gpt-6-luna, assinatura); confere estrutura
cd ~/projetos/kit-15-comandos
for L in en es; do
 N=$([ $L = en ] && echo "inglês (en-US)" || echo "espanhol latino-americano (es)")
 P="Traduza para $N o arquivo JSON src/pt.json deste diretório e grave o resultado em src/$L.json. Regras: mantenha EXATAMENTE a mesma estrutura, as mesmas chaves, a mesma ordem e o mesmo número de itens em cada lista; traduza só os textos para leitura humana. NÃO traduza: URLs, nomes de arquivo, comandos (tudo que começa com / ou -- ou claude, Shift+Tab, checa.sh, CLAUDE.md, SKILL.md), valores das chaves id, img, st, n, e nomes próprios de projetos e cursos INEMA (ex.: Execução Longa, Skills v6, OSWork, LOOP-R, 7conselho, faxina-agentes). Troque a chave lang por \"$([ $L = en ] && echo en || echo es)\". Dentro de hero.h1 mantenha o <span class=\"amb\"> em volta de '15 comandos' traduzido. Tom simples e direto. Não edite nenhum outro arquivo."
 echo "$P" | timeout 1200 codex exec -m gpt-6-luna --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox - > video/traduz-$L.log 2>&1 &
done
wait
python3 - <<'P'
import json
def shape(x):
    if isinstance(x,dict): return {k:shape(v) for k,v in x.items()}
    if isinstance(x,list): return [shape(v) for v in x]
    return type(x).__name__
pt=json.load(open('src/pt.json'))
for L in ['en','es']:
    try:
        d=json.load(open(f'src/{L}.json')); print(L, 'estrutura', 'OK' if shape(d)==shape(pt) else 'DIFERENTE')
        bad=[(a['n'],b['cmd']) for ca,cb in zip(pt['camadas'],d['camadas']) for a,b in zip(ca['dicas'],cb['dicas']) if a['cmd']!=b['cmd']]
        print(L,'cmds alterados:',bad)
    except Exception as e: print(L,'ERRO',e)
P
echo FIM
