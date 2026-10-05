# mate&dintorni

Home page animata a tema spazio e infinito che raccoglie i 6 giochi di mate&dintorni come tasti cliccabili. Pensata per ragazzi di 12–13 anni.

È un singolo file statico: apri `index.html` nel browser o pubblicalo su qualsiasi hosting statico (GitHub Pages, Netlify, ecc.).

## Modificare i giochi

In `index.html`, cerca l'array `SITES` all'inizio dello `<script>` e cambia per ciascun sito:

- `name` – nome mostrato sulla card
- `desc` – descrizione breve
- `url` – indirizzo del gioco (lascialo vuoto `""` per mostrare "link in arrivo")
- `tag` – categoria (Esplora, Codice, Arcade…)
- `img` – immagine di copertina della card (formato consigliato 600×340)
- `sym` – simbolo decorativo sullo sfondo della card

## Effetti

- titolo che entra lettera per lettera, con la `&` in gradiente rotante e un grande ∞ percorso da una cometa
- campo stellare 3D che segue il mouse e passa in iperspazio quando si punta un gioco
- card con tilt 3D, luce che segue il cursore, bordo luminoso, navicella che percorre il disegno, ripple e scintille al clic
- curiosità sull'infinito che cambiano nell'intestazione e nastro scorrevole di paradossi famosi
- scorciatoie da tastiera `1`–`6` per aprire i siti
- rispetta `prefers-reduced-motion` e funziona su mobile

## Immagini

Le copertine animate dei giochi sono in `img/` e sono generate da `tools/genera-immagini.py`:

```
python3 tools/genera-immagini.py
```

Per usare uno screenshot vero di un gioco, mettilo in `img/` (png, jpg o gif, meglio se 600×340 o più grande con le stesse proporzioni) e cambia il campo `img` di quel gioco in `index.html`.
