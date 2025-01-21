## Most Frequent
A Galaktikus Tanács egy ősi adatcsomagot szerzett meg, amely a Jedik bölcsességét rejti. Az adatcsomag egy számsorozatot tartalmaz, de a kód megfejtéséhez a sorozat kulcsfontosságú elemét kell megtalálni: azt a számot, amely a leggyakrabban ismétlődik.
Ha több szám is egyforma gyakorisággal fordul elő, akkor a legkisebb számot kell választanod, mert a Jedik a szerénységet és az egyszerűséget tartották fontosnak.
Küldetésed tehát: határozd meg a sorozatban szereplő leggyakoribb (és ha kell, a legkisebb) számot, hogy felfedd az adatcsomag titkát! Az Erő vezessen!

### Bemenet
A bemenet első sorában egy egész szám van: $N$, a számsorozat hossza.
A bemenet második sorában pontosan $N$ egész szám van szóközzel elválasztva: $A_1, A_2, \ldots, A_{N}$, a sorozat elemei.

### Kimenet
Egyetlen számot kell kiírnod, az adatcsomagban szereplő leggyakoribb számot. Ha több ilyen is van, akkor a legkisebbet kell kiírni közülük.

### Korlátok
* $1 \le N \le 100$
* $1 \le A_{i} \le 100$

### Példa bemenet
    9
    5 2 2 8 5 3 5 2 8

### Példa kimenet
    2

### A példa magyarázata
Az 5 és a 2 is háromszor szerepel, a kisebb kell.
