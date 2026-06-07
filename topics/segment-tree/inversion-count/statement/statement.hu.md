## Inverziók Száma
Adott az $A$ tömb, amely $n$ darab, egymástól különböző pozitív egész számot tartalmaz. Egy $(i,j)$ indexpárt **inverziónak** nevezünk, ha $i<j$ és $A[i]>A[j]$.

Határozzuk meg az adott tömbben található inverziók számát.

### Bemenet
A bemenet első sora a tesztesetek számát, $T$-t tartalmazza.

Minden teszteset első sora egy $n$ egész számot tartalmaz. Ezt követi $n$ sor, amelyek közül az $i$-edik sor az $A[i]$ elemet adja meg.

Az egyes teszteseteket egy üres sor választja el egymástól.

### Kimenet
Minden tesztesethez írj ki egy sort, amely az adott tömbben található inverziók számát tartalmazza.

### Korlátok
* $1 \le n \le 200\,000$
* $1 \le A[i] \le 10^6$ minden $i$-re
* $A[i] \neq A[j]$ ha $i \neq j$
* Az összes tesztesetben szereplő tömbök méreteinek összege legfeljebb $200\,000$.

### Példa bemenet
    2
    
    3
    3
    1
    2
    
    5
    2
    3
    8
    6
    1

### Példa kimenet
    2
    5
