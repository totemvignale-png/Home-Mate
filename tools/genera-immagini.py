"""Genera le copertine SVG animate dei 6 giochi in img/. Uso: python3 tools/genera-immagini.py"""
import math, random, os

W, H = 600, 340
OUT = os.path.join(os.path.dirname(__file__), "..", "img")


def stars(seed, n=90, area=(0, 0, W, H), colors=("#ffffff", "#cfe0ff", "#ffe3b0")):
    rnd = random.Random(seed)
    x0, y0, x1, y1 = area
    out = []
    for i in range(n):
        x, y = rnd.uniform(x0, x1), rnd.uniform(y0, y1)
        r = rnd.choice([.6, .8, 1, 1, 1.3, 1.8])
        c = rnd.choice(colors)
        tw = ""
        if i % 5 == 0:
            d = rnd.uniform(1.5, 4)
            tw = f'<animate attributeName="opacity" values="1;.2;1" dur="{d:.1f}s" repeatCount="indefinite" begin="{rnd.uniform(0, 3):.1f}s"/>'
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{c}" opacity="{rnd.uniform(.4, 1):.2f}">{tw}</circle>')
    return "".join(out)


def lemni(cx, cy, a, ky=1, n=240):
    pts = []
    for k in range(n + 1):
        u = k / n * 2 * math.pi
        d = 1 + math.sin(u) ** 2
        pts.append((cx + a * math.cos(u) / d, cy + ky * a * math.sin(u) * math.cos(u) / d))
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + "Z"


def svg(body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f"<defs>{defs}</defs>{body}</svg>")


SHIP = '<path d="M14 0 L-10 -9 L-5 0 L-10 9 Z" fill="#fff"/><path d="M-6 -3 L-18 0 L-6 3 Z" fill="#ffb84d"><animate attributeName="opacity" values="1;.5;1" dur=".25s" repeatCount="indefinite"/></path>'

# ---------------------------------------------------------------- 1. Viaggio nell'infinito
def infinito():
    defs = """
    <radialGradient id="bg" cx="50%" cy="50%" r="70%"><stop offset="0" stop-color="#2a1a5e"/><stop offset=".6" stop-color="#110a2e"/><stop offset="1" stop-color="#05040f"/></radialGradient>
    <linearGradient id="inf" x1="0" x2="1"><stop offset="0" stop-color="#b48cff"/><stop offset=".5" stop-color="#6fb6ff"/><stop offset="1" stop-color="#ff6fae"/></linearGradient>
    <filter id="glow" x="-20%" y="-40%" width="140%" height="180%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <radialGradient id="pl" cx="35%" cy="30%" r="70%"><stop offset="0" stop-color="#ffd59a"/><stop offset=".6" stop-color="#ff7a59"/><stop offset="1" stop-color="#5a1f3a"/></radialGradient>"""
    rings = ""
    for i, s in enumerate([1, .78, .6, .46, .35, .27, .2]):
        op = 1 - i * .13
        rings += f'<path d="{lemni(300, 170, 250 * s, 1.15)}" fill="none" stroke="url(#inf)" stroke-width="{max(1, 5 * s):.1f}" opacity="{op:.2f}"/>'
    main = lemni(300, 170, 250, 1.15)
    body = f"""<rect width="{W}" height="{H}" fill="url(#bg)"/>{stars(1, 120)}
    <circle cx="520" cy="62" r="34" fill="url(#pl)"/><ellipse cx="520" cy="62" rx="58" ry="11" fill="none" stroke="#ffd59a" stroke-width="2" opacity=".6" transform="rotate(-18 520 62)"/>
    <circle cx="70" cy="280" r="14" fill="#6fb6ff" opacity=".7"/>
    <g filter="url(#glow)">{rings}
      <g>{SHIP}<animateMotion dur="6s" repeatCount="indefinite" rotate="auto" path="{main}"/></g>
    </g>
    <text x="300" y="322" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-size="18" fill="#cfd5ff" opacity=".7">1, 2, 3, … ∞</text>"""
    return svg(body, defs)


