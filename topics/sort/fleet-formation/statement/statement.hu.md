## Flottaalakzat
Egy Flottát vezetsz csatába, az ütközet előtt szeretnéd úgy elrendezni a hajóidat, hogy középen legyenek a legerősebb hajóid és a széleken a gyengébbek. Ezt úgy teszed meg, hogy középre teszed a legerősebb hajódat, majd tőle balra a második legerősebbet, majd tőlük jobbra a harmadik legerősebbet és így tovább. Add meg a hajóid erejét a rendezés után, balról jobbra haladva.

### Bemenet
A bemenetben első sorában egyetlen egész páratlan szám van: $N$<br>
A bemenet második sorában $N$ db $H$ szám van, a hajóid ereje 

### Kimenet
$N$ db számot kell kiírnod egy sorba, a hajóid erejét

### Korlátok
* $1 \le N \le 999$
* $1 \le H \le 10000$

### Példa bemenet
    7
    33 32 3 40 4 35 2

### Példa kimenet
    3 32 35 40 33 4 2

### A példa magyarázata
legerősebb hajó 40, mivel páros db hajó van ezért a 4. helyre kerül, mert így lesz középen a legnagyobb haderő, mert második legerősebb hajó tőle balra kerül.<br>
második legerősebb hajó 3.hely<br>
harmadik legerősebb 5.hely<br>
negyedik legerősebb 2.hely<br>
ötödik legerősebb 6.hely<br>
hatodik legerősebb 1.hely<br>
hetedik legerősebb 7.hely<br>