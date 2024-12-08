## Leghosszabb emelkedő
Egy zseniális tudós, Dr. Pulsar, régóta álmodozik arról, hogy az űrbe repüljön, de rakéták helyett a bolygó természeti adottságaira kell támaszkodnia. Egy különleges hegyvidéket választott ki, ahol a terep magasságát korábbi expedíciói során pontosan feltérképezte. A terv egyszerű: egy hosszú emelkedőről indítja el az űrhajóját, hogy a lehető legtöbb ideje legyen felgyorsulni. Ahhoz, hogy a kilövés sikeres legyen, meg kell találnia a terepen a leghosszabb folyamatos emelkedőt. Egy emelkedő olyan magasságokból álló szakasz, ahol minden egyes mérési ponton a magasság növekszik az előzőhöz képest. A tudós arra kér téged, hogy segíts neki meghatározni a leghosszabb ilyen emelkedő kezdő és végpontját.

### Bemenet
A bemenetben első sorában egyetlen egész szám van: $N$. <br /> 
Ezt követi $N$ sor mindegyik egy $M$ szám az $N$-ik mérés magassága.

### Kimenet
Két számot kell kiírnod, a leghosszabb emelkedő kezdő és végpontját. Ha nincs emelkedő akkor -1-et kell kiírnod.

### Korlátok
* $1 \le N \le 1000$
* $1 \le M \le 1000$

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
    100<110<115  3 db magasság
    105<115<125<130  4 db magasság, ez a leghosszabb emelkedő