# ---------------------------------------------------------------- 2. Toy Story
def toy():
    defs = """
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a7bd5"/><stop offset="1" stop-color="#8ec5ff"/></linearGradient>
    <linearGradient id="body" x1="0" x2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#cfd8ee"/></linearGradient>
    <radialGradient id="star" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff6c9"/><stop offset="1" stop-color="#ffb84d"/></radialGradient>
    <filter id="soft"><feGaussianBlur stdDeviation="1.2"/></filter>"""
    def cloud(x, y, s, dur):
        return (f'<g opacity=".95"><g transform="translate({x} {y}) scale({s})">'
                '<ellipse cx="0" cy="0" rx="46" ry="22" fill="#fff"/><circle cx="-22" cy="-12" r="20" fill="#fff"/>'
                '<circle cx="8" cy="-22" r="26" fill="#fff"/><circle cx="34" cy="-8" r="18" fill="#fff"/></g>'
                f'<animateTransform attributeName="transform" type="translate" values="0 0; 24 0; 0 0" dur="{dur}s" repeatCount="indefinite"/></g>')
    clouds = cloud(80, 70, 1, 14) + cloud(470, 50, .8, 18) + cloud(300, 300, 1.2, 16) + cloud(560, 250, .9, 12) + cloud(40, 250, .7, 20)
    star_pts = " ".join(f"{470 + (34 if k % 2 == 0 else 14) * math.cos(-math.pi / 2 + k * math.pi / 5):.1f},{110 + (34 if k % 2 == 0 else 14) * math.sin(-math.pi / 2 + k * math.pi / 5):.1f}" for k in range(10))
    rocket = """
      <g transform="rotate(35)">
        <path d="M0 -62 C 22 -40 24 -6 20 30 L -20 30 C -24 -6 -22 -40 0 -62 Z" fill="url(#body)" stroke="#1d2b55" stroke-width="3"/>
        <path d="M0 -62 C 12 -50 16 -40 17 -32 L -17 -32 C -16 -40 -12 -50 0 -62 Z" fill="#ff5a4e" stroke="#1d2b55" stroke-width="3"/>
        <circle cx="0" cy="-8" r="10" fill="#6fb6ff" stroke="#1d2b55" stroke-width="3"/>
        <path d="M-20 10 L -38 38 L -20 30 Z M20 10 L 38 38 L 20 30 Z" fill="#7ee0b5" stroke="#1d2b55" stroke-width="3" stroke-linejoin="round"/>
        <rect x="-12" y="30" width="24" height="8" rx="2" fill="#1d2b55"/>
        <path d="M-10 40 Q 0 80 10 40 Z" fill="#ffb84d"><animate attributeName="d" values="M-10 40 Q 0 80 10 40 Z;M-10 40 Q 0 64 10 40 Z;M-10 40 Q 0 80 10 40 Z" dur=".3s" repeatCount="indefinite"/></path>
        <path d="M-5 40 Q 0 60 5 40 Z" fill="#fff6c9"/>
      </g>"""
    body = f"""<rect width="{W}" height="{H}" fill="url(#sky)"/>{clouds}
    <path d="M60 330 C 140 300, 200 260, 270 190" fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="2 12" stroke-linecap="round" opacity=".9">
      <animate attributeName="stroke-dashoffset" values="0;-28" dur=".8s" repeatCount="indefinite"/></path>
    <g transform="translate(300 170)">{rocket}<animateTransform attributeName="transform" type="translate" values="300 170; 306 162; 300 170" dur="1.6s" repeatCount="indefinite"/></g>
    <g><polygon points="{star_pts}" fill="url(#star)" stroke="#c97a00" stroke-width="2.5" stroke-linejoin="round"/>
      <animateTransform attributeName="transform" type="rotate" values="0 470 110; 12 470 110; 0 470 110" dur="3s" repeatCount="indefinite"/></g>
    <g transform="translate(40 268)"><rect width="52" height="52" rx="6" fill="#ff5a4e" stroke="#1d2b55" stroke-width="3"/><text x="26" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="36" font-weight="700" fill="#fff">∞</text></g>
    <g transform="translate(96 284) rotate(-8)"><rect width="40" height="40" rx="5" fill="#ffb84d" stroke="#1d2b55" stroke-width="3"/><text x="20" y="30" text-anchor="middle" font-family="Georgia, serif" font-size="26" font-weight="700" fill="#1d2b55">+1</text></g>"""
    return svg(body, defs)


