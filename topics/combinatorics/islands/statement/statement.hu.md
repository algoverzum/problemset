## Szigetek
Régészek nemrég egy feljegyzésre bukkantak, ami leírja, ahogyan egy polinéz törzs benépesített egy korábban lakatlan csendes-óceáni szigetcsoportot. A törzs kezdetben csak egy szigeten volt jelen, de ahogy nőtt a népesség, a zsúfolt szigetekről időről időre felfedezők indultak útnak új, ismeretlen földek felé. A törzs öregei minden szigethez feljegyezték az onnan felfedezett új szigeteket. Hányféle sorrendben fedezhette fel a törzs a szigetcsoport szigeteit, ha tudjuk, hogy minden szigetet pontosan egyszer fedeztek fel, és nem történt egyszerre két felfedezés?

### Bemenet
A bemenet első sorában a szigetek száma ($1\le N\le 20\,000$) található. A következő $N$ sor közül az $i$-edik tartalmazza az $i$-edik szigetről felfedezett új szigetek számát, majd a szigetek sorszámait. Tudjuk, hogy a törzs őshazája az 1-es sziget, ezt fedezték fel először.

### Kimenet
A kimenetre a lehetséges felfedezési sorrendek számát kell kiírni. A megoldás nagyon nagy lehet, ezért az eredmény $10^9+7$-es maradékát kell megadni.

### Korlátok
* $1 \le N \le 20\,000$

### 1. példa bemenet
    5
    2 2 3
    2 4 5
    0
    0
    0

### 1. példa kimenet
    8

### Az 1. példa magyarázata
A lehetséges felfedezési sorrendek:

1 2 3 4 5

1 2 3 5 4

1 2 4 3 5

1 2 4 5 3

1 2 5 3 4

1 2 5 4 3

1 3 2 4 5

1 3 2 5 4
    
### 2. példa bemenet
    13
    4 2 3 4 6
    0
    1 5
    0
    2 7 12
    1 9
    1 8
    1 13
    2 10 11
    0
    0
    0
    0

### 2. példa kimenet
    221760
