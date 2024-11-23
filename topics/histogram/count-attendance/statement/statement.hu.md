## Jelenlét Számlálás
Moo Seis Lee egy kis iskolájába 10 gyerek iratkozott be. Az elmúlt $N$ nap mindegyikén felírták, hogy hány gyerek jelent meg az iskolában. Ebből szeretnénk kiszámolni, hogy olyan nap volt amikor pontosan $0,1,\ldots,9$ vagy $10$ gyerek ment suliba.

### Bemenet
A bemenet első sorában egy egész szám van: $N$ - a vizsgált napok száma.
A második sorban pedig $N$ szóközzel elválasztott szám van $A_1,A_2,\ldots,\A_N$ - ahol $A_i$ az $i$-edik napon iskolába menő gyerekek száma.

### Kimenet
Egyetlen sorba kell kiírnod 11 szóközzel elválasztott számot $H_0,H_1,\ldots,\A_{10}$ - ahol $H_i$ azon napok száma amikor pontosan $i$ gyerek ment iskolába.

### Korlátok
* $1 \le N \le 400$
* $0 \le A_i \le 10$

### Példa bemenet
    15
    8 9 10 0 0 1 3 5 7 9 7 3 1 10 9

### Példa kimenet
    2 2 0 2 0 1 0 2 1 3 2

### A példa magyarázata
A negyedik és ötödik napon homokvihar miatt senki sem ment iskolába, ezért az első szám 2. A válaszból még az derül ki, hogy 2 olyan nap volt, amikor mindenki jelen volt, 3 napon pedig csak 1 gyerek hiányzott, stb.
