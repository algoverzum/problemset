## Kémműhold
A Birodalom egyik geostacionárius kémműholdját sikerült a Lázadóknak meghekkelniük. Ez közvetlenül a hírhedt Mos Eisley űrkikötő felett kering, és most a Birodalom tudta nélkül készíthetnek felvételeket az ott parkoló űrhajókról.

A Lázadók hírszerzése megszerezte az információt, hogy $N$ űrhajó fog megjelenni egy-egy meghatározott időintervallumban. A kémműholddal a lehető legkevesebb képet szeretnének készíteni – úgy, hogy mind az $N$ űrhajó szerepeljen legalább egy felvételen. Az $i$-edik űrhajó $A_i$ időpontban érkezik és $B_i$ időpontban távozik. Egy $T$ időpontban készített fényképen akkor és csak akkor lesz rajta az $i$-edik űrhajó, ha $A_i \le T < B_i$.

Határozd meg, hogy mely időpillanatokban kell aktiválni a műholdat az űrkikötő megfigyelésére, úgy, hogy minden űrhajó legalább egy alkalommal megfigyelésre kerüljön, amikor valóban ott tartózkodik!

### Bemenet
A bemenet első sorában az érkező űrhajók $N$ száma van. A következő $N$ sor mindegyikében két egész szám van, az $i$-edik sorban $A_i$ és $B_i$, ahol $A_i$ az $i$-edik űrhajó érkezési és $B_i$ a távozási időpontja.

### Kimenet
A kimenet első sorába egyetlen számot kell kiírni, a készítendő fényképek $K$ számát.  
A második sor pontosan $K$ egész számot tartalmazzon egy-egy szóközzel elválasztva, azon időpontokat (tetszőleges sorrendben), amikor a képeket készíteni kell.
Ha több megoldás van, akkor bármelyiket kiírhatod.

### Korlátok
* $1 \le N \le 10^5$
* $1 \le A_i < B_i \le 10^9$ minden $i=1, 2, \ldots, N$-re

### Példa bemenet
    6
    2 4
    1 4
    2 7
    7 13
    5 10
    3 9

### Példa kimenet
    2
    3 9

### A példa magyarázata
A 3. és 4. űrhajót nem lehet egyszerre lefotózni, így legalább 2 fényképre szükségünk lesz. Két képpel megoldható a feladat amint az az ábrán is látható. (Több megoldás is van.)

![](tex/abra.png)
