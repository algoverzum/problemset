## Leghosszabb emelkedő
Egy zseniális tudós, Dr. Pulsar, régóta álmodozik arról, hogy az űrbe repüljön, de rakéták helyett a bolygó természeti adottságaira kell támaszkodnia. Egy különleges hegyvidéket választott ki, ahol a terep magasságát korábbi expedíciói során pontosan feltérképezte. A terv egyszerű: egy hosszú emelkedőről indítja el az űrhajóját, hogy a lehető legtöbb ideje legyen felgyorsulni. Ahhoz, hogy a kilövés sikeres legyen, meg kell találnia a terepen a leghosszabb folyamatos emelkedőt. Egy emelkedő olyan magasságokból álló szakasz, ahol minden egyes mérési ponton a magasság növekszik az előzőhöz képest. A tudós arra kér téged, hogy segíts neki meghatározni a leghosszabb ilyen emelkedő kezdő és végpontját.

### Bemenet
A bemenetben első sorában egyetlen egész szám van: $N$. <br /> 
Ezt követi $N$ sor mindegyikben egy $M_i$ szám, az $i$-edik mérés magassága ($i=1, 2, \ldots, N$).

### Kimenet
Két számot kell kiírnod, a leghosszabb emelkedő kezdő és végpontjának sorszámát. Ha nincs emelkedő, akkor -1-et kell kiírnod. Több lehetséges válasz esetén azt kell megadni, amelyiknek a legkisebb a kezdőpontja.

### Korlátok
* $1 \le N \le 1000$
* $1 \le M_i \le 1000$

### Példa bemenet
    10
    100
    110
    115
    110
    105
    115
    125
    130
    125
    125

### Példa kimenet
    5 8

### A példa magyarázata
A $100<110<115$ emelkedő 3 db magasság mérési pontot tartalmaz.

A $105<115<125<130$ emelkezdő 4 db magasság mérési pontot tartalmaz, ez a leghosszabb emelkedő.
