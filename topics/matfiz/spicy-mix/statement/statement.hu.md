## Csípős keverék
Rudolf egy új, különleges csípős ételt készít. A recept szerint pontosan két fűszert kell összekevernie:

* egyet az $A$ dobozból,
*egyet a $B$ dobozból.

Minden fűszernek van egy csípősségértéke, amely azt jelzi, mennyire égeti a nyelvet.

* Az $A$ dobozban $n$ fűszer található, csípősségeik: $a_1, a_2, \ldots, a_n$.
* A $B$ dobozban $m$ fűszer található, csípősségeik: $b_1, b_2, \ldots, b_m$.

Rudolf szeretné, hogy az étel összcsípőssége ne legyen nagyobb, mint a megengedett $k$ érték, különben ehetetlenül csípős lesz.

Ez azt jelenti, hogy az $A$ doboz $i$-edik és a $B$ doboz $j$-edik fűszere csak akkor keverhető össze, ha $a_i+b_j\le k$.

A feladatod, hogy megszámold, hány olyan $(i,j)$ fűszerpár létezik, amelynek összcsípőssége nem haladja meg $k$-t.

### Bemenet
Az első sor három egész szám van: $n, m, k$.  
A második sorban $n$ egész szám, az $A$ doboz fűszereinek csípőssége van.  
A harmadik sorban $m$ egész szám, a $B$ doboz fűszereinek csípőssége van.

### Kimenet
Egyetlen számot kell kiírnod, az olyan $(i,j)$ fűszerpárok számát, amire $a_i+b_j\le k$.

### Korlátok
* $1 \le n,m \le 1000$
* $1 \le a_i \le 1000$ minden $i=1,2,\ldots,n$-re.
* $1 \le b_j \le 1000$ minden $i=1,2,\ldots,m$-re.
* $1 \le k \le 2000$

### 1. példa bemenet
    4 4 8
    1 5 10 14
    2 1 8 1

### 1. példa kimenet
    6

### Az 1. példa magyarázata
Rudolf a következő indexpárokat választhatja ki: [1,1],[1,2],[1,4],[2,1],[2,2],[2,4].

### 2. példa bemenet
    2 3 4
    4 8
    1 2 3

### 2. példa kimenet
    0

### A 2. példa magyarázata
Rudolf akárhogyan választ ki két fűszert, ezek csípősségének összege meghaladja a $k=4$ értéket.

### 3. példa bemenet
    3 4 2000
    1 1 1
    1 1 1 1

### 3. példa kimenet
    12

### A 3. példa magyarázata
Rudolf az $A$ dobozból és a $B$ dobozból is bármelyik fűszert választhatja.
