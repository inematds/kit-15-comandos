#!/usr/bin/env python3
"""Gera o guia (página única) em PT/EN/ES a partir de src/<lang>.json.

  python3 src/build.py   -> guia/index.html, guia/en/index.html, guia/es/index.html
O texto mora só nos JSON; HTML e CSS saem daqui. Vídeos: src/videos.json (opcional).
"""
import html, json, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SRC = RAIZ / "src"
SLUG = "kit-15-comandos"
REPO = f"https://github.com/inematds/{SLUG}"
SITE = f"https://inematds.github.io/{SLUG}/guia/"
ZIP = f"{REPO}/releases/download/kit-v1.0.0/{SLUG}.zip"
LANGS = ["pt", "en", "es"]
CSS = (SRC / "base.css.html").read_text()
EXTRA_CSS = """<style>
  .camada{padding:30px 0;border-top:1px solid var(--line)} .camada:first-of-type{border-top:none}
  .cab{display:grid;grid-template-columns:1fr 1.2fr;gap:26px;align-items:center;margin-bottom:20px}
  @media(max-width:820px){.cab{grid-template-columns:1fr}}
  .ill{margin:0;border-radius:14px;overflow:hidden;border:1px solid var(--line)}
  .ill img{width:100%;display:block;aspect-ratio:16/9;object-fit:cover}
  .cab h3{font-size:1.5rem;margin:.2em 0 .3em} .cab p{color:var(--mut);margin:0}
  .rot{font-family:Sora;font-weight:800;color:var(--amb);font-size:.85rem;letter-spacing:.1em;text-transform:uppercase}
  .dicas{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
  .dica{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;min-width:0;display:flex;flex-direction:column;gap:8px}
  .dica .top{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
  .dica .n{font:800 1.6rem/1 Sora;color:var(--amb);min-width:2ch}
  .dica h4{font:700 1.08rem/1.25 Sora;margin:0}
  .dica code.cmd{display:block;font-family:'JetBrains Mono',monospace;font-size:.86rem;background:rgba(250,204,21,.09);border:1px solid rgba(250,204,21,.35);border-radius:8px;padding:6px 10px;overflow-wrap:anywhere;color:var(--txt)}
  .st{font-size:.72rem;font-weight:600;border-radius:99px;padding:.2em .7em;white-space:nowrap}
  .st.ok{background:rgba(34,197,94,.14);color:#22c55e;border:1px solid rgba(34,197,94,.4)}
  .st.conferir{background:rgba(250,204,21,.12);color:var(--amb);border:1px solid rgba(250,204,21,.4)}
  body.light .st.conferir{color:#854d0e}
  .dica .lb{font:700 .74rem Sora;letter-spacing:.08em;text-transform:uppercase;color:var(--mut);margin-top:4px}
  .dica p{margin:0;color:var(--txt);font-size:.95rem}
  .dica ol{margin:0;padding-left:1.2em;font-size:.93rem} .dica ol li{margin:.25em 0}
  .dica .ln{display:flex;flex-wrap:wrap;gap:6px} .dica .ln a{font-size:.84rem;border:1px solid var(--line);border-radius:99px;padding:.2em .7em}
  .two{display:grid;grid-template-columns:1fr 1fr;gap:22px} @media(max-width:820px){.two{grid-template-columns:1fr}}
  .box{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px;min-width:0}
  .box h3{font-size:1.05rem;margin-bottom:.4em} .box p{color:var(--mut);margin:.2em 0 .8em}
  .box pre{white-space:pre-wrap;overflow-wrap:anywhere;margin:0}
  .copy{margin-top:12px;font-size:.85rem;padding:.45em .9em}
  .modelos{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px}
  .dl{display:flex;gap:12px;flex-wrap:wrap;margin:6px 0 24px}
  ul.arq{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:10px} @media(max-width:700px){ul.arq{grid-template-columns:1fr}}
  ul.arq li{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;display:flex;flex-direction:column;min-width:0}
  ul.arq code{font-family:'JetBrains Mono',monospace;font-size:.86rem;color:var(--amb);overflow-wrap:anywhere} ul.arq span{color:var(--mut);font-size:.9rem}
  body.light ul.arq code{color:#854d0e}
  .grid.g3{grid-template-columns:repeat(3,1fr)} @media(max-width:900px){.grid.g3{grid-template-columns:1fr 1fr}} @media(max-width:560px){.grid.g3{grid-template-columns:1fr}}
  .kitf .eixo{color:var(--amb);font-size:.84rem;margin-top:.5em} body.light .kitf .eixo{color:#854d0e}
  .grupos{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}
  .grupo h3{font-size:1rem;margin:0 0 .5em} .grupo a{display:block;padding:.3em 0;border-bottom:1px solid var(--line);font-size:.93rem}
  .vids{display:grid;grid-template-columns:2fr 1fr;gap:20px;align-items:start} @media(max-width:820px){.vids{grid-template-columns:1fr}}
  .vids video{width:100%;border-radius:14px;border:1px solid var(--line);background:#000;display:block}
  .vids .v916 video{max-width:360px;margin:0 auto}
  .vids h3{font-size:1rem;margin:0 0 .6em} .vids p{margin:.6em 0 0;font-size:.88rem}
  table.cola{width:100%;border-collapse:collapse} table.cola td{padding:12px;border-bottom:1px solid var(--line)} table.cola td:first-child{font-family:Sora;font-weight:800;color:var(--amb);white-space:nowrap}
  body.light table.cola td:first-child{color:#854d0e}
  .tip{border-left:3px solid var(--amb);background:rgba(250,204,21,.08);padding:12px 16px;border-radius:0 10px 10px 0;margin:14px 0 0;color:var(--txt)}
</style>"""