# ---------------------------------------------------------------- 3. Razzo in codice
def codice():
    defs = """
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0c1a24"/><stop offset="1" stop-color="#06120f"/></linearGradient>
    <linearGradient id="fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff6c9"/><stop offset=".5" stop-color="#ffb84d"/><stop offset="1" stop-color="#ff5a4e" stop-opacity="0"/></linearGradient>"""
    lines = [
        ("razzo", " = ", "Razzo()", "#7ee0b5"),
        ("razzo.aggiungi", "(", "Motore(spinta=9000))", "#6fb6ff"),
        ("razzo.aggiungi", "(", "Serbatoio(litri=500))", "#6fb6ff"),
        ("razzo.aggiungi", "(", "Alette(n=3))", "#6fb6ff"),
        ("", "", "", ""),
        ("for", " t ", "in range(10, 0, -1):", "#ff6fae"),
        ("    print", "(", "t)", "#ffb84d"),
        ("razzo.lancia", "(", ")", "#7ee0b5"),
    ]
    code = ""
    for i, (a, b, c, col) in enumerate(lines):
        y = 92 + i * 24
        code += f'<text x="44" y="{y}" font-family="ui-monospace, Menlo, monospace" font-size="15" xml:space="preserve"><tspan fill="#4c6670">{i + 1:>2}  </tspan><tspan fill="{col}">{a}</tspan><tspan fill="#cfd8e6">{b}{c}</tspan></text>'
    blocks = ""
    parts = [(452, 230, 56, 40, "#cfd8e6"), (452, 190, 56, 40, "#eef1ff"), (460, 150, 40, 40, "#eef1ff"), (466, 126, 28, 24, "#ff5a4e")]
    for i, (x, y, w, h, c) in enumerate(parts):
        blocks += (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{c}" stroke="#0c1a24" stroke-width="3" opacity="0">'
                   f'<animate attributeName="opacity" values="0;1;1;1" keyTimes="0;.1;.9;1" dur="6s" begin="{i * .5}s" repeatCount="indefinite"/></rect>')
    body = f"""<rect width="{W}" height="{H}" fill="url(#bg)"/>{stars(3, 40, colors=("#7ee0b5", "#ffffff"))}
    <g><rect x="24" y="36" width="370" height="268" rx="12" fill="#0a141c" stroke="#1f3a3a" stroke-width="2"/>
      <rect x="24" y="36" width="370" height="30" rx="12" fill="#12232b"/><rect x="24" y="54" width="370" height="12" fill="#12232b"/>
      <circle cx="44" cy="51" r="5" fill="#ff5a4e"/><circle cx="62" cy="51" r="5" fill="#ffb84d"/><circle cx="80" cy="51" r="5" fill="#7ee0b5"/>
      <text x="210" y="56" text-anchor="middle" font-family="ui-monospace, Menlo, monospace" font-size="12" fill="#6b8a8a">razzo.py</text>
      {code}
      <rect x="128" y="257" width="9" height="18" fill="#7ee0b5"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect></g>
    <g>
      <g><animateTransform attributeName="transform" type="translate" values="0 0;0 0;0 -260" keyTimes="0;.7;1" dur="6s" repeatCount="indefinite" calcMode="spline" keySplines="0 0 1 1;.5 0 .9 .6"/>
        {blocks}
        <path d="M452 270 L 432 290 L 452 286 Z M508 270 L 528 290 L 508 286 Z" fill="#7ee0b5" stroke="#0c1a24" stroke-width="3"/>
        <circle cx="480" cy="170" r="9" fill="#6fb6ff" stroke="#0c1a24" stroke-width="3"/>
        <path d="M462 272 Q 480 330 498 272 Z" fill="url(#fl)" opacity="0"><animate attributeName="opacity" values="0;0;1;1" keyTimes="0;.55;.6;1" dur="6s" repeatCount="indefinite"/></path>
      </g>
      <rect x="420" y="300" width="120" height="10" rx="3" fill="#1f3a3a"/><rect x="430" y="310" width="8" height="30" fill="#1f3a3a"/><rect x="522" y="310" width="8" height="30" fill="#1f3a3a"/>
    </g>"""
    return svg(body, defs)


