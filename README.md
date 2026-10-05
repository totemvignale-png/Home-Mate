# mate&dintorni

Home page animata che raccoglie i 6 siti di mate&dintorni come tasti cliccabili.

È un singolo file statico: apri `index.html` nel browser o pubblicalo su qualsiasi hosting statico (GitHub Pages, Netlify, ecc.).

## Modificare i siti

In `index.html`, cerca l'array `SITES` all'inizio dello `<script>` e cambia per ciascun sito:

- `name` – nome mostrato sulla card
- `tag` – piccola formula in alto
- `desc` – descrizione breve
- `url` – indirizzo del sito
- `curve` – animazione della card: `sine`, `rose`, `parabola`, `spiral`, `gauss`, `lissajous`
- `sym` – simbolo decorativo sullo sfondo della card

## Effetti

- titolo che entra lettera per lettera, con la `&` in gradiente rotante
- curve parametriche (rose, Lissajous, spirografo, farfalla) che si disegnano sullo sfondo e seguono il mouse
- card con tilt 3D, luce che segue il cursore, bordo luminoso, ripple al clic e curva che si ridisegna al passaggio
- formula che cambia nell'intestazione e nastro scorrevole di formule celebri
- scorciatoie da tastiera `1`–`6` per aprire i siti
- rispetta `prefers-reduced-motion` e funziona su mobile
