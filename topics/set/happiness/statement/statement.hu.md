## Boldogság
A USS Enterprise fedélzetére új rakomány érkezett. A szállítmány minden ládáját egy azonosító számmal jelölik.

A Csillagflotta két listát is átadott:

* $A$ halmaz (előnyben részesített készletek): Ezek a nagy értékű vagy alapvető fontosságú szövetségi áruk.
* $B$ halmaz (korlátozott rakomány): Ezek a nem kívánt vagy problémás áruk, amelyek problémákat okozhatnak.

A rakomány kezdeti boldogság faktora 0. Ahogy megvizsgálod az egyes ládákat:

* Ha az azonosítója az $A$ halmazban van, akkor a boldogság faktor 1-gyel nő (ami növeli a küldetés sikerét).
* Ha a láda azonosítója a $B$ halmazban van, a boldogságérték 1-gyel csökken (potenciális problémát okoz).
* Ellenkező esetben a rakomány boldogság faktora változatlan marad.

A végén jelentsed a végső boldogság faktort.

### Bemenet
Az első sorban az $N$ és $M$ egész számok vannak szóközzel elválasztva.

A második sor $N$ egész számot tartalmaz, a rakomány azonosítóinak az $S$ sorozatát.
A harmadik és negyedik sor $M$ egész számot tartalmaz, $A$ és $B$ értékeit.

### Kimenet
Egyetlen egész számot írj ki, a végső boldogság faktort.

### Korlátok
* $1 \le N \le 10^5$
* $1 \le M \le 10^5$
* $1 \le S_i, A_i, B_i \le 10^9$
* $A$ és $B$ diszjunkt

### Példa bemenet
    4 2
    1 5 3 9
    3 1
    5 7

### Példa kimenet
    1

### A példa magyarázata
Az $A$ halmaz 3 és 1 elemi boldogságot szereznek. A $B$ halmazban az 5 miatt veszítesz egyet. 9 nem változtat semmin.
