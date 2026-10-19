#!/usr/bin/env bash
# traduz src/pt.json -> src/<lang>.json (tradutor central inema-traduz: INEMA_TRADUCAO_*, hoje Sonnet 5.5, assinatura); confere estrutura
cd ~/projetos/kit-15-comandos
for L in en es; do
 N=$([ $L = en ] && echo "inglês (en-US)" || echo "espanhol latino-americano (es)")
 P="Traduza para $N o JSON abaixo (conteúdo de src/pt.json). Responda SÓ com o JSON traduzido, sem cercas de código nem comentários. Regras: mantenha EXATAMENTE a mesma estrutura, as mesmas chaves, a mesma ordem e o mesmo número de itens em cada lista; traduza só os textos para leitura humana. NÃO traduza: URLs, nomes de arquivo, comandos (tudo que começa com / ou -- ou claude, Shift+Tab, checa.sh, CLAUDE.md, SKILL.md), valores das chaves id, img, st, n, e nomes próprios de projetos e cursos INEMA (ex.: Execução Longa, Skills v6, OSWork, LOOP-R, 7conselho, faxina-agentes). Troque a chave lang por \"$([ $L = en ] && echo en || echo es)\". Dentro de hero.h1 mantenha o <span class=\"amb\"> em volta de '15 comandos' traduzido. Tom simples e direto.

$(cat src/pt.json)"
 ( printf '%s' "$P" | timeout 1200 ~/projetos/wifi/scripts/inema-traduz > video/traduz-$L.out 2> video/traduz-$L.log \
   && python3 -c 'import json,sys; t=open(sys.argv[1]).read(); d=json.loads(t[t.index("{"):t.rindex("}")+1]); open(sys.argv[2],"w").write(json.dumps(d,ensure_ascii=False,indent=1)+"\n")' video/traduz-$L.out src/$L.json \
   || echo "$L: tradução falhou (ver video/traduz-$L.log)" ) &
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
