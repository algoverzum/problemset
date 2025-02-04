## Energia cellák
Egy elhagyatott űrhajóroncsra találtunk és szeretnénk kifosztani hasznos alkatrészekért. Az energia tárolóból szeretnénk elvinni a legerősebb energia cellát. Az energia tároló egy négyzetrácsban elrendezett tároló egységekből álló téglalap. Írj egy programot, amely megtalálja a legerősebb energia cella pozícióját nullától számozva. (Ha ilyenből több van, akkor a legkisebb sorszámút keressük, azon belül pedig a legkisebb oszlopszámút.) 

### Bemenet
A bemenet első sorában kettő egész szám van, a sorok és az oszlopok száma: $N$ és $M$.
A következő $N$ sorban rendre $M$ egész szám van, az energia cellák töltöttségi szintje: $E_{ij}$

### Kimenet
Kettő egész számot kell kiírnod, a legnagyobb elem sorát, majd oszlopát. Mind kettő sorszámozást nullától kezdjük.

### Korlátok
* $1 \le N,M \le 100$
* $0 \le E_{ij} \le 1000$

### Példa bemenet
    3 4
    10 2 3 4
    0 0 16 4
    7 7 7 7 
### Példa kimenet
    1 2

### A példa magyarázata
A táblázatban szereplő legnagyobb elem az alábbi:
10 2 3 4
0 0 **16** 4
7 7 7 7 
