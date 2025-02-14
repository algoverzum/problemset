## Több oxigén
Egy idegen bolygót terraformálnak űrutazók, hogy az embereknek is lakható legyen. Ennek fontos lépése, hogy a bolygó oxigén szintje konzisztensen megfelelő szinten legyen. Ennek ellenőrzésére a feladatot végző tudósok több mérő állomást állítottak fel, amik a környezetük oxigén szintjét mutatják ki minden nap egy egész számként reprezentálva. A tudósok szeretnék tudni, hogy az elmúlt napokban mikor fordult elő, hogy minden mérő állomás nagyobb értéket mért, mint az azt megelőző napon. A feladatod, hogy ebben segíts nekik.

### Bemenet
A bemenetben első sorában kettő egész szám van, a mérő állomások száma: $N$, és a napok száma: $M$.
Az ezt követő $N$ sorban rendre $M$ szám van, ezek az $i$-edik mérő állomáson a $j$-edik nap mért oxigén szintnek felelnek meg: $A_{i,j}$.

### Kimenet
A kimenet első sorába a helyes napok számát kell kiírnod, míg a másodikba a helyes napok sorszámát kell szóközzel elválasztva. 

### Korlátok
* $1 \le N \le 100$
* $1 \le M \le 100$
* $1 \le A_{i,j} \le 1000$

### Példa bemenet
    3 5
    2 10 4 5 7 8
    11 12 13 14 15 15
    1 20 42 1 13 13

### Példa kimenet
    2
    2 5

### A példa magyarázata

A második napon a három mérő állás eredményei: 1. 10>2, 2. 12>11, 3. 20>1. Az ötödik nap eredménye: 1. 7>5, 2. 15>14, 3. 13>1. Ezen a kettő napon kívül nincs más olyan, amikor a feltétel teljesül.