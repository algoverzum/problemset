## Egyedi elemek
Egy raktárban tárolt árucikkek közül szeretnénk megállapítani, hogy melyikből maradt már csak egy darab, mivel ezeket akciósan szeretnénk eladni a vásárlóknak.
Készíts egy programot, amely $N$ darab árucikk kódja alapján megállapítja, hogy mely kódok szerepelnek **pontosan egyszer** a listában. Az ilyen kódokat a **bemenetben való előfordulás sorrendjében** kell kiírni.

### Bemenet
A bemenet első sorában egy egész szám szerepel, az árucikkek száma: $N$.
A bemenet második sorában $N$ darab egész szám található: $A_1, A_2, \ldots, A_N$ az egyes árucikkek kódjai.

### Kimenet
A kimenet első sorába kell kiírni azokat az árucikk-kódokat, amelyek **csak egyszer** fordulnak elő a bemenetben.
A kódokat szóközzel elválasztva, az eredeti bemeneti sorrendjükben kell megjeleníteni.
Ha nincs egyetlen ilyen kód sem, a kimenet maradjon üres.

### Korlátok
* $1 \le N \le 1\,000$
* $1 \le A_i \le 10\,000$

### Példa bemenet
    7
    4 2 1 3 3 2 3

### Példa kimenet
    4 1

### A példa magyarázata
A `4` és az `1` kódú árucikkek csak egyszer szerepelnek a listában, így ezek megjelennek a kimenetben.
A `2` és `3` kódok többször is előfordulnak, ezért ezeket nem írjuk ki.
