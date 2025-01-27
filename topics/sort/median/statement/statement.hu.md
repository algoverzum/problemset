## Medián
Egy új űrhajót tesztelünk és lemértük pár alkalommal, hogy milyen hosszú ideig tartott, amíg kiértünk a légkörből vele. Szeretnénk a piacra dobni, de tudnunk kell előtte, hogy mi a medián idő, amíg ki tud érni a légkörből. Írj egy programot, ami megállapítja ezt. A mediánja egy számsornak a növekvő sorrendben pont középen elhelyezkedő szám. Ez egyértelmű, ha páratlan darab szám van, viszont a ha páros, akkor a kettő középső számból vegyük a kisebbet.

### Bemenet
A bemenet első sorában egyetlen egész szám van, a mérések száma: $N$.
A bemenet második sorában $N$ egész szám van, a mérések eredményei: $A_1, A_2, \ldots, A_N$ .

### Kimenet
Egyetlen számot kell kiírnod, a mérések medián értékét.

### Korlátok
* $1 \le N \le 100$
* $1 \le A_i \le 1000$

### Példa bemenet
    6
    5 4 1 1 4 3

### Példa kimenet
    3

### A példa magyarázata
A számok rendezve:
1 1 3 4 4 5
A középső számok a 3 és a 4, ezek közül a kisebb a 3.
