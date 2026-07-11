## Legolcsóbb távoli űrutazás
A barátom, Akikó $N$ darab űrutazás közül választhat. Mindegyik utazásra ismert a cél távolsága fényévekben és az utazás ára tallérokban. Szeretne legalább $K$ fényév távolságra elutazni, az ilyen utazások közül a legolcsóbbat fogja választani. Mennyibe fog kerülni neki?

### Bemenet
A bemenet első sorában egy egész szám található: $N$, az elérhető űrutazások száma.

A második sorban egy egész szám található: $K$, a kívánt minimális távolság.

A következő $2N$ sor az egyes utazások adatait tartalmazza. Minden utazáshoz két egymást követő sor tartozik: először a cél távolsága $D_i$ fényévekben, majd az utazás ára $P_i$ tallérokban.

### Kimenet
Egyetlen számot kell kiírnod, a legalább $K$ fényévű utazások közül a legolcsóbb árát, illetve $-1$-et ha nincs ilyen utazás.  

### Korlátok
* $1 \le N \le 1000$
* $1 \le D_i \le 1000$
* $1 \le P_i \le 1000$

### 1. Példa bemenet
    5
    10
    100
    999
    5
    100
    9
    1
    20
    50
    15
    100

### 1. Példa kimenet
    50

### Az 1. példa magyarázata
A 4. utazás a legolcsóbb a legalább 10 fényévre menők között.

### 2. Példa bemenet
    2
    10
    5
    12
    6
    345

### 2. Példa kimenet
    -1

### A 2. példa magyarázata
Nincs legalább 10 fényévre menő utazás.
