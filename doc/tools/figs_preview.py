"""Genera páginas de prueba con todos los diagramas SVG de index.html en su estado final.

Uso (desde la raíz del proyecto):
    python3 -I doc/tools/figs_preview.py
    google-chrome --headless=new --no-sandbox --hide-scrollbars --window-size=1360,1600 \
        --virtual-time-budget=3000 --screenshot=figs_0.png "file://$PWD/doc/tools/out/figs_0.html"

Sirve para revisar solapamientos de texto en los diagramas sin tener que scrollear.
Con el argumento «dark» genera las páginas en modo oscuro.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "doc", "tools", "out")
os.makedirs(OUT, exist_ok=True)
dark = "dark" in sys.argv[1:]

s = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
head = s[: s.index('<header class="topbar"')]
if dark:
    head = head.replace('<html lang="es">', '<html lang="es" data-theme="dark">')
svgs = [x for x in re.findall(r"<svg viewBox=.*?</svg>", s, flags=re.S) if "aria-label" in x]
print(len(svgs), "diagramas")

for f in os.listdir(OUT):
    if f.startswith("figs_"):
        os.remove(os.path.join(OUT, f))
for part in range(0, len(svgs), 6):
    body = "".join(
        '<div class="card" style="margin:8px;width:640px;display:inline-block;vertical-align:top">'
        '<div class="sans" style="font-size:11px">#%d</div>%s</div>' % (i, svgs[i])
        for i in range(part, min(part + 6, len(svgs)))
    )
    html = (head + '<div style="width:1340px;padding:10px">' + body + "</div>"
            '<script>document.querySelectorAll("svg [data-s]").forEach(e=>e.classList.add("on"))</script></body></html>')
    open(os.path.join(OUT, "figs_%d.html" % (part // 6)), "w", encoding="utf-8").write(html)
