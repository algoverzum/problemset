## Prím szita
Írj programot, amely beolvas egy pozitív egész $N$ számot, majd kiírja $N$-ig az összes prímet.

Alkalmazd az Eratoszthenész vagy prím szita módszerét:

Elkészítjük azt a számsorozatot, amely az összes potitív egészet tartalmazza.

Kiindulunk az első prímszámból ($2$), majd "lehúzzuk" a többszöröseit ($4, 6, 8, 10, \ldots$), aztán az első le nem húzott számmal folytatjuk ($3$), majd "lehúzzuk" ennek a többszöröseit, stb így folytatva $N$-ig. A "le nem húzott" számok lesznek a prímek.

### Bemenet
A bemenetben egyetlen egész szám van: $N$.

### Kimenet
Írd ki $N$-ig az összes prímet szóközzel elválasztva.

### Korlátok
* $1 \le N \le 1000$

### Példa bemenet
    20

### Példa kimenet
    2 3 5 7 11 13 17 19

### A példa magyarázata
20-ig ezek a prímszámok.
