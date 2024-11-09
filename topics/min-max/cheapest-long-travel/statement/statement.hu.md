## Legolcsóbb Távoli Űrutazás
A barátom, Akikó $N$ darab űrutazás közül választhat. Mindegyik utazásra ismert a cél távolsága fényévekben és az utazás ára tallérokban. Szeretne legalább $K$ fényév távolságra elutazni, az ilyen utazások közül a legolcsóbbat fogja választani. Mennyibe fog kerülni neki?

### Bemenet
A bemenetben első sorában két szóközzel elválasztott egész szám van: $N,K$, az eléthető űrutazások száma, és a kívánt minimális távolság. A második sorban $N$ egész szám van szóközzel elválasztva, az egyes utak céltávolságai fényévekben ($A_1, A_2, \ldots, A_N$). A harmadik sorban $N$ egész szám van szóközzel elválasztva, az egyes utazások árai tallérokban ($B_1, B_2, \ldots, B_N$).

### Kimenet
Egyetlen számot kell kiírnod, a legalább $K$ fényévű utazások közül a legolcsóbb árát, illetve $-1$-et ha nincs ilyen utazás.  

### Korlátok
* $1 \le N \le 1000$
* $1 \le A_i \le 1000$
* $1 \le B_i \le 1000$

### 1. Példa bemenet
    5 10
    100 5 9 20 15
    999 100 1 50 100

### 1. Példa kimenet
    50

### Az 1. példa magyarázata
A 4. utazás a legolcsóbb a legalább 10 fényévre menők között.

### 2. Példa bemenet
    2 10
    5 6
    12 345

### 2. Példa kimenet
    -1

### A 2. példa magyarázata
Nincs legalább 10 fényévre menő utazás.
