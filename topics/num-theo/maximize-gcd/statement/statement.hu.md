
## Villámosztás

Alex imádja a változatos matematikai fejtörőket, és hogy megünnepelje a
Kódkupa idei szezonjának kezdetét, az alábbi feladattal ajándékoz meg
titeket. Adott három pozitív egész szám, $A$, $B$ és $K$: **pontosan**
$K$ alkalommal ki kell választanotok az $A$ és $B$ számok egyikét, és
meg kell növelnetek az értékét $1$-gyel. Az a cél, hogy végül az $A$ és
$B$ számok legnagyobb közös osztójának értéke a lehető legnagyobb
legyen.


Például, ha $A = 7$, $B = 11$ és $K = 3$, akkor az elérhető legnagyobb
közös osztó a $7$ lesz, melyet úgy kapunk, hogy három alkalommal
megnöveljük $B$ értékét $1$-gyel: így végül $A = 7$, $B = 14$ és
$lnko(7, 14) = 7$. Továbbá, ha $A = 18$, $B = 9$ és $K = 3$, akkor a
három növeléssel elő tudjuk állítani $A = 20$ és $B = 10$ értékeket,
melyekre $lnko(20, 10) = 10$ adódik - be lehet látni, hogy ez a
maximális elérhető legnagyobb közös osztó.

Alex úgy döntött, hogy $T$ ilyen számhármasra is próbára teszi
tudásotokat. Mutassátok meg neki, hogy ti is legalább olyan jól
boldogultok a matematikai feladványokkal, mint ő!

### Bemenet

Az első sor a számhármasok $T$ számát tartalmazza. A következő $T$ sor
mindegyike három pozitív egészet tartalmaz, rendre $A$, $B$ és $K$
értékét.

### Kimenet

A kimenetre $T$ sort kell írni, mindegyik sor a válaszotokat tartalmazza
a megfelelő számhármasra.

### Korlátok

-   $1 \le T \le 100$.

-   $1 \le A, B, K \le 10^9$.


### Példa bemenet
    4
    7 11 3
    18 9 3
    58 38 14
    68 94 231

### Példa kimenet
    7
    10
    22
    131

### A példa magyarázata


A **példa teszteset** négy számhármast tartalmaz, melyek közül az első
kettőt a feladatleírásban korábban részleteztük.

A harmadik számhármasban az első két szám értéke $66$-ig, illetve
$44$-ig növelhető a $K=14$ művelet felhasználásával.

A negyedik számhármasban az első két szám értéke $131$-ig, illetve
$262$-ig növelhető a $K=231$ művelettel.

Megmutatható, hogy ezekre az értékekre lesz a legnagyobb közös osztó
értéke maximális az egyes esetekben.

