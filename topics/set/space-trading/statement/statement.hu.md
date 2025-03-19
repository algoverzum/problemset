## Űrkereskedelem
Kettő űrhajó találkozott a világűr mélyén és úgy döntöttek, hogy cserekereskedelembe fognak. Az első űrhajó raktárában $N$ *különböző* rakomány van, a második űrhajó raktárában pedig $M$ *különböző* rakomány. Minden árut egy számkóddal azonosítunk, és értelemszerűen az azonos kódú áruk megegyeznek, a különbözőek pedig nem. A fedélzeti robotok automatikusan kicsomagolják a cserére alkalmas rakományokat, de amik mind a kettő hajó raktárában vannak, azokat a raktárban szeretnék hagyni. Készíts programot, amely a két hajó raktárának tartalma alapján eldönti, hogy melyik rakományok fognak a raktárban maradni!

### Bemenet
A bemenet első sorában kettő egész szám van, az első, majd a második hajó rakterében lévő rakományok száma: $N$, $M$.
A bemenet második sorában $N$ darab különböző egész szám van, az első hajó rakterében lévő rakományok kódjai: $A_1, A_2, \dots, A_N$.
A bemenet második sorában $M$ darab különböző egész szám van, a második hajó rakterében lévő rakományok kódjai: $B_1, B_2, \dots, B_M$.

### Kimenet
A kimenet első sorában azoknak a rakományoknak a számát írd ki, amelyek mind a kettő hajó rakterében megtalálhatóak.
A kimenet második sorában ezeknek a rakományoknak a kódját írd ki **növekvő sorrendben**.

### Korlátok
* $1 \le N, M \le 10^5$
* $1 \le A_i \le 10^9 (1 \le i \le N)$
* $1 \le B_i \le 10^9 (1 \le i \le M)$
* $A_i \ne A_j$, minden $i \ne j$ -re
* $B_i \ne B_j$, minden $i \ne j$ -re

### Példa bemenet
    5 6
    1 12 4 23 6
    7 4 8 9 12 6

### Példa kimenet
    3
    4 6 12

### A példa magyarázata
A 4, 6 és a 12 azok a kódok, amelyek mind az első, mind a második számsorozatban szerepelnek.
