## Klingon próba
Egy fiatal klingon harcos arra törekszik, hogy kivívja helyét a Nagytanácsban. A Felemelkedés Szertartásának részeként egy sor harci próbán kell átesnie, amelyek mindegyikéhez egy tiszteletérték tartozik — ez jelzi a próba nehézségét.

A próbák rögzített sorrendben követik egymást. Néhányat kihagyhat, de csak előre haladhat — ha egy próbát kihagyott, ahhoz már nem térhet vissza. A célja, hogy egyre nehezebb, szigorúan növekvő tiszteletértékű próbákból álló sorozatot teljesítsen, és ebből a lehető legtöbbet.

A feladatod: határozd meg, hogy legfeljebb hány próbát tud így teljesíteni — azaz mi a próbák nehézségi értékeiből képzett leghosszabb szigorúan növekvő részsorozat hossza.

### Bemenet
Az első sorban egy egész szám van: $N$ – az elérhető próbák száma.

A második sorban $N$ egész szám szerepel: $T_1, T_2, \ldots, T_N$ – a próbák tiszteletértékei az adott sorrendben.

### Kimenet
Egyetlen számot kell kiírnod, a leghosszabb növekvő nehézségű próbasorozat hosszát.

### Korlátok
* $1 \le N \le 1000$
* $1 \le T_i \le 10^9$ minden $1 \le i \le N$ esetén

### Példa bemenet
    11
    8 3 4 6 5 2 1 7 9 1 9

### Példa kimenet
    5

### A példa magyarázata
Egy lehetséges leghosszabb növekvő sorozat: $3, 4, 5, 7, 9$.

Egy másik érvényes sorozat: $3, 4, 6, 7, 9$.

Mindkettő hossza 5.
