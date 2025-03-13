## Űrkereskedelem
Kettő űrhajó találkozott az világűr mélyén és úgy döntöttek, hogy cserekereskedelembe fognak. A fedélzeti számítógépek automatikusan kicsomagolják a cserére alkalmas rakományokat, de azokat, amik mind a kettő hajó raktárában vannak, azokat a raktárban fogja hagyni. Készíts programot, amely a két adott hajó raktárának tartalma alapján eldönti, hogy melyik típussú rakományok fognak a raktárban maradni!

### Bemenet
A bemenet első sorában kettő egész szám van, az első, majd a második hajó rakterében lévő rakományok száma: $N$, $M$.
A bemenet második sorában $N$ darab egész szám van, az első hajó rakterében lévő rakományok kódjai: $A_1, A_2, \dots, A_N$.
A bemenet második sorában $M$ darab egész szám van, a második hajó rakterében lévő rakományok kódjai: $B_1, B_2, \dots, B_N$.

### Kimenet
A kimenet első sorában azoknak a rakományoknak a számát írd ki, amelyek mind a kettő hajó rakterében megtalálhatóak.
A kimenet második sorában ezeknek a rakományoknak a kódját írd ki **növekvő sorrendben**.

### Korlátok
* $1 \le N, M \le 100$
* $1 \le A_i, B_i \le 1000$

### Példa bemenet
    5 6
    1 12 4 23 6
    7 4 8 9 12 6

### Példa kimenet
    3
    4 6 12

### A példa magyarázata
A 4, 6 és a 12 azok a kódok, amelyek mind az első, mind a második számsorozatban szerepel.
