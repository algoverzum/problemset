## Hajóépítő
Sikeres űrhajóépítő vállalkozó vagy, és olyan népszerű lettél, hogy több megbízást kapsz, mint amennyit el tudsz végezni. Szerencsére korszerű felszereléseidnek köszönhetően bármilyen űrhajót pontosan egy nap alatt el tudsz készíteni.
Rendelkezésedre áll egy $N$ elemű lista, amelyben az egyes megbízások határideje szerepel, növekvő sorrendben. Egy megrendelést akkor tekintünk időben teljesítettnek, ha legkésőbb a határidő napján elkészül.
Határozd meg, legfeljebb hány űrhajót tudsz határidőre elkészíteni, és add meg ezeknek az indexeit!

### Bemenet
A bemenet első sorában egyetlen egész szám van: $N$ a megbízások darabszáma. <br>
A bemenet második sorában $N$ db egész szám szerepel: $H_1, H_2, \ldots, H_N$, ahol $H_i$ az $i$-edik megrendelés határideje.

### Kimenet
A kimenet első sorába egyetlen számot kell kiírnod, $S$-et a megbízások számát, amelyeket sikeresen el tudtál végezni határidőre.<br>
A második sorban $S$ db szám szerepeljen növekvő sorrendben: azoknak a megrendeléseknek az 1-től indexelt sorszámai, amelyeket teljesítettél.

### Korlátok
* $1 \le N, H_i \le 100\,000$
* $H_i \le H_j$ minden $1 \le i < j \le N$ esetén

### Példa bemenet
    7
    1 1 2 2 2 4 4
    
### Példa kimenet
    4
    1 3 6 7

### A példa magyarázata
Az első napon elkészítjük az 1-es megrendelést (határidő: 1. nap).<br>
A második napon elkészítjük a 3-as megrendelést (határidő: 2. nap).<br>
A harmadik napon elkészítjük a 6-os megrendelést (határidő: 4. nap).<br>
A negyedik napon elkészítjük a 7-es megrendelést (határidő: 4. nap).

