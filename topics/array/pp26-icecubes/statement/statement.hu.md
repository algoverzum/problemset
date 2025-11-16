## Jégkockák
Egy étteremnek van egy hűtőszekrénye, amelynek $N$ rekesze van, és minden rekeszben ismert, hogy hány jégkocka található.

Érkezik egy pincér, és minden olyan rekeszből kivesz egy jégkockát, amelyben van legalább egy.

Hány jégkocka marad ezek után a hűtőszekrényben összesen?

### Bemenet
A bemenet első sorában egy egész szám van: $N$, a rekeszek száma.

A következő sor $N$ darab egész számot tartalmaz: $C_{0}, \, \ldots, \, C_{N-1}$ -- az egyes rekeszekben található jégkockák számát.

### Kimenet
Egyetlen számot kell kiírnod, a hűtőszekrényben maradt jégkockák számát, miután a pincér kivette a számára szükséges jégkockákat.

### Korlátok
* $1 \le N \le 10^5$
* $0 \le C_i \le 1000$ minden $i=0\ldots N-1$-re.

### 1. példa bemenet
    5
    0 3 1 0 5

### 1. példa kimenet
    6

### Az 1. példa magyarázata

Az első példában, miután a pincér kivette a szükséges jégkockákat, a rekeszekben rendre $0, 2, 0, 0, 4$ jégkocka maradt, ami összesen $2 + 4 = 6$ darab.

### 2. példa bemenet
    3
    1 1 1

### 2. példa kimenet
    0

### A 2. példa magyarázata
A második példában, miután a pincér kivette a szükséges jégkockákat, a rekeszekben rendre $0, 0, 0$ jégkocka maradt, ami összesen $0$ darab.