# ---------------------------------------------------------------- 4. Pioggia di asteroidi
def asteroidi():
    defs = """
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#050a1e"/><stop offset="1" stop-color="#0f2350"/></linearGradient>
    <radialGradient id="rock" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="#a7b3d6"/><stop offset=".6" stop-color="#5a6690"/><stop offset="1" stop-color="#262c4a"/></radialGradient>
    <linearGradient id="trail" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#6fb6ff" stop-opacity=".7"/><stop offset="1" stop-color="#6fb6ff" stop-opacity="0"/></linearGradient>"""
    rnd = random.Random(4)
    rocks = ""
    for i in range(9):
        x = rnd.uniform(30, 570); s = rnd.uniform(10, 30); dur = rnd.uniform(3, 6); beg = rnd.uniform(0, 5)
        pts = " ".join(f"{s * (.75 + .25 * rnd.random()) * math.cos(k * math.pi / 4):.1f},{s * (.75 + .25 * rnd.random()) * math.sin(k * math.pi / 4):.1f}" for k in range(8))
        rocks += (f'<g><g transform="rotate({-20 + rnd.uniform(-8, 8):.0f})"><rect x="{-s * .5:.1f}" y="{-s * 4:.1f}" width="{s:.1f}" height="{s * 3.5:.1f}" rx="{s * .5:.1f}" fill="url(#trail)"/></g>'
                  f'<polygon points="{pts}" fill="url(#rock)" stroke="#1a1f38" stroke-width="2"><animateTransform attributeName="transform" type="rotate" values="0;360" dur="{rnd.uniform(4, 9):.1f}s" repeatCount="indefinite"/></polygon>'
                  f'<animateMotion dur="{dur:.1f}s" begin="-{beg:.1f}s" repeatCount="indefinite" path="M{x:.0f} -60 L {x - 140:.0f} 400"/></g>')
    ship = """
    <g><animateTransform attributeName="transform" type="translate" values="230 270; 360 270; 290 270; 230 270" dur="4s" repeatCount="indefinite" calcMode="spline" keySplines=".4 0 .6 1;.4 0 .6 1;.4 0 .6 1"/>
      <path d="M0 -34 L 22 18 L 0 8 L -22 18 Z" fill="#eef1ff" stroke="#6fb6ff" stroke-width="2.5" stroke-linejoin="round"/>
      <path d="M0 -14 L 6 2 L -6 2 Z" fill="#6fb6ff"/>
      <path d="M-10 12 L 0 40 L 10 12 Z" fill="#ffb84d"><animate attributeName="opacity" values="1;.4;1" dur=".2s" repeatCount="indefinite"/></path>
      <rect x="-1.5" y="-110" width="3" height="40" rx="1.5" fill="#7ee0b5"><animate attributeName="y" values="-60;-340" dur=".7s" repeatCount="indefinite"/></rect>
    </g>"""
    body = f"""<rect width="{W}" height="{H}" fill="url(#bg)"/>{stars(5, 110)}{rocks}{ship}
    <text x="24" y="322" font-family="ui-monospace, Menlo, monospace" font-size="14" fill="#6fb6ff">PUNTI 004 210</text>
    <text x="576" y="322" text-anchor="end" font-family="ui-monospace, Menlo, monospace" font-size="14" fill="#ff6fae">♥ ♥ ♥</text>"""
    return svg(body, defs)


# ---------------------------------------------------------------- 5. Orbita perfetta
def orbita():
    defs = """
    <radialGradient id="bg" cx="40%" cy="55%" r="80%"><stop offset="0" stop-color="#2a1420"/><stop offset=".5" stop-color="#120a18"/><stop offset="1" stop-color="#06040c"/></radialGradient>
    <radialGradient id="planet" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="#ffd2a8"/><stop offset=".45" stop-color="#ff7a59"/><stop offset="1" stop-color="#4a1630"/></radialGradient>
    <radialGradient id="atmo" cx="50%" cy="50%" r="50%"><stop offset=".7" stop-color="#ff7a59" stop-opacity=".35"/><stop offset="1" stop-color="#ff7a59" stop-opacity="0"/></radialGradient>
    <radialGradient id="moon" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="#eef1ff"/><stop offset="1" stop-color="#6b7299"/></radialGradient>
    <clipPath id="pc"><circle cx="300" cy="175" r="70"/></clipPath>"""
    orbit = "M80 175 A 220 70 0 1 0 520 175 A 220 70 0 1 0 80 175 Z"
    body = f"""<rect width="{W}" height="{H}" fill="url(#bg)"/>{stars(6, 110)}
    <g transform="rotate(-10 300 175)">
      <path d="M80 175 A 220 70 0 0 1 520 175" fill="none" stroke="#ff7a59" stroke-width="1.5" stroke-dasharray="4 6" opacity=".5"/>
      <circle cx="300" cy="175" r="100" fill="url(#atmo)"/>
      <circle cx="300" cy="175" r="70" fill="url(#planet)"/>
      <g clip-path="url(#pc)" opacity=".35"><path d="M220 150 Q 300 135 380 150" stroke="#4a1630" stroke-width="8" fill="none"/><path d="M220 190 Q 300 205 380 188" stroke="#ffd2a8" stroke-width="6" fill="none"/><path d="M230 215 Q 300 228 370 214" stroke="#4a1630" stroke-width="5" fill="none"/></g>
      <path d="M520 175 A 220 70 0 0 1 80 175" fill="none" stroke="#ff7a59" stroke-width="2" stroke-dasharray="4 6"/>
      <g><g transform="scale(.9)">{SHIP}</g><animateMotion dur="5s" repeatCount="indefinite" rotate="auto" path="{orbit}"/></g>
    </g>
    <circle cx="510" cy="60" r="18" fill="url(#moon)"/>
    <g font-family="ui-monospace, Menlo, monospace" font-size="13" fill="#ffb59e">
      <text x="24" y="300">v = 7,9 km/s</text><text x="24" y="320" fill="#8f98c2">g = 9,81 m/s²</text></g>"""
    return svg(body, defs)


