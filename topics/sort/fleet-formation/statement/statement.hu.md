## Flottaalakzat
Egy Flottát vezetsz csatába, az ütközet előtt szeretnéd úgy elrendezni a hajóidat, hogy középen legyenek a legerősebb hajóid és a széleken a gyengébbek. Ezt úgy teszed meg, hogy középre teszed a legerősebb hajódat, majd tőle balra a második legerősebbet, majd tőlük jobbra a harmadik legerősebbet és így tovább. Add meg a hajóid erejét a rendezés után, balról jobbra haladva.

### Bemenet
A bemenet első sorában egyetlen páratlan egész szám van: $N$.<br>
A bemenet második sorában $N$ darab szám van, $S_1,S_2,\ldots,S_N$ a hajóid ereje.

### Kimenet
$N$ darab számot kell kiírnod egy sorba, a hajóid erejét, csatarendben.

### Korlátok
* $1 \le N \le 999$
* $N$ páratlan
* $1 \le S_i \le 10000$

### Példa bemenet
    7
    33 32 3 40 4 35 2

### Példa kimenet
    3 32 35 40 33 4 2

### A példa magyarázata
legerősebb hajó a 40-es, mivel páratlan hajó van ezért a 4. helyre kerül, mert így lesz középen a legnagyobb haderő.
A második legerősebb (35) hajó 3. helyre,
a harmadik legerősebb (33) az 5. helyre,
a negyedik legerősebb (32) a 2. helyre,
az ötödik legerősebb (4) a 6. helyre,
a hatodik legerősebb (3) az 1. helyre,
a hetedik legerősebb (2) a 7. helyre.
