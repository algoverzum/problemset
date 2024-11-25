## Cukorka cserélés
Egy osztályban $N$ gyerek van. Az a hagyományuk, hogy párokba állnak a diákok és minden párban a két gyerek odaadja a cukorkáit a egymásnak. Idén a tanárnak nincs kedve párokba állítani a diákokat ezért csak sorba állította őket és a sor elejétől kezdve alkotott párokat. Ha páratlan sok diák van, akkor a sorban az utolsónak nem lesz párja és nem cserél senkivel. Adott a diákok cukorkáinak száma a cserék előtt, meg tudod mondani, hogy kinek mennyi lesz a cserék után?

### Bemenet
A bemenet első sorában a diákok száma van $N$.
A bemenet második sorában a diákok cukorkáinak száma van: $C_1, C_2, \ldots, C_N$.

### Kimenet
Az egyes diákok cukorkáinak számát kell kiírnod a cserék után egy sorba, szóközzel elválasztva.

### Korlátok
* $1 \le N \le 1\,000$
* $1 \le C_i \le 1\,000$

### Példa bemenet
    5
    9 4 5 2 3

### Példa kimenet
    4 9 2 5 3

### A példa magyarázata
    Az 1. diáknak 9, a másodiknak 4 cukorkája van. Cserélnek, az elsőnek 4 lesz, a másodiknak 9.
    A 3. diáknak 5 cukorkája van, a 4. diáknak 2. Cserélnek, a harmadiknak 2 lesz és a negyediknek pedig 5.
    Az 5. diáknak nincs párja ezért nem cserél senkivel, így 3 cukorkája marad.
