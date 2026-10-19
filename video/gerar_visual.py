#!/usr/bin/env python3
"""Roteiro visual v2 do vídeo kit-15-comandos (1 bloco, 12 cenas) -> visual/pt-b01.json.
Confere se cada deixa (at / *_at) existe, em ordem, na fala da própria cena."""
import json, re, sys, unicodedata
from pathlib import Path

OUT = Path.home() / "projetos/output/explica-kit-15-comandos"
M = str(OUT / "media") + "/"
rot = json.loads((OUT / "roteiro/pt.json").read_text())


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", s).split())


def img(nome, at, label, focus=(0.5, 0.5), zoom=(1.0, 1.06), prev=None, **kw):
    s = {"type": "media", "at": at, "src": M + nome, "focus": list(focus), "zoom": list(zoom), "label": label, "calm": True}
    if prev:
        s.update(cont=True, **{"from": {"focus": list(prev[0]), "zoom": prev[1]}})
    s.update(kw)
    return s


def node(i, label, col, row, at, icon=None):
    n = {"id": i, "label": label, "col": col, "row": row, "at": at}
    if icon:
        n["icon"] = icon
    return n


S = {}
S["1"] = {"header": False, "shots": [
    {"type": "hook", "at": "@start", "text": "Menos instrução, **mais prova**", "src": M + "01-capa-hook.png"},
    {"type": "fields", "at": "trabalhar com menos", "title": "O seu agente", "fields": [
        {"label": "Instrução", "value": "menos", "at": "menos instrução"},
        {"label": "Tokens", "value": "menos", "at": "gastar menos tokens"},
        {"label": "Prova", "value": "de que terminou", "at": "provar que terminou"}]},
    {"type": "statement", "at": "O Claude mudou muito", "text": "O Claude **mudou**", "then": {"text": "muita receita virou **peso**", "at": "virou peso"}},
    {"type": "keyword", "at": "quinze mudanças", "text": "15 mudanças", "sub": "em **5 camadas**", "sub_at": "cinco camadas"},
    {"type": "keyword", "at": "No fim tem um kit", "text": "Kit para baixar", "sub": "no **fim** do vídeo"},
]}
S["2"] = {"shots": [
    img("02-tese.png", "A ideia central", "a **ideia central**"),
    {"type": "steps", "at": "saindo do prompt detalhado", "goal": "do **prompt** para…", "steps": [
        {"title": "contexto", "at": "Contexto é dar"}, {"title": "execução", "at": "Execução é deixar"},
        {"title": "verificação", "at": "Verificação é exigir"}], "done_at": "prova de que terminou"},
]}
S["3"] = {"shots": [
    img("c1-skills.png", "Primeira camada", "camada 1 · **skills**"),
    {"type": "statement", "at": "trezentas linhas", "text": "Skill de **300 linhas**", "then": {"text": "repete o que ele **já faz**", "at": "o modelo já faz"}},
    img("c1-skills.png", "lista de correções", "skill = **lista de correções**", focus=(0.7, 0.5), zoom=(1.15, 1.2), prev=((0.5, 0.5), 1.06)),
    {"type": "steps", "at": "Faça a tarefa sem skill", "goal": "skill **enxuta**", "steps": [
        {"title": "faça sem skill", "at": "Faça a tarefa sem skill"}, {"title": "anote o erro", "at": "anote só o que saiu errado"},
        {"title": "compare com e sem", "at": "com e sem ela"}, {"title": "não ganhou? apague", "at": "Enxugue ou apague"}], "done_at": "Enxugue ou apague"},
    {"type": "keyword", "at": "gravar você fazendo", "text": "Grave a tarefa", "sub": "o agente **escreve a skill**", "sub_at": "escrever a skill"},
]}
S["4"] = {"shots": [
    img("c2-modelo.png", "Segunda camada", "camada 2 · **modelo**"),
    {"type": "statement", "at": "Trocar de modelo no meio", "text": "Trocar de modelo **no meio**", "then": {"text": "parece **economia**", "at": "parece economia"}},
    {"type": "steps", "at": "cada modelo guarda", "goal": "o que acontece", "steps": [
        {"title": "cada modelo, um cache", "at": "o próprio cache"}, {"title": "relê tudo sem desconto", "at": "lido de novo"},
        {"title": "e de novo na volta", "at": "de novo na volta"}], "done_at": "de novo na volta"},
    {"type": "compare", "at": "Barato por token",
     "left": {"title": "Por token", "at": "Barato por token", "tone": "neutral", "lines": [{"text": "parece **barato**", "at": "Barato por token"}]},
     "right": {"title": "Por tarefa", "at": "não é barato por tarefa", "tone": "good", "lines": [{"text": "conta as **tentativas**", "at": "não é barato por tarefa"}]}},
    img("c2-modelo.png", "Escolha um modelo", "um modelo · **baixe o esforço**", focus=(0.6, 0.5), zoom=(1.12, 1.18), prev=((0.5, 0.5), 1.06)),
]}
S["5"] = {"shots": [
    {"type": "keyword", "at": "Existe o advisor", "text": "/advisor", "sub": "o forte **só quando precisa**", "sub_at": "só nas horas difíceis"},
    {"type": "steps", "at": "antes de escolher o caminho", "goal": "quando ele **consulta**", "steps": [
        {"title": "antes do caminho", "at": "antes de escolher o caminho"}, {"title": "quando o erro volta", "at": "quando o erro volta"},
        {"title": "antes de terminar", "at": "antes de dizer que terminou"}], "done_at": "sem quebrar o cache"},
    {"type": "statement", "at": "os padrões melhoraram", "text": "Os padrões **melhoraram**", "then": {"text": "só mude **e meça**", "at": "e meça"}},
]}
S["6"] = {"shots": [
    img("c3-prova.png", "Terceira camada", "camada 3 · **plano e prova**"),
    {"type": "fields", "at": "O plano continua valendo", "title": "O plano é seu", "fields": [
        {"label": "Objetivo", "value": "o que existe no fim", "at": "o objetivo"},
        {"label": "Limites", "value": "o que não mexer", "at": "os limites"},
        {"label": "Pronto", "value": "como saber", "at": "o que conta como pronto"}]},
    {"type": "statement", "at": "Mudar um plano", "text": "Mudar o **plano**", "then": {"text": "custa menos que **desfazer**", "at": "desfazer cem linhas"}},
    img("c3-prova.png", "Peça uma entrevista", "plano no **arquivo** · sessão nova", focus=(0.4, 0.5), zoom=(1.12, 1.18), prev=((0.5, 0.5), 1.06)),
]}
S["7"] = {"shots": [
    img("07-goal.png", "a armadilha do goal", "a armadilha do **/goal**"),
    {"type": "statement", "at": "quem confere lê apenas", "text": "Quem confere lê **só a conversa**", "then": {"text": "não abre **arquivo**", "at": "Não abre arquivo"}},
    img("07-goal.png", "Se o agente disser", "\"terminei\" **não é prova**", focus=(0.3, 0.5), zoom=(1.15, 1.2), prev=((0.5, 0.5), 1.06)),
    {"type": "steps", "at": "pôr a prova dentro", "goal": "**/goal** com prova", "steps": [
        {"title": "script que passa", "at": "um script de checagem"}, {"title": "saída na conversa", "at": "a saída colada"},
        {"title": "limite de voltas", "at": "um limite de voltas"}], "done_at": "um limite de voltas"},
]}
S["8"] = {"shots": [
    img("08-hook.png", "a peça mais poderosa", "hook que **confere**"),
    {"type": "flow", "at": "Quando o Claude tenta terminar", "nodes": [
        node("t", "tenta parar", 0, 1, "tenta terminar"),
        node("v", "verificador olha", 1, 1, "outro modelo olha"),
        node("r", "não pode? motivo", 2, 1, "Se não pode"),
        node("c", "continua até passar", 3, 1, "continua até passar")],
     "edges": [{"from": "t", "to": "v", "at": "outro modelo olha"}, {"from": "v", "to": "r", "at": "Se não pode"},
               {"from": "r", "to": "c", "at": "continua até passar"}]},
    {"type": "keyword", "at": "Você nem precisa", "text": "Peça ao Claude", "sub": "ele **escreve o hook**", "sub_at": "peça ao próprio Claude"},
]}
S["9"] = {"shots": [
    img("c4-contexto.png", "Quarta camada", "camada 4 · **contexto**"),
    {"type": "statement", "at": "Um milhão de tokens", "text": "1 milhão de tokens", "then": {"text": "não é **memória melhor**", "at": "não é memória melhor"}},
    img("c4-contexto.png", "Guarde o contexto", "arquivos **pequenos**", focus=(0.35, 0.5), zoom=(1.15, 1.2), prev=((0.5, 0.5), 1.06)),
    {"type": "steps", "at": "Guarde o contexto", "goal": "contexto **portátil**", "steps": [
        {"title": "pastas pequenas", "at": "arquivos pequenos"}, {"title": "CLAUDE.md = ponteiros", "at": "só os ponteiros"},
        {"title": "handoff e retome", "at": "grave um handoff"}], "done_at": "limpe a conversa e retome"},
]}
S["10"] = {"shots": [
    img("10-delegar.png", "Para dividir o trabalho", "subagente **ou** fork"),
    {"type": "compare", "at": "subagente começa do zero",
     "left": {"title": "Subagente", "at": "subagente começa", "tone": "neutral", "lines": [{"text": "começa **do zero**", "at": "começa do zero"}, {"text": "devolve **o resultado**", "at": "devolve só o resultado"}]},
     "right": {"title": "Fork", "at": "Fork é uma cópia", "tone": "good", "lines": [{"text": "sabe **tudo**", "at": "sabe tudo"}, {"text": "aproveita o **cache**", "at": "aproveita o cache"}]}},
    {"type": "keyword", "at": "Para pesquisa pesada", "text": "Vários agentes", "sub": "tamanho do fluxo: **pequeno**", "sub_at": "tamanho do fluxo em pequeno"},
]}
S["11"] = {"shots": [
    img("c5-sem-voce.png", "Quinta camada", "camada 5 · **sem você**"),
    {"type": "fields", "at": "podem acordar com um evento", "title": "Rotinas por evento", "fields": [
        {"label": "Pedido web", "value": "dispara", "at": "um pedido web"},
        {"label": "Pull request", "value": "dispara", "at": "um pull request novo"}]},
    img("c5-sem-voce.png", "notebook fechado", "**--cloud** e **--teleport**", focus=(0.6, 0.4), zoom=(1.12, 1.18), prev=((0.5, 0.5), 1.06)),
    {"type": "statement", "at": "só deixe rodar sozinho", "text": "Sozinho só com **verificação**", "then": {"text": "token = **senha**", "at": "como senha"}},
]}
S["12"] = {"shots": [
    img("c6-fim.png", "Resumindo", "menos instrução, **mais prova**"),
    {"type": "fields", "at": "skill só com o que ele erra", "title": "Para lembrar", "fields": [
        {"label": "Skill", "value": "só o que ele erra", "at": "skill só com"},
        {"label": "Modelo", "value": "um por trabalho", "at": "um modelo por trabalho"},
        {"label": "Prova", "value": "em vez de promessa", "at": "prova em vez de promessa"},
        {"label": "Sem você", "value": "só com verificação", "at": "trabalho sozinho"}]},
    img("11-guia.png", "O kit com os quinze", "**inema.club** · kit grátis", zoom=(1.0, 1.05)),
]}
# conferência das deixas
erros = []
for k, sc in S.items():
    fala = norm(rot[int(k) - 1]["speech"])
    for sh in sc["shots"]:
        def ver(v):
            if v in ("@start",) or v is None:
                return
            c, _, n = v.partition("#")
            if norm(c) not in fala:
                erros.append(f"cena {k}: deixa '{v}' não está na fala")
        def anda(o):
            if isinstance(o, dict):
                for kk, vv in o.items():
                    if (kk == "at" or kk.endswith("_at")) and isinstance(vv, str):
                        ver(vv)
                    else:
                        anda(vv)
            elif isinstance(o, list):
                for x in o:
                    anda(x)
        anda(sh)
for k, sc in S.items():
    t = rot[int(k) - 1]
    sc.setdefault("takeaway", t["takeaway"])
(OUT / "visual/pt-b01.json").write_text(json.dumps({"block": "pt-b01", "scenes": S}, ensure_ascii=False, indent=1))
print("\n".join(erros) or "deixas OK", "| cenas", len(S), "| shots", sum(len(s["shots"]) for s in S.values()))
sys.exit(1 if erros else 0)
