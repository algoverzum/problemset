## Legrövidebb kör
A Kuklos bolygón a városokat számokkal jelöljük $1$-től $N$-ig. Egyes városokat utak kötnek össze, és ezeken az utakon mindkét irányba lehet közlekedni.
A $P$ sorszámú városban vagyunk, és szeretnénk egy rövid kirándulást tenni. Fontos számunkra, hogy:

* a kirándulás visszavezessen a kiindulási, vagyis a $P$ városba,
* egy úton legfeljebb egyszer menjünk végig,
* és a lehető legrövidebb ilyen kört találjuk meg.

Keressük meg a legrövidebb utat, ami $P$ városból indul, több városon keresztül halad, majd visszatér $P$-be, úgy, hogy közben egy úton sem megyünk át kétszer.

### Bemenet
A bemenet első sorában három egész szám van: $N$ a városok száma, $M$ az utak száma és $P$ a város ahonnan indulunk. <br>
Ezután $M$ sor következik. Mindegyik sor két város sorszámát tartalmazza ($A_i$ és $B_i$), amelyek között van út.

### Kimenet
Az első sorba azt az egész számot írd, ami a legrövidebb megtalálható kör hossza (hány úton haladtunk). Ha nincs ilyen kör, akkor $-1$ legyen a válasz. <br>
A második sorban sorold fel a körben szereplő városokat sorrendben, ahogy haladtál. (Az utolsó városból automatikusan visszatérünk az elsőbe, ezt nem kell külön kiírni.)

Ha több jó megoldás is van, bármelyik megadható.

### Korlátok
* $1 \le N \le 100000$
* $1 \le M \le 200000$
* $1 \le P \le N$
* $1 \le A_i, B_i \le N$ minden $i = 1, 2, \ldots, N$-re

### Példa bemenet
    8 10 2
    1 3
    3 6
    3 2
    2 4
    2 5
    6 7
    6 8
    1 8
    5 3
    4 7


### Példa kimenet
    3
    2 5 3

### A példa magyarázata
A legrövidebb kör az alábbi utakból áll: 2–5, 5–3 és 3–2.
A városokat bármilyen sorrendben megadhatjuk, amíg a megadott lista továbbra is egy kört alkot.
Például az 5 2 3 szintén egy érvényes megoldás.

![](tex/abra.png)
