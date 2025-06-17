## Egyforma szomszédok
Űrhajós csapatod egy titokzatos bolygón landolt. Az egyik barlangban egy táblázatot találtok, tele furcsa számokkal – ezek az idegenek által hagyott jelértékek.

Néha előfordul, hogy két szomszédos mező (egymás mellett vízszintesen vagy függőlegesen, tehát nem átlósan) ugyanazt a számot tartalmazza. Ezeket hívjuk visszhang jeleknek.

A feladatod az, hogy megszámold, hány olyan mező van, amelynek legalább egy szomszédja pontosan ugyanazt a számot tartalmazza.

### Bemenet
A bemenet első sora két egész számot tartalmaz: a sorok ($N$) és az oszlopok ($M$) számát.
Ezután $N$ sor következik, mindegyikben $M$ egész szám található: az $i$-edik sor $j$-edik eleme $S_{i,j}$, az $(i,j)$ mezőben található jelérték.

### Kimenet
Egyetlen számot írj ki: annak a mezőknek a számát, amelyeknek van legalább egy szomszédja azonos értékkel. 

### Korlátok
* $1 \le N, M \le 100$
* $1 \le S_{i,j} \le 1000$

### Példa bemenet
    4 3
    2 1 5
    5 3 5
    2 2 2
    9 6 7

### Példa kimenet
    5

### A példa magyarázata
Az alábbi mezőknek van azonos értékű szomszédjuk:

* (1,3) és (2,3): mindkettő 5, az egyik a másik felett van.

* (3,1), (3,2), (3,3): mindegyik 2, egymás mellett vannak.
