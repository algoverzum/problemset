## Klingon Próba
Egy fiatal klingon harcos arra törekszik, hogy helyet szerezzen magának a Nagytanácsban. A Felemelkedés Szertartásának részeként egy sor harci próbán kell átesnie — mindegyikhez tartozik egy tiszteletérték, amely a próba nehézségét és presztízsét jelzi.

Ezeket a próbákat **rögzített sorrendben** kell teljesíteni, ahogyan azt az ősi hagyomány megköveteli.

A harcos célja, hogy kiválasszon egy szigorúan növekvő sorrendű részsorozatot — olyat, amely a lehető legnagyobb tiszteletet hozza számára bajtársai körében.

Ha szükséges, kihagyhat néhány próbát, de a sorrendden nem változtathat, nem térhet vissza egy korábbi próbához, ha azt már kihagyta.

A te feladatod, hogy segíts megtalálni a harcos számára a leghosszabb növekvő tiszteletértékű próbasorozatot — vagyis a leghosszabb láncot egyre nagyobb presztízsű próbákból, amelyeket teljesíthet az adott sorrenden belül.

### Bemenet
Az első sor egy egész számot tartalmaz: $N$ – az elérhető próbák száma.

A második sor $N$ egész számot tartalmaz: $T_1, T_2, \ldots, T_N$ – a próbák tiszteletértékei az adott sorrendben.

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
Egy lehetséges leghosszabb növekvő sorozat: $3, 4, 5, 7, 9$

Egy másik érvényes sorozat: $3, 4, 6, 7, 9$

Mindkettő hossza: 5
