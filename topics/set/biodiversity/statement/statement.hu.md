## Biodiverzitás
Egy bolygón élő összes élőlény azonosítóját szeretnénk összegyűjteni. Ennek érdekében két csapatot küldtünk ki, akik a bolygó két különböző felén kutattak. Mindkét csapat elküldött egy listát az általuk talált élőlények azonosítóival. A feladatod, hogy írd ki az összes olyan azonosítót, amely legalább az egyik listában szerepel.

### Bemenet
A bemenet első sorában két egész szám van szóközzel elválasztva: $N$ és $M$ a csapatok által gyűjtött azonosítók száma.
A bemenet második sorában $N$ db egész szám van szóközzel elválasztva, az első csapat által összegyűjtött azonosítók: $A_1, A_2, \ldots A_N$. 
A bemenet harmadik sorában $M$ db egész szám van szóközzel elválasztva, a második csapat által összegyűjtött azonosítók: $B_1, B_2, \ldots B_M$ . 

### Kimenet
A standard kimenet első sorába azon azonosítók számát írd, amelyek legalább az egyik listában szerepelnek.
A második sorba ezeket az azonosítókat kell kiírni szóközzel elválasztva, növekvő sorrendben. Minden azonosítót csak egyszer szabad kiírni!

### Korlátok
* $1 \le N,M \le 10\,000$
* $1 \le A_i, B_i \le 100\,000$

### Példa bemenet
    5 6
    9 3 6 7 1
    2 2 3 6 6 5

### Példa kimenet
    7
    1 2 3 5 6 7 9


