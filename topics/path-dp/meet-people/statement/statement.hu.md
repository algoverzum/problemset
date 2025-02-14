## Találkozások
Egy távoli galaxisban Spock a világűr egy szektorában navigál, amelyet egy csillagrendszerekből álló rács képvisel. A rács minden egyes négyzete egy-egy csillagrendszernek felel meg, és minden rendszerben különböző számú legénységi tag állomásozik a USS Enterprise-ról vagy esetleg más csillaghajókról.

Spock feladata, hogy a rács bal széléről (bármelyik csillagrendszerből kiindulva) elutazzon a szektor jobb szélére (bármelyik csillagrendszerbe). Spocknak minden lépésnél több lehetősége van:

* Jobbra lépni: Spock egyenesen továbbhaladhat az azonos sorban lévő következő rendszerig.
* Jobbra felfelé léphet: Spock átlósan jobbra-felfelé mozoghat egy sorral feljebb és egy oszloppal jobbra lévő rendszerbe.
* Lefelé jobbra léphet: Spock átlósan lefelé-jobbra mozoghat egy sorral lejjebb és egy oszloppal jobbra lévő rendszerbe.

Spocknak gondosan meg kell terveznie a szektoron belüli útvonalát. A **cél** az, hogy balról jobbra haladva a lehető legtöbb legénységi taggal találkozzon az útja során. Nem hagyhatja el a rácsot, és minden egyes rendszerben, amelyet meglátogat, találkozik az összes ottani legénységi taggal.

### Bemenet
A bemenetben első sorában a sorok és oszlopok száma van: $N$, $M$.
Az ezt követő $N$ sorban $M$ darab szám van, a rács $i$-edik sorának $j$-edik oszlopában lévő mezőben az emberek száma $P_{i,j}$.

### Kimenet
A kimenet első sorába egy számot kell kiírnod: mennyi az a legtöbb ember, akikel találkozni tud Spock.
A kimenet második sorába egy számot kell kiírnod: melyik sorból kell indulnia ehhez. (A sorszámozást 1-től kezdjük.)

### Korlátok
* $1 \le N,M \le 100$
* $0 \le P_{i,j} \le 1000$

### Példa bemenet
    4 4
    6 1 7 1
    1 6 1 7
    2 2 2 2
    9 1 1 9

### Példa kimenet
    26
    1

### A példa magyarázata
Az alábbi mezőket látogatjuk meg ($6+6+7+7=26$):

<b>6</b> 1 <b>7</b> 1

1 <b>6</b> 1 <b>7</b>

2 2 2 2

9 1 1 9
