## Érmekombináció
Egy különleges országban kétféle érme van forgalomban. Az egyik érme értéke 2 peták, a másiké $K$ peták, ahol $K \not= 2$.

A kérdés az, hogy ki lehet-e pontosan fizetni $N$ petákot ezekkel az érmékkel. Másképp megfogalmazva: eldöntendő, hogy léteznek-e olyan nemnegatív egész számok $x$ és $y$, amelyekre $2\cdot x+K\cdot y=N$ teljesül.

### Bemenet
A bemenet első sorában egyetlen egész szám van: $N$, a kifizetendő összeg.

A bemenet második sorában egyetlen egész szám van: $K$, a másik érme értéke.

### Kimenet
Írd ki, hogy `YES`, ha az $N$ peták pontosan kifizethető a megadott érmékkel.
Ellenkező esetben írd ki, hogy `NO`.

### Korlátok
* $1 \le N, K \le 10^{18}$
* $K \not= 2$

### 1. Példa bemenet
    5
    3

### 1. Példa kimenet
    YES

### Az 1. példa magyarázata
Használhatsz egy 2-es érmét és egy $K=3$-as érmét.

### 2. Példa bemenet
    6
    1

### 2. Példa kimenet
    YES

### Az 2. példa magyarázata
Használhatsz három darab 2-es érmét. Alternatívaként használhatsz hat darab $K=1$-es érmét is.

### 3. Példa bemenet
    7
    4

### 3. Példa kimenet
    NO


### 4. Példa bemenet
    5
    7

### 4. Példa kimenet
    NO

