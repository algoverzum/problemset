## Városok
Egy távoli csillagrendszert kell katalogizálnod. Ehhez rendelkezésedre áll egy lista, amelyben soronként egy bolygó neve szerepel, mellette pedig a rajta található városok. Emellett van egy másik listád, amely városneveket tartalmaz, és a feladatod az, hogy meghatározd, melyik bolygón találhatók ezek a városok.

### Bemenet
A bemenetben első sorában egy egész szám van: $N$ a bolygók száma
A következő $N$ sor mindegyike egy bolygó nevét tartalmazza, utána szóközzel elválasztva az azon található városokat.
A bemenet $N+2$-edik sorában egy egész szám szerepel: $M$ a keresett városok száma.
az ezt követő $M$ sor mindegyike egy-egy város nevét tartalmazza. Minden város biztosan megtalálható valamelyik bolygón.
A bolygók és a városok neve kizárólag az angol ábécé kisbetűiből áll, legfeljebb 10 karakter hosszúak.
Egy bolygón legfeljebb 1000 város lehet.

### Kimenet
$M$ bolygó nevét kell kiírnod, mindegyiket külön sorba. Ezek azok a bolygók, ahol a keresett városok találhatók.

### Korlátok
* $1 \le N,M \le 10000$

### Példa bemenet
    4
    mandalore sundari ronion
    naboo theed keren vis
    alderaan aldera juranno
    kamino tipoca
    3
    tipoca
    theed
    aldera

### Példa kimenet
    kamino
    naboo
    alderaan

### A példa magyarázata
    tipoca a kamino bolygón van.
    theed a naboo bolygón van.
    aldera az alderaan bolygón van.
