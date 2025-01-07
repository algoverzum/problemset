## Asztronauta Párok
Egy űrhajós küldetésre kettő azonos súlyú asztronautát szeretnénk küldeni, hogy az űrhajó egyensúlyban legyen. $N$ különböző jelöltünk van, akiknek ismerjük a testsúlyait: $A_1, A_2, \ldots, A_N$. Szeretnénk tesztekkel megtalálni a legjobb párt, így az összes lehetséges módon ki szeretnénk választani két asztronautát, akiknek a testsúlya megegyezik. Határozd meg, hogy hány tesztet kell elvégeznünk, tehát azt a számot, hogy hányféleképpen tudunk kiválasztani két azonos súlyú asztronautát. Formálisan, az olyan $i, j$ párok számát keressük, ahol $1 \leq i < j \leq N$ és $A_i = A_j$.

### Bemenet
A bemenet első sorában egy szám van, az asztronauták száma: $N$ .
A bemenet második sorában $N$ szám van, az egyes asztronauták súlyai: $A_1, A_2, \ldots, A_N$.

### Kimenet
Egyetlen számot kell kiírnod, a lehetséges párok számát.

### Korlátok
* $1 \le N \le 100$
* $1 \le A_i \le 1000$

### Példa bemenet
    6
    71 82 63 82 63 63

### Példa kimenet
    4

### A példa magyarázata
A három 63 súlyú asztronautából háromféleképpen is tudunk azonos súlyú párt csinálni és még egy lehetséges pár a kettő 82-es.
