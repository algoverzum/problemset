## Cukorka Cserélés
Egy osztályban $N$ gyerekek van. Az a hagyományuk, hogy párokba állnak a diákok és minden párban a két gyerek odaadja a cukorkáit a egymásnak. Idén a tanárnak nincs kedve párokba állítani a diákokat ezért csak sorba állította őket és a sor elejétől kezdve alkotott párokat.

### Bemenet
A bemenet első sorában a diákok száma van $N$.
A bemenetben második sorában a diákok cukorkáinak száma van. $A_1, A_2, \ldots, A_{N}$.

### Kimenet
Az összes diák cukorkáinak számát kell kiírnod egy sorba szóközzel elválasztva.

### Korlátok
* $1 \le N \le 1000$
* $1 \le A \le 1000$

### Példa bemenet
    5
    9 4 5 2 3

### Példa kimenet
    4 9 2 5 3

### A példa magyarázata
    1. diáknak 9, másodnak 4 cukorkája van. Cserélnek elsőnek 4 lesz másodiknak 9.
    3. diáknak 5, cukorkája van, 4. diáknak 2 Cserélnek harmadiknak 2 lesz negyediknek pedig 5.
    5. diáknak nincs párja ezért nem cserél senkivel, így 5 cukorkája marad.
