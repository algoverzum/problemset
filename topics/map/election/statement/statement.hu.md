## Szavazás
Egy úrexpedíció vezetésére keresünk egy űrhajóst. Ezt szavazással akarjuk kiválasztani, de rossz szervezés miatt a szavazatok több különböző dobozba lettek bedobva, így most ezeket összegeznünk kell. Írj egy programot, ami több "jelölt"-"szavazat szám" párosból összegezni tudja, hogy melyik jelöltre mennyi szavazat érkezett!

### Bemenet
A bemenet első sorában egyetlen egész szám van, a szavazat csomagok száma: $N$.
A következő $N$ sorban egy string és egy egész szám van szóközzel elválasztva, a jelölt neve és a hozzá tartozó szavazatok száma: $S_1, S_2, \dots, S_N$; $A_1, A_2, \dots, A_N$

### Kimenet
Írd ki az összes jelöltet ábécésorrendben külön sorokba az alábbi módon:
A sor első eleme a jelölt neve legyen, majd ezt a hozzá tartozó szavazatok száma kövesse szóközzel elválasztva!

### Korlátok
* $1 \le N \le 1000$
* $1 \le S_i$ hossza $ \le 256$
* $1 \le A_i \le 10000$

### Példa bemenet
    5
    Dreebo 5
    Eeper 2
    Dreebo 2
    Dreebo 6
    Scrimbler 8

### Példa kimenet
    Dreebo 13
    Eeper 2
    Scrimbler 8

### A példa magyarázata
Dreebo-ra több különböző csomagban is érkeztek szavazatok, így ezek összeadódnak. A többiekhez csak egy-egy csomag tartozott.
