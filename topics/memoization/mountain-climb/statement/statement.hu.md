## Hegymászás
Kutatók a bolygó egy hegyét próbálják feltérképezni. A hegy különböző szakaszait egy négyzetrács jelképezi, ahol az egyes mezőkben lévő értékek a szakasz magasságát jelképezik. A négyzetrács két oldala azonos hosszúságú. A kutatók a hegy szélének egyik mezőjéről indulnak és egy lépésben egy pontosan eggyel magasabb szomszédos(nem átlós) mezőre lépnek. A kutatók addig mennek ilyen módon felfele, amíg el nem érnek egy olyan szakaszra, ahonnan már nem tudnak feljebb menni, ahol pedig expedíciójukat befejezik. Készíts programot, amely megadja a kutatók által megtehető leghosszabb utat, aminek a végén az expedíciót befejezik.

### Bemenet
A bemenet első sorában egyetlen egész szám van a hegyet tartalmazó négyzet oldalának hossza: $N$.
A következő $N$ sorban $N$ egész szám van, az egyes hegyszakaszok magassága: $ A_{1,1}, A_{2,1}, \ldots, A_{N,1}, A_{1,2}, \dots, A_{N,N}$ 

### Kimenet
A kimenet első sorába egyetlen egész számot kell kiírnod, a leghosszabb útvonal hosszát.
A kimenet második sorába kettő egész számot kell kiírnod, a leghosszabb expedíció kezdőpontját.

### Korlátok
* $1 \le N \le 30$
* $1 \le A_{i,j} \le 30$

### Példa bemenet
    6
    1 2 2 2 2 2
    4 3 4 2 2 1
    1 1 5 6 1 8
    1 1 1 9 6 7
    1 3 4 4 5 1
    1 2 1 1 1 1

### Példa kimenet
    5
    1 1

### A példa magyarázata
A bal felső sarokból indulva a (3,4)es mezőig tart a leghosszabb út.
