## Kisebbek száma
Egy űrhajó reaktorainak elegendő energiát kell termelniük a biztonságos utazáshoz. Indulás előtt a rendszer elemzi a teljesítményüket, és azokat az egységeket azonosítja, amelyek a kritikus küszöbérték alatt működnek.

Írj egy függvényt, amely megszámolja, hány reaktor teljesítménye van egy adott határ alatt egy listában.

### Sablon
Indulj ki az előre készített sablon kódból! Ne változtass a főprogramon semmit, mert különben nem lesz elfogadva. A `count_lower` függvényt kell megírnod, amely paraméterként a teljesítmények számsorozatát és egy határértéket kap, majd visszaadja azok számát, amelyek a határérték alatt vannak.

### Korlátok
* $1 \le N \le 100$, ahol $N$ a számsorozat mérete.
* $1 \le K \le 10\,000$, ahol $K$ a megadott határ.
* A sorozat minden eleme $1$ és $10\,000$ között van.

### Példa
A (6 3 4 1 2) számsorból az 1, a 2 és a 3 kisebb mint a megadott 4-es határ, így a függvény visszatérési értéke 3.
