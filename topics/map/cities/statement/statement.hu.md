## Városok
Egy távoli csillagrendszert kell katalogizálnod. Ehhez rendelkezésedre áll egy lista, amelyben soronként egy bolygó neve szerepel, mellette pedig a rajta található városok. Emellett van egy másik listád, amely városneveket tartalmaz, és a feladatod az, hogy meghatározd, melyik bolygón találhatók ezek a városok.

### Bemenet
A bemenetben első sorában egy egész szám van: $N$ a bolygók száma. <br>
A következő $N$ blokk mindegyike két sorból áll:<br>
* Az első sorban a bolygó neve és egy egész szám szerepel, amely megadja az adott bolygón található városok számát.<br>
* A második sor a bolygón található városok neveit tartalmazza szóközzel elválasztva.

A bemenet következő ($N+2$-edik) sorában egy egész szám szerepel: $M$ a keresett városok száma.<br>
Az ezt követő $M$ sor mindegyike egy-egy város nevét tartalmazza. Minden város biztosan megtalálható valamelyik bolygón.
A bolygók és a városok neve kizárólag az angol ábécé kisbetűiből áll, legfeljebb 10 karakter hosszúak.
Egy bolygón legfeljebb 1000 város lehet.

### Kimenet
$M$ bolygó nevét kell kiírnod, mindegyiket külön sorba. Ezek azok a bolygók, ahol a keresett városok találhatók.

### Korlátok
* $1 \le N,M \le 1000$

### Példa bemenet
    4
    mandalore 2
    sundari ronion
    naboo 3
    theed keren vis
    alderaan 2
    aldera juranno
    kamino 1
    tipoca
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