# ---------------------------------------------------------------- 6. Salto nell'iperspazio
def iperspazio():
    defs = """
    <radialGradient id="bg" cx="50%" cy="50%" r="70%"><stop offset="0" stop-color="#3a1240"/><stop offset=".4" stop-color="#140820"/><stop offset="1" stop-color="#04030a"/></radialGradient>
    <radialGradient id="core" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#ffffff"/><stop offset=".3" stop-color="#ffc2e0"/><stop offset="1" stop-color="#ff6fae" stop-opacity="0"/></radialGradient>
    <radialGradient id="eng" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff"/><stop offset=".5" stop-color="#6fb6ff"/><stop offset="1" stop-color="#6fb6ff" stop-opacity="0"/></radialGradient>"""
    rnd = random.Random(7)
    streaks = ""
    cols = ["#ff6fae", "#b48cff", "#6fb6ff", "#ffffff", "#ffffff"]
    for i in range(70):
        a = rnd.uniform(0, 2 * math.pi)
        r1 = rnd.uniform(20, 60); r2 = r1 + rnd.uniform(60, 260)
        x1, y1 = 300 + r1 * math.cos(a), 170 + r1 * math.sin(a) * .65
        x2, y2 = 300 + r2 * math.cos(a), 170 + r2 * math.sin(a) * .65
        dur = rnd.uniform(.6, 1.4); beg = rnd.uniform(0, 1.4)
        streaks += (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{rnd.choice(cols)}" stroke-width="{rnd.uniform(1, 3):.1f}" stroke-linecap="round" pathLength="100" stroke-dasharray="30 100">'
                    f'<animate attributeName="stroke-dashoffset" values="30;-100" dur="{dur:.2f}s" begin="-{beg:.2f}s" repeatCount="indefinite"/></line>')
    ship = """
    <g transform="translate(300 250)">
      <animateTransform attributeName="transform" type="translate" values="300 250; 304 246; 297 252; 300 250" dur="1.2s" repeatCount="indefinite"/>
      <path d="M-90 10 L -20 -14 L 20 -14 L 90 10 L 40 18 L -40 18 Z" fill="#1c1430" stroke="#b48cff" stroke-width="2.5" stroke-linejoin="round"/>
      <path d="M-20 -14 L -10 -32 L 10 -32 L 20 -14 Z" fill="#2a1f48" stroke="#b48cff" stroke-width="2.5" stroke-linejoin="round"/>
      <path d="M-8 -28 L 8 -28 L 12 -18 L -12 -18 Z" fill="#6fb6ff" opacity=".8"/>
      <circle cx="-30" cy="8" r="12" fill="url(#eng)"><animate attributeName="r" values="11;14;11" dur=".15s" repeatCount="indefinite"/></circle>
      <circle cx="30" cy="8" r="12" fill="url(#eng)"><animate attributeName="r" values="11;14;11" dur=".15s" repeatCount="indefinite" begin=".07s"/></circle>
    </g>"""
    body = f"""<rect width="{W}" height="{H}" fill="url(#bg)"/>
    <ellipse cx="300" cy="170" rx="90" ry="60" fill="url(#core)"><animate attributeName="rx" values="80;100;80" dur="2s" repeatCount="indefinite"/></ellipse>
    {streaks}{ship}
    <text x="576" y="322" text-anchor="end" font-family="ui-monospace, Menlo, monospace" font-size="14" fill="#ff6fae">VELOCITÀ ×∞</text>"""
    return svg(body, defs)


for name, fn in [("viaggio-infinito", infinito), ("toy-story", toy), ("razzo-codice", codice),
                 ("asteroidi", asteroidi), ("orbita", orbita), ("iperspazio", iperspazio)]:
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
        f.write(fn())
    print("ok", name)
