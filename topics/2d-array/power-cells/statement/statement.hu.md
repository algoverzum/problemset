## Energia cellák
Egy elhagyatott űrhajóroncsra találtunk és szeretnénk kifosztani hasznos alkatrészekért. Az energia tárolóból szeretnénk elvinni a legerősebb energia cellát. Az energia tároló egy négyzetrácsban elrendezett tároló egységekből álló téglalap. Írj egy programot, amely megtalálja a legerősebb energia cella pozícióját. Ha ilyenből több van, akkor a legkisebb sorszámút keressük, azon belül pedig a legkisebb oszlopszámút. A sorokat és oszlopokat is $1$-től kezdve sorszámozzuk.

### Bemenet
A bemenet első sorában kettő egész szám van, az energia tároló sorainak és az oszlopainak száma: $N$ és $M$.
A következő $N$ sorban rendre $M$ egész szám van, az energia cellák töltöttségi szintje: $E_{i, j}$.

### Kimenet
Kettő egész számot kell kiírnod, a legnagyobb elem sorát, majd oszlopát. Mind kettő sorszámozást egytől kezdjük.

### Korlátok
* $1 \le N,M \le 100$
* $0 \le E_{i, j} \le 1000$

### Példa bemenet
    3 4
    10 2 3 4
    0 0 16 4
    7 7 7 7 

### Példa kimenet
    2 3

### A példa magyarázata
A táblázatban szereplő legnagyobb elem az alábbi:
10 2 3 4
0 0 **16** 4
7 7 7 7 
