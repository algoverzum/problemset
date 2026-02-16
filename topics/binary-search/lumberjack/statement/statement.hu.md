## Favágó
Egy faipari vállalatnak egy sorban álló, adott magasságú fákból legalább $M$ méter faanyagot kell kitermelnie. Egy vágógépet használnak, amelynél beállítható egy $H$ vágási magasság: a gép minden fából levágja a $H$ fölötti részt, az alacsonyabb fák változatlanok maradnak. A levágott darabok adják a kitermelt famennyiséget.

A cél a lehető legnagyobb egész $H$ érték meghatározása úgy, hogy a levágott faanyag hossza legalább $M$ méter legyen.

### Bemenet
Az első sor: $N$ (fák száma) és $M$ (szükséges famennyiség).  
A második sor: $N$ darab pozitív egész szám $A_1, A_2, \ldots, A_n$- a fák magasságai.

### Kimenet
A maximális egész $H$ vágási magasság, amivel a levágott fa öszhossza legalább $M$ méter.

### Korlátok
* $1 \le N \le 10^5$
* $1 \le M \le 2\cdot 10^{9}$
* $1 \le \A_i \le 10^9$ minden $i=1, 2, \ldots, N$ esetén
* $A_1 + A_2 + \ldots + A_n \ge M$

### 1. Példa bemenet
    4 7
    15 10 5 12

### 1. Példa kimenet
    10

### Az 1. példa magyarázata
Például, ha a fasorban 15, 10, 5 és 12 méter magas fák vannak, és 10 méter magasra emelik a fűrészlapot, akkor a vágás után megmaradó fák magassága 10, 10, 5 és 10 méter lesz. Az első fából 5 métert, a negyedik fából pedig 2 métert vágnak le (összesen 7 méter fát).

### 2. Példa bemenet
    5 20
    14 52 50 36 56

### 2. Példa kimenet
    46
