# mate&dintorni

Home page animata a tema spazio e infinito che raccoglie i 6 giochi di mate&dintorni come tasti cliccabili. Pensata per ragazzi di 12–13 anni.

È un singolo file statico: apri `index.html` nel browser o pubblicalo su qualsiasi hosting statico (GitHub Pages, Netlify, ecc.).

## Modificare i giochi

In `index.html`, cerca l'array `SITES` all'inizio dello `<script>` e cambia per ciascun sito:

- `name` – nome mostrato sulla card
- `desc` – descrizione breve
- `url` – indirizzo del gioco (lascialo vuoto `""` per mostrare "link in arrivo")
- `tag` – categoria (Esplora, Codice, Arcade…)
- `img` – immagine di copertina della card (formato 1200×680)
- `sym` – simbolo decorativo sullo sfondo della card

## Effetti

- titolo che entra lettera per lettera, con la `&` in gradiente rotante e un grande ∞ percorso da una cometa
- campo stellare 3D che segue il mouse e passa in iperspazio quando si punta un gioco
- card con tilt 3D, luce che segue il cursore, bordo luminoso, navicella che percorre il disegno, ripple e scintille al clic
- curiosità sull'infinito che cambiano nell'intestazione e nastro scorrevole di paradossi famosi
- scorciatoie da tastiera `1`–`6` per aprire i siti
- rispetta `prefers-reduced-motion` e funziona su mobile

## Immagini

Le copertine sono in `img/` e sono tutte nello stesso stile (nebulosa, stelle, bagliore, grana e cornice HUD).
Le genera `tools/genera-copertine.js`, che disegna le scene di `tools/copertine.html`:

```
npm i -D playwright && npx playwright install chromium
node tools/genera-copertine.js
```

Aprendo `tools/copertine.html` nel browser vedi un'anteprima di tutte le scene.

### Usare lo screenshot vero di un gioco

Metti lo screenshot in `tools/screenshot/` con lo stesso nome della copertina, per esempio
`tools/screenshot/viaggio-infinito.png`, e rilancia lo script: la copertina viene rifatta dallo
screenshot, trasformata nello stesso stile delle altre (bicromia con il colore del gioco, effetto ologramma, cornice).

Per far scattare lo screenshot direttamente allo script, dai giochi che hanno già un indirizzo:

```
node tools/genera-copertine.js --cattura
```

## Build Fight 1v1

In `buildfight/index.html` c'è un gioco 3D in stile Fortnite: una mappa da build fight 1v1 in cui sfidi un bot (Facile, Normale o Difficile) oppure ti alleni da solo contro un manichino.

- griglia di costruzione come in Fortnite: **Q** muro, **E** rampa, **C** pavimento, clic sinistro per piazzare (tieni premuto per costruire veloce)
- **1** piccone, **2** pompa, **3** fucile d'assalto, **R** ricarica, clic destro per mirare
- **Shift** per accovacciarsi; premuto mentre corri fa scivolare (in discesa sulle rampe acceleri, saltando tieni la velocità)
- **F** modifica i tuoi muri (3×3 riquadri) e pavimenti (2×2): trascina sui riquadri e rilascia per fare porte, finestre e archi, tasto destro ripristina
- mira precisa: mirino che mostra la dispersione reale, primo colpo perfetto da fermo mirando o accovacciato, rosa fissa della pompa, mouse senza accelerazione
- scudo e vita, colpi alla testa, danno da caduta, costruzioni che si rinforzano dopo essere piazzate e crollano se perdono la base
- il bot spara, si copre con muri e rampe e fa ramp rush per prenderti l'altezza
- round al meglio di 3, 5 o 7

Si gioca con tastiera e mouse: apri il file nel browser (serve la connessione per caricare three.js dal CDN).
