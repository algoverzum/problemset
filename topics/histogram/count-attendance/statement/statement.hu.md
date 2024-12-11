## Jelenlét számlálás
Moo Seis Lee egy kis iskolájába 10 gyerek iratkozott be. Az elmúlt $N$ nap mindegyikén felírták, hogy hány gyerek jelent meg az iskolában. Ebből szeretnénk kiszámolni, hogy hány olyan nap volt amikor pontosan $0,1,\ldots,9$ vagy $10$ gyerek ment suliba.

### Bemenet
A bemenet első sorában egy egész szám van: $N$ - a vizsgált napok száma.
A második sorban pedig $N$ szóközzel elválasztott szám van $C_1,C_2,\ldots,C_N$ - ahol $C_i$ az $i$-edik napon iskolába menő gyerekek száma.

### Kimenet
Egyetlen sorba kell kiírnod 11 szóközzel elválasztott számot: $H_0,H_1,\ldots,H_{10}$, ahol $H_i$ azon napok száma amikor pontosan $i$ gyerek ment iskolába.

### Korlátok
* $1 \le N \le 400$
* $0 \le C_i \le 10$

### Példa bemenet
    15
    8 9 1 0 0 1 3 5 7 9 7 3 1 10 9

### Példa kimenet
    2 3 0 2 0 1 0 2 1 3 1

### A példa magyarázata
A negyedik és ötödik napon homokvihar miatt senki sem ment iskolába, ezért az első szám 2, ami azt jelenti, hogy 2 olyan nap volt, amikor 0 gyerek volt az iskolában. A válaszból még az derül ki, hogy 3 olyan nap volt, amikor csak egy diák volt, nem volt olyan nap, amikor két diák volt, stb.
