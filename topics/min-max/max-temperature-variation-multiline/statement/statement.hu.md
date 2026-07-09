## Legnagyobb hőingás
Az időjárást előrejelző mágikus állatunk, a josi megadta a következő $N$ napra a napi várható minimum és maximum hőmérséklet. Mekkora lesz a legnagyobb napi hőingás? (Azaz milyen nagy lehet a napi maximális hőmérséklet és az aznapi minimális hőmérséklet különbsége?)

### Bemenet
A bemenet első sorában egy egész szám található: $N$, az időjárás-előrejelzésben szereplő napok száma.

A következő $2N$ sor a hőmérsékleteket tartalmazza. Minden naphoz két egymást követő sor tartozik: először az $A_i$ minimumhőmérséklet, majd a $B_i$ maximumhőmérséklet.

### Kimenet
Egyetlen számot kell kiírnod, a legnagyobb napi hőingás értékét.

### Korlátok
* $1 \le N \le 100$
* $-50 \le A_i \leq B_i\le 50$

### Példa bemenet
    5
    10
    15
    4
    8
    -5
    -1
    -2
    0
    -5
    1

### Példa kimenet
    6

### A példa magyarázata
Az első nap $15-10=5$ a hőingás. Utánna rendre $8-4=4$, $-1-(-5)=4$, $0-(-2)=2$, $1-(-5)=6$. Ezek maximuma 6. 
