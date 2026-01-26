## Harcosok
Egy kalandjátékban $n$ harcos vesz részt. A harcosok száma **páros**. Az $i$-edik harcos erejét az $a_i$ szám jelöli.

A játék mestere $\frac{n}{2}$ párost szeretne kialakítani úgy, hogy:

* minden páros pontosan két harcosból álljon,
* minden harcos pontosan egy párosba kerüljön,
* egy párost csak azonos erejű harcosok alkothatnak (különben nem tudnak együtt harcolni).

A harcosok edzhetnek, hogy növeljék az erejüket.
Minden egyes edzés eggyel növeli a harcos erejét.

A játék mestere szeretné tudni, hogy összesen legalább hány edzésre van szükség, hogy pontosan $\frac{n}{2}$ páros jöjjön létre (vagyis minden harcos találjon párt magának).

A feladatod ennek a minimális számnak a meghatározása.

### Bemenet
A bemenet első sora egy egész számot tartalmaz: $n$ - a harcosok száma. Garantált, hogy $n$ páros.

A bemenet második sora $n$ egész számot tartalmaz: $a_1, a_2, \ldots, a_n$, ahol $a_i$ az $i$-edik harcos ereje.

### Kimenet
Egyetlen számot kell kiírnod, az edzések minimális számát, amely szükséges ahhoz, hogy pontosan $\frac{n}{2}$ páros alakuljon ki.

### Korlátok
* $2 \le n \le 100$
* $1 \le a_i \le 100$ minden $i=1,2,\ldots,n$ esetén. 

### 1. Példa bemenet
    6
    5 10 2 3 14 5

### 1. Példa kimenet
    5

### Az 1. példa magyarázata
Az első példában az optimális csapatok a következők lesznek: (3,4) (1,6) és (2,5), ahol a zárójelben lévő számok a harcosok indexei. Az első párosnál (3,4) a képességek különbsége $|3-2|=1$, tehát 1 edzésre van szükség. A második párosnál (1,6) a képességek különbsége $|5-5|=0$, tehát 0 edzés szükséges. A harmadik párosnál (2,5) a képességek különbsége $|14-10|=4$, tehát 4 edzés szükséges. Összesen tehát: $1+0+4=5$

### 2. Példa bemenet
    2
    1 100

### 2. Példa kimenet
    99

### Az 2. példa magyarázata
A második példában az első harcos 99 edzés után tud a másodikkal egy csapatot alkotni.
