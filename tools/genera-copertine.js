// Genera le copertine dei giochi in img/*.jpg usando tools/copertine.html.
//
//   node tools/genera-copertine.js
//
// Se esiste tools/screenshot/<nome>.png (o .jpg), quella copertina viene creata
// dallo screenshot vero, trasformato nello stesso stile delle altre.
// Con --cattura prova anche a fotografare da solo i siti che hanno un indirizzo.
//
// Richiede Playwright: npm i -D playwright && npx playwright install chromium

const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const ROOT = path.join(__dirname, "..");
const SHOTS = path.join(__dirname, "screenshot");

const GIOCHI = [
  { nome: "viaggio-infinito", accento: "#b48cff", codice: "M-01 · ESPLORA", url: "https://infinito-mate.netlify.app" },
  { nome: "toy-story", accento: "#ffb84d", codice: "M-02 · AVVENTURA" },
  { nome: "razzo-codice", accento: "#7ee0b5", codice: "M-03 · CODICE" },
  { nome: "asteroidi", accento: "#6fb6ff", codice: "M-04 · ARCADE" },
  { nome: "orbita", accento: "#ff7a59", codice: "M-05 · ARCADE" },
  { nome: "iperspazio", accento: "#ff6fae", codice: "M-06 · ARCADE" },
];

function trovaScreenshot(nome) {
  for (const ext of ["png", "jpg", "jpeg", "webp"]) {
    const f = path.join(SHOTS, `${nome}.${ext}`);
    if (fs.existsSync(f)) return f;
  }
  return null;
}

(async () => {
  const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});

  if (process.argv.includes("--cattura")) {
    fs.mkdirSync(SHOTS, { recursive: true });
    for (const g of GIOCHI.filter(g => g.url)) {
      const page = await browser.newPage({ viewport: { width: 1440, height: 816 }, deviceScaleFactor: 1 });
      try {
        await page.goto(g.url, { waitUntil: "networkidle", timeout: 30000 });
        await page.waitForTimeout(2500);
        await page.screenshot({ path: path.join(SHOTS, `${g.nome}.png`) });
        console.log(`screenshot ${g.nome}: ok`);
      } catch (e) {
        console.log(`screenshot ${g.nome}: non riuscito (${e.message.split("\n")[0]})`);
      }
      await page.close();
    }
  }

  fs.mkdirSync(path.join(ROOT, "img"), { recursive: true });
  const page = await browser.newPage();
  await page.addInitScript(() => { window.__headless = true; });
  await page.goto("file://" + path.join(__dirname, "copertine.html"));

  for (const g of GIOCHI) {
    const shot = trovaScreenshot(g.nome);
    const screenshot = shot && {
      dataUrl: `data:image/${path.extname(shot).slice(1).replace("jpg", "jpeg")};base64,` + fs.readFileSync(shot).toString("base64"),
      accento: g.accento, codice: g.codice,
    };
    const dataUrl = await page.evaluate(async ({ nome, screenshot }) => (await genera(nome, screenshot)).toDataURL("image/jpeg", .88), { nome: g.nome, screenshot });
    fs.writeFileSync(path.join(ROOT, "img", `${g.nome}.jpg`), Buffer.from(dataUrl.split(",")[1], "base64"));
    console.log(`copertina ${g.nome}: ${shot ? "da screenshot" : "illustrata"}`);
  }
  await browser.close();
})();