def esc(s):
    return html.escape(s, quote=False)


def construir(lang, videos):
    d = json.loads((SRC / f"{lang}.json").read_text())
    base = RAIZ / "guia" / ("" if lang == "pt" else lang)
    a0 = "assets/" if lang == "pt" else "../assets/"
    up = "" if lang == "pt" else "../"
    sfx = "" if lang == "pt" else f"-{lang}"
    nav = d["nav"]
    secoes = [("tese", nav["tese"]), ("dicas", nav["dicas"]), ("kit", nav["kit"]), ("comunidade", nav["comunidade"])] + ([("video", nav["video"])] if videos else [])
    links = "".join(f'<a class="sec" href="#{a}">{esc(t)}</a>' for a, t in secoes)
    seletor = "".join(f'<a{" class=\"on\"" if l == lang else ""} href="{(up + ("" if l == "pt" else l + "/")) or "./"}">{l.upper()}</a>' for l in LANGS)
    alt = "".join(f'<link rel="alternate" hreflang="{"pt-BR" if l == "pt" else l}" href="{SITE}{"" if l == "pt" else l + "/"}">' for l in LANGS)
    h, t, k, cu, ks, co, f, st = d["hero"], d["tese"], d["kit"], d["cuidados"], d["kits"], d["comunidade"], d["fim"], d["status"]
    fig = lambda src, altt: f'<figure class="ill"><img src="{a0}{src}" alt="{html.escape(altt)}" loading="lazy"></figure>'
    cards = "".join(f'<div class="card"><h3>{e} {esc(a)}</h3><p>{esc(b)}</p></div>' for e, a, b in t["cards"])

    def dica(x):
        como = "".join(f"<li>{esc(i)}</li>" for i in x["como"])
        ln = "".join(f'<a href="{u}" target="_blank" rel="noopener">{esc(a)} ↗</a>' for a, u in x["inema"])
        return f"""<article class="dica" id="d{x['n']}">
  <div class="top"><span class="n">{x['n']}</span><h4>{esc(x['titulo'])}</h4><span class="st {x['st']}">{esc(st[x['st']])}</span></div>
  <code class="cmd">{esc(x['cmd'])}</code>
  <div class="lb">{esc(d['rot_mudou'])}</div><p>{esc(x['mudou'])}</p>
  <div class="lb">{esc(d['rot_como'])}</div><ol>{como}</ol>
  <div class="lb">{esc(d['rot_inema'])}</div><div class="ln">{ln}</div>
</article>"""

    camadas = "".join(f"""<div class="camada" id="{c['id']}">
  <div class="cab">{fig(c['img'], c['img_alt'])}<div><span class="rot">{esc(d['camada_rot'])} {i}</span><h3>{esc(c['nome'])}</h3><p>{esc(c['intro'])}</p></div></div>
  <div class="dicas">{''.join(dica(x) for x in c['dicas'])}</div>
</div>""" for i, c in enumerate(d["camadas"], 1))
    arquivos = "".join(f'<li><code>{esc(a)}</code><span>{esc(b)}</span></li>' for a, b in k["arquivos"])
    modelos = "".join(f"""<div class="box"><span class="chip">{esc(m['quem'])}</span><h3>{esc(m['titulo'])}</h3><p>{esc(m['p'])}</p><pre id="m{n}">{esc(m['txt'])}</pre>
      <button class="btn copy" data-alvo="m{n}">{esc(k['copiar'])}</button></div>""" for n, m in enumerate(k["modelos"]))
    cuid = "".join(f'<div class="card"><h3>{e} {esc(a)}</h3><p>{esc(b)}</p></div>' for e, a, b in cu["itens"])
    kitsf = "".join(f'<div class="card kitf"><h3>{esc(a)}</h3><p>{esc(b)}</p><p class="eixo">↳ {esc(c)}</p></div>' for a, b, c in ks["itens"])
    grupos = "".join(f'<div class="box grupo"><h3>{esc(g)}</h3>{"".join(f"<a href=\"{u}\" target=\"_blank\" rel=\"noopener\">{esc(a)} ↗</a>" for a, u in itens)}</div>' for g, itens in co["grupos"])
    linhas = "".join(f'<tr><td>{esc(a)}</td><td>{esc(b)}</td></tr>' for a, b in f["linhas"])
    vid = ""
    if videos:
        v = d["video"]
        yt = lambda key: f' · <a href="{videos[key]}">YouTube</a>' if videos.get(key) else ""
        vid = f"""<section id="video"><div class="wrap">
  <span class="chip">{esc(v['chip'])}</span><h2>{esc(v['h2'])}</h2><p class="sub">{esc(v['sub'])}</p>
  <div class="vids">
    <div><h3>{esc(v['longo'])}</h3><video controls preload="metadata" playsinline poster="{a0}{videos['poster']}"><source src="{videos['longo']}" type="video/mp4"></video>
      <p><a href="{videos['longo']}">{esc(v['baixar'])}</a>{yt('yt_longo')}</p></div>
    <div class="v916"><h3>{esc(v['reel'])}</h3><video controls preload="metadata" playsinline poster="{a0}{videos['poster_reel']}" style="aspect-ratio:9/16;object-fit:cover"><source src="{videos['reel']}" type="video/mp4"></video>
      <p><a href="{videos['reel']}">{esc(v['baixar'])}</a>{yt('yt_reel')}</p></div>
  </div>
</div></section>"""
    corpo = f"""
<header class="hero" id="top">
  <div class="glow"></div>
  <div class="wrap">
    <div>
      <span class="chip">{esc(h['chip'])}</span>
      <h1>{h['h1']}</h1>
      <p class="lead">{esc(h['lead'])}</p>
      <div class="cta"><a class="btn" href="#dicas">{esc(h['cta1'])}</a><a class="btn ghost" href="{ZIP}">{esc(h['cta2'])}</a></div>
    </div>
    <figure><img src="{a0}banner{sfx}.jpg" alt="{html.escape(h['alt'])}"></figure>
  </div>
</header>
<section id="resumo" class="resumo"><div class="wrap"><span class="chip">{esc(d['resumo_chip'])}</span><p>{esc(d['resumo'])}</p></div></section>
<section id="tese"><div class="wrap">
  <span class="chip">{esc(t['chip'])}</span><h2>{esc(t['h2'])}</h2><p class="sub">{esc(t['sub'])}</p>
  <figure style="margin:0 0 26px;border-radius:16px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 80px -30px #000"><img src="{a0}banner-grade{sfx}.jpg" alt="{html.escape(t['alt_grade'])}" loading="lazy" style="width:100%;display:block"></figure>
  <div class="grid g3">{cards}</div>
</div></section>
<section id="dicas"><div class="wrap">
  <span class="chip">{esc(d['dicas_chip'])}</span><h2>{esc(d['dicas_h2'])}</h2><p class="sub">{esc(d['dicas_sub'])}</p>
  {camadas}
</div></section>
<section id="kit"><div class="wrap">
  <span class="chip">{esc(k['chip'])}</span><h2>{esc(k['h2'])}</h2><p class="sub">{esc(k['sub'])}</p>
  <div class="dl"><a class="btn" href="{ZIP}">⬇ {esc(k['baixar'])}</a><a class="btn ghost" href="{REPO}/tree/main/kit" target="_blank" rel="noopener">{esc(k['ver'])}</a></div>
  <h3 style="margin:0 0 12px">{esc(k['arquivos_h3'])}</h3><ul class="arq">{arquivos}</ul>
  <h3 style="margin:30px 0 12px">{esc(k['modelos_h3'])}</h3><div class="modelos">{modelos}</div>
</div></section>
<section id="cuidados"><div class="wrap">
  <span class="chip">{esc(cu['chip'])}</span><h2>{esc(cu['h2'])}</h2>
  <div class="grid g3" style="margin-top:18px">{cuid}</div>
</div></section>
<section id="kits"><div class="wrap">
  <span class="chip">{esc(ks['chip'])}</span><h2>{esc(ks['h2'])}</h2><p class="sub">{esc(ks['sub'])}</p>
  <div class="grid g3">{kitsf}</div>
</div></section>
<section id="comunidade"><div class="wrap">
  <span class="chip">{esc(co['chip'])}</span><h2>{esc(co['h2'])}</h2><p class="sub">{esc(co['sub'])}</p>
  <div class="grupos">{grupos}</div>
</div></section>
{vid}
<section id="fim"><div class="wrap">
  <span class="chip">{esc(f['chip'])}</span><h2>{esc(f['h2'])}</h2>
  <div class="two" style="align-items:center;margin-top:18px">{fig(f['img'], f['img_alt'])}<div class="box"><table class="cola">{linhas}</table></div></div>
  <p class="tip" style="margin-top:22px"><strong>{esc(f['frase'])}</strong></p>
</div></section>
"""
    pagina = f"""<!DOCTYPE html>
<html lang="{d['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(d['title'])} — {esc(d['tagline'])}</title>
<meta name="description" content="{html.escape(d['meta'])}">
{alt}
<meta property="og:title" content="{html.escape(d['title'])} — {html.escape(d['tagline'])}">
<meta property="og:description" content="{html.escape(d['meta'])}">
<meta property="og:image" content="{SITE}assets/banner{sfx}.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
{CSS}
{EXTRA_CSS}
</head>
<body>
<nav><div class="wrap">
  <a class="brand" href="./"><span class="emoji">⌨️</span> {esc(d['title'])}</a>
  <span class="sep">|</span>
  <span class="clubpro">
    <a class="inema" href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a>
    <span class="sep">-</span>
    <a class="pro" href="https://inema.pro" target="_blank" rel="noopener">PRO</a>
  </span>
  <div class="links">
    {links}
    <span class="lang">{seletor}</span>
    <button class="tgl" id="themeToggle" aria-label="{esc(nav['tema'])}" title="{esc(nav['tema'])}">🌙</button>
    <a class="btn" href="{REPO}" target="_blank" rel="noopener">{esc(nav['github'])}</a>
  </div>
</div></nav>
{corpo}
<footer>
  <div class="wrap">
    {"".join(f'<div class="pill">{esc(s)}</div>' for s in d['footer']['stack'])}
    <p style="margin-top:18px">{esc(d['title'])} · {esc(d['footer']['nota'])} · <a href="{REPO}">inematds/{SLUG}</a> · <a href="https://inema.club">INEMA.CLUB</a></p>
  </div>
</footer>
<script>
  (function(){{
    var KEY='{SLUG}-theme', b=document.body, tg=document.getElementById('themeToggle');
    try{{ if(localStorage.getItem(KEY)==='light'){{ b.classList.add('light'); tg.textContent='☀️'; }} }}catch(e){{}}
    tg.addEventListener('click',function(){{ var light=b.classList.toggle('light'); tg.textContent=light?'☀️':'🌙'; try{{ localStorage.setItem(KEY, light?'light':'dark'); }}catch(e){{}} }});
    document.querySelectorAll('.copy').forEach(function(bt){{
      bt.addEventListener('click',function(){{
        var txt=document.getElementById(bt.dataset.alvo).innerText;
        (navigator.clipboard?navigator.clipboard.writeText(txt):Promise.reject()).then(function(){{ var o=bt.textContent; bt.textContent='{esc(k['copiado'])} ✓'; setTimeout(function(){{bt.textContent=o;}},1600); }}).catch(function(){{}});
      }});
    }});
  }})();
</script>
</body>
</html>
"""
    base.mkdir(parents=True, exist_ok=True)
    (base / "index.html").write_text(pagina)


if __name__ == "__main__":
    vf = SRC / "videos.json"
    videos = json.loads(vf.read_text()) if vf.exists() else None
    for l in LANGS:
        if (SRC / f"{l}.json").exists():
            construir(l, videos); print("ok", l)
