## Egyedi elemek
Egy raktárban tárolt árucikkek közül szeretnénk megállapítani, hogy miből maradt már csak egy darab, mivel ezeket akciósan szeretnénk eladni a vásárlóknak. Készíts egy programot, ami képes $N$ db árucikk kódjából megállapítani, hogy melyikek szerepelnek csak egyszer a sorban. Az egyszer szereplő elemeket a bemenetben való előfordulás sorrendjében írd ki.

### Bemenet
A bemenet első sorában egy egész szám van, az árucikkek száma: $N$
A bemenet második sorában $N$ darab egész szám van, az árucikkeket jelölő kódok: $A_1, A_2, \ldots, A_N$

### Kimenet
A kimenet első sorába azon árucikkek kódját kell kiírnod, amelyek csak egyszer szerepelnek a kódok listájában. Ezeket szóközökkel elválasztva, a bemenetben való előfordulásukkal azonos sorrendben írd ki. Ha nincs egy ilyen elem sem, akkor maradjon üresen a kimenet.

### Korlátok
* $1 \le N \le 1\,000$
* $1 \le A_i \le 10\,000$

### Példa bemenet
    6
    2 1 3 3 2 3

### Példa kimenet
    1

### A példa magyarázata
Az 1-es kódú árucikk csak egy alkalommal jelenik meg a sorban, így ezt kiírjuk, míg a 2-es és a 3-as kódú árucikkek többször is szerepelnek a sorban, így ezeket nem írjuk ki.
