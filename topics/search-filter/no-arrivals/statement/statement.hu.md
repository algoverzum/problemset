## Nincs érkezés
Egy űrhajó állomásnál minden nap feljegyeztük, hogy mennyi beérkező űrhajót láttunk aznap. A feljegyzett napok között volt egy ünnepnap is, amikor nem volt közlekedés, így egy űrhajó sem érkezett aznap. A feladatod, hogy megtaláld annak a napnak a sorszámát, amelyikre esett ez az ünnepnap.

### Bemenet
A bemenet első sorában egyetlen egész szám van, a napok száma: $N$
Az azt követő $N$ sorban rendre egy szám van, az aznap leszállt űrhajók száma: $A_1, A_2, \dots, A_N$

### Kimenet
Egyetlen számot kell kiírnod, annak a napnak a sorszámát, amikor 0 érkező űrhajó volt.

### Korlátok
* $1 \le N \le 100$
* $0 \le A_i \le 100$

### 1. Példa bemenet
    6
    20
    1
    0
    3
    10
    6

### 1. Példa kimenet
    3

### Az 1. példa magyarázata
$N=6$ nap van. A harmadik napon fordult elő, hogy nem érkezett űrhajó.

### 2. Példa bemenet
    6
    32
    13
    41
    52
    13
    0

### 2. Példa kimenet
    6
