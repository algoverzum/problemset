## Robot selejtezés
A Galaktikus Birodalom robotjavító üzemében felírták az oda érkező robotok azonosító számait. Azt kell kideríteni, hogy melyik robot érkezett már korábban is javításra, és javasolni, hogy selejtezzék le.

### Bemenet
A bemenet első sora $N$, a listán szereplő azonosítók száma.
A második sora $N$ azonosítót tartalmaz szóközzel elválasztva: $A_0, A_1, \ldots, A_{N-1}$.

### Kimenet
Írj ki **-1**-et ha a listán minden azonosító különböző. Különben pedig a legelső ismétlődő azonosító első és második előfordulásának **indexeit** egy sorban.

### Korlátok
* $1 \le N \le 10^5$
* $-10^9 \le A_i \le 10^9$

### 1. Példa bemenet
    8
    -1 4 -3 1 7 4 7 4

### 1. Példa kimenet
    1 5

### Az 1. példa magyarázata
A 4-es azonosítójú robot és a 7-es is többször volt javítva, de a 4-es szerepel korábban.

### 2. Példa bemenet
    8
    -1 4 -3 1 7 -4 8 9

### 2. Példa kimenet
    -1
