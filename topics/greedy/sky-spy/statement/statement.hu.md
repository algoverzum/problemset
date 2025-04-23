## Kémműhold
A Birodalom egyik geostacionárius kémműholdját sikerült a Lázadóknak meghekkelniük. Ez közvetlenül a hírhedt Mos Eisley űrkikötő felett kering, és most a Birodalom tudta nélkül készíthetnek felvételeket az ott parkoló űrhajókról.

A Lázadók hírszerzése megszerezte az információt, hogy $N$ űrhajó fog megjelenni különböző időpontokban. Mindegyik hajó pontosan megadta, hogy mely időintervallumban tartózkodik az űrkikötőben. A kémműhold képes nagy felbontású felvételeket készíteni, de a lebukás elkerülése érdekében a lehető legkevesebb képet szeretnénk készíteni – úgy, hogy mind a $N$ űrhajó szerepeljen legalább egy felvételen.

Határozd meg, hány időpillanatban kell aktiválni a műholdat az űrkikötő megfigyelésére, úgy, hogy minden űrhajó legalább egy alkalommal megfigyelésre kerüljön, amikor valóban ott tartózkodik.

### Bemenet
A bemenet első sorában az érkező űrhajók száma van: $N$.

A következő $N$ sor mindegyike két egész számot tartalmaz, az $i$-edik sorban $A_i$-t és $B_i$-t; $A_i$ az $i$-edik űrhajó érkezési és $B_i$ a távozási időpontja. Ha egy fényképet a $T$ időpontban készítik és $A_i \le T < B_i$, akkor
azon a fényképen rajta lesz az $i$-edik űrhajó.

### Kimenet
A kimenet első sorába egyetlen számot kell kiírni, a készítendő fényképek $K$ számát.

A második sor pontosan $K$ egész számot tartalmazzon egy-egy szóközzel elválasztva, azon időpontokat (tetszőleges sorrendben), amikor a képeket készíteni kell!
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
