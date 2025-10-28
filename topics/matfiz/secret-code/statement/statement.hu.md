## Titkos kód
Egy legfeljebb $N$ számjegyű titkos számkódot szeretnénk megfejteni, a kód pozitív egész szám. Az tudjuk csak róla, hogy mennyi az 5-tel ($A$), a 7-tel ($B$), illetve a 11-gyel ($C$) osztásának maradéka.

Írj programot, amely beolvassa $N$ ($1\le N\le 5$), valamint $A$ és $B$ és $C$ értékét, majd megadja a legkisebb olyan számkódot, ami a maradékok alapján lehetséges, továbbá hogy hány ilyen legfeljebb $N$-jegyű szám van összesen szóközzel elválasztva!

Ha nincs ilyen szám, akkor -1 legyen a kiírt szám.

### Bemenet
A bemenet első sorában egyetlen egész szám van: $N$, a titkos kód legfeljebb $N$ számjegyű.

A bemenet második sorában egyetlen egész szám van: $A$, a titkos kód 5-ös maradéka.

A bemenet harmadik sorában egyetlen egész szám van: $B$, a titkos kód 7-es maradéka.

A bemenet negyedik sorában egyetlen egész szám van: $C$, a titkos kód 11-es maradéka.

### Kimenet
Két számot kell kiírnod egy sorba: A legkisebb olyan számkódot, ami a maradékok alapján lehetséges, továbbá hogy hány ilyen legfeljebb $N$-jegyű szám van összesen! 

### Korlátok
* $1 \le N \le 5$
* $0 \le A \le 4$
* $0 \le B \le 6$
* $0 \le C \le 10$

### 1. Példa bemenet
    3
    3
    4
    0

### 1. Példa kimenet
    88 3

### 2. Példa bemenet
    1
    2
    1
    1

### 2. Példa kimenet
    -1

### 3. Példa bemenet
    4
    1
    5
    2

### 3. Példa kimenet
    376 25
