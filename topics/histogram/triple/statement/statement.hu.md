## Tripla
Adott egy $a$ tömb, amely $n$ számot tartalmaz. Írd ki a legkisebb olyan számot, ami legalább háromszor szerepel a tömbben, vagy írd ki a $-1$-et, ha nincs ilyen szám.

### Bemenet
A bemenet első sora egyetlen egész számot tartalmaz: $n$ - a tömb hossza.  
A bemenet második sora $n$ egész számot tartalmaz, $a_1, a_2, \ldots, a_n$ ($1\le a_i\le n$ - a tömb elemei.

### Kimenet
Egyetlen számot kell kiírnod, a **legkisebb** háromszor szereplő számot, vagy írd ki a -1-et, ha nincs ilyen.

### Korlátok
* $1 \le n \le 10^5$
* $1 \le a_i \le n$ minden $i=1,2,\ldots,n$ esetén.

### 1. példa bemenet
    5
    1 5 2 4 3

### 1. példa kimenet
    -1

### Az 1. példa magyarázata
Minden szám különböző, így egyik sem fordul elő legalább háromszor, ezért a válasz -1.

### 2. példa bemenet
    8
    2 2 3 3 4 4 2 2

### 2. példa kimenet
    2

### A 2. példa magyarázata
A 2 négyszer fordul elő, így a válasz 2.

### 3. példa bemenet
    10
    3 1 2 3 1 2 3 1 2 3

### 3. példa kimenet
    1

### A 3. példa magyarázata
Az 1, 2 és 3 mindegyik legalább háromszor fordul elő, így ezek közül a legkisebb azaz az 1 a jó válasz.
