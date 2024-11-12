## Egyedi elemek
Egy raktárban tárolt árucikkek közül szeretnénk megállapítani, hogy miből maradt már csak egy darab, mivel ezeket akciósan szeretnénk eladni a vásárlóknak. Készíts egy programot, ami képes $N$ db árucikk kódjából megállapítani, hogy melyikek szerepelnek csak egyszer a sorban és ezeket az előfordulás sorrendjében írd ki.

### Bemenet
A bemenet első sorában egy darab egész szám van, az árucikkek száma: $N$
A bemenet második sorában $N$ darab egész szám van, az árucikkeket jelölő kódok: $A_1, A_2, \ldots, A_N$

### Kimenet
A kimenet első sorába azon árucikkek kódját kell kiírnod, amelyek csak egyszer szerepelnek a kódok listájában. Ezeket szóközökkel elválasztva előfordulási sorrendben kell megtenned.

### Korlátok
* $1 \le N \le 1000$
* $1 \le A_i \le 10000$

### Példa bemenet
    6
    1 2 2 3 3 3

### Példa kimenet
    1

### A példa magyarázata
Az 1-es kódú árucikk csak egy alkalommal jelenik meg a sorban, így ezt kiírjuk, míg a 2-es és a 3-as kódú árucikkek többször is szerepelnek a sorban, így ezeket nem írjuk ki.
