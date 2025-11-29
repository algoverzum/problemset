## Kettéosztás
Adott $n$ egész szám. A feladat: a számokat két nem üres részre osztani úgy, hogy:

* Mindkét részben legyen legalább egy elem.
* A két részben az elemek összege azonos paritású legyen.

Például, ha az adott számok [1, 2, 4, 3, 2, 3, 5, 4], akkor a két rész lehet: [1, 2, 3] ás [4, 2, 3, 5, 4], ahol az első részben az elemek összege 6, a második részben az elemek összege 18.

### Bemenet
Az első sor egy egész számot tartalmaz, $n$ - a megadott számok számát.  
A következő sor $n$ egész számot tartalmaz, $a_1, a_2, \ldots, a_n$ - a megadott $n$ számot.

### Kimenet
Írd ki, hogy "YES" (idézőjelek nélkül), ha lehetséges a kettéosztás úgy, hogy az elemek összegének paritása mindkét részben ugyanaz legyen, és mindkét rész legalább egy elemet tartalmaz, különben írd ki, hogy "NO".

### Korlátok
* $2 \le n \le 50$
* $1 \le a_i \le 50$ minden $i=1, 2, \ldots, n$ esetén.

### 1. példa bemenet
    8
    1 2 4 3 2 3 5 4

### 1. példa kimenet
    YES

### Az 1. példa magyarázata
Az első példa leírásra került a feladat szövegében.

### 2. példa bemenet
    2
    4 7

### 2. példa kimenet
    NO

### A 2. példa magyarázata
Csak két felosztás van: [4], [7] és [7], [4], de mindkét esetben az összeg paritása különbözik.
