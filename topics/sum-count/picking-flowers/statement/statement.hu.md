## Virágszedés
Aladár virágokat szed. $N$ virágot lát a réten, mindegyikről tudja, hogy hány szirma van (ezek a számok fel vannak sorolva a bemeneten). Csak a páratlan szirmú virágokat szedi össze. Hány virág marad a réten?  
Az első szám azt jelenti, hogy mennyi virágot lát, utána következnek egyesével, hogy melyik virágnak mennyi szirma van.

### Bemenet
A bemenet első sorában a virágok száma van: $N$. Ezt követően adott $N$ szám, mindegyik külön sorban, az egyes virágok szirmainak száma ($S_1, S_2, \ldots, S_N$).  

### Kimenet
Egyetlen számot kell kiírnod, a réten maradó virágok számát. 

### Korlátok
* $1 \le N \le 100$
* $1 \le S_i \le 100$

### Példa bemenet
    5
    7
    4
    3
    11
    6

### Példa kimenet
    2

### A példa magyarázata
A 4 és 6 szirmú virágok maradnak a réten, a többit leszedi Aladár.
