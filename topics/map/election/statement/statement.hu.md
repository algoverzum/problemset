## Szavazás
Egy űrhajóst keresünk egy űrexpedíció vezetésére, és a kiválasztást szavazás útján szeretnénk eldönteni. Azonban a szavazatok a rossz szervezés miatt több dobozba kerültek, így most összesítenünk kell őket. Készíts egy programot, amely több "jelölt"-"szavazat szám" párosból összegezni tudja, hogy melyik jelöltre mennyi szavazat érkezett!

### Bemenet
A bemenet első sorában egyetlen egész szám van, a szavazat csomagok száma: $N$.
A következő $N$ sorban egy string és egy egész szám van szóközzel elválasztva, a jelölt neve és a hozzá tartozó szavazatok száma: $S_1, S_2, \ldots, S_N$; $A_1, A_2, \ldots, A_N$

### Kimenet
Írd ki az összes jelöltet ábécésorrendben külön sorokba az alábbi módon:
A sor első eleme a jelölt neve legyen, majd ezt a hozzá tartozó szavazatok száma kövesse szóközzel elválasztva!

### Korlátok
* $1 \le N \le 1000$
* $1 \le S_i$ hossza $ \le 30$ és $S_i$ az angol ábécé betűit tartalmazza minden $1 \le i \le N$ esetén
* $1 \le A_i \le 10000$ minden $1 \le i \le N$ esetén

### Példa bemenet
    5
    dreebo 5
    eeper 2
    dreebo 2
    dreebo 6
    scrimbler 8

### Példa kimenet
    dreebo 13
    eeper 2
    scrimbler 8

### A példa magyarázata
dreebo-ra több különböző csomagban is érkeztek szavazatok, így ezek összeadódnak. A többiekhez csak egy-egy csomag tartozott.
