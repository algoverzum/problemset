## Találkozások
A kultúránkban fesztiválokon gyakran négyzetrács szerint csoportosulnak a résztvevők. Minden ilyen mezőben addot számú résztvevővel tudsz találkozni. A négyzetrács bal széléről indulsz és a jobb szélére szeretnél elérni. Minden lépésben dönthetsz. hogy az aktuális mezőről (i,j) jobbra (i,j+1), jobbra fel (i-1,j+1) vagy jobbra le (i+1,j+1) lépsz. Minden mezőn amire belépsz, ott az összes ott tartózkodóval találkozol. Készíts programot, ami megadja, hogy mennyi résztvevővel tudsz találkozni maximum, és hogy melyik mezőről kell hozzá indulnod.

### Bemenet
A bemenetben első sorában a sorok és oszlopok száma van: $N$, $M$.
Az ezt követő $N$ sorban $M$ darab szám van, az egyes rácsmezőben lévő személyek száma: $P_i$.

### Kimenet
A kimenet első sorába egy számot kell kiírnod: mennyi az a legtöbb résztvevő, akikel találkozni tudunk.
A kimenet második sorába egy számot kell kiírnod: melyik sorból kell indulnunk ehhez. (A sorszámozást 1-től kezdjük)

### Korlátok
* $1 \le N,M \le 100$
* $0 \le P_i \le 1000$

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
Az alábbi mezőket látogatjuk meg:
<b>6</b> 1 <b>7</b> 1
1 <b>6</b> 1 <b>7</b>
2 2 2 2
9 1 1 9
