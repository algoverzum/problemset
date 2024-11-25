## Leghosszabb emelkedő
Egy tudós űrhajót épít, sajnos nincs rakétája, hogy felszállhasson. Ezért egy emelkedőről szeretné kilövetni az űrhajóját. Ahhoz, hogy a legnagyobb esélye legyen a sikerre meg szeretné találni a leghosszabb emelkedőt, hogy a lehető legtöbb ideje legyen felgyorsulni. Emelkedőnek nevezzük azt a számsorozatot, amelynek minden eleme nagyobb, mint az előtte lévő. Az emelkedő hossza a számsorozatban lévő számok darabszáma.

### Bemenet
A bemenetben első sorában egyetlen egész szám van: $N$. <br /> 
Ezt követi $N$ sor mindegyik egy $M$ szám az $N$-ik hegycsúcs magassága.

### Kimenet
Két számot kell kiírnod, a leghosszabb emelkedő kezdő és végpontját. Ha nincs emelkedő akkor -1-et kell kiírnod.

### Korlátok
* $1 \le N \le 1000$
* $1 \le M \le 1000$

### Példa bemenet
    10
    100
    110
    115
    110
    105
    115
    125
    130
    125
    125

### Példa kimenet
    5 8

### A példa magyarázata
    100<110<115  3 csúcs
    105<115<125<130  4 csúcs, ez a leghosszabb emelkedő
