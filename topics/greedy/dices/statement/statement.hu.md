## Dobókockák
Bár egy tipikus dobókocka 6 oldalú, ahol az oldalak 1-től 6-ig számozottak, sok játékban másfajta kockákat is használnak. $D_k$ egy olyan kocka, amelynek $k$ oldala van, és az oldalak mutat 1-től $k$-ig számozottak. Például $D_6$ egy tipikus kocka, $D_4$ négyoldalú, míg $D_{1000000}$ egymillió oldalú.

![](dices.png)

Ebben a feladatban $N$ darab kockát kapunk. Az $i$-edik kocka egy $D_{S_i}$, azaz $S_i$ oldalú, és az oldalain 1-től $S_i$-ig szerepelnek az egész számok.

Egy $M$ hosszúságú sorozat az $1, 2, \ldots, M$ számok listája. A cél, hogy kiválasszunk néhány kockát (akár mindet), és mindegyikről egy számot választva egy ilyen sorozatot hozzunk létre. Mi a leghosszabb sorozat, amit így meg tudunk alkotni?

### Bemenet
A bemenet első sora tartalmazza $N$ értékét - a játékban szereplő kockák számát.

A második sor $N$ darab egész számot tartalmaz: $S_1, S_2, \ldots, S_N$, amelyek mindegyike egy kocka oldalainak számát jelöli.

### Kimenet
Írj ki egyetlen számot: a leghosszabb sorozat hosszát, amit a megadott kockákból létre lehet hozni.

### Korlátok
* $1 \le N \le 10^5$
* $4 \le S_i \le 10^6$, minden $i$-re

### 1. Példa bemenet
    4
    6 10 12 8

### 1. Példa kimenet
    4

### 1. példa magyarázata
Az összes kockát felhasználhatjuk, hogy létrehozzuk az $1,2,3,4$ sorozatot.

### 2. Példa bemenet
    6
    5 4 5 4 4 4

### 2. Példa kimenet
    5

### 2. Példa magyarázata
Az összes kockát felhasználhatjuk, hogy létrehozzuk az $1,2,3,4$ sorozatot.

### Példa bemenet 2

6
5 4 5 4 4 4

### Példa kimenet 2

5

### Magyarázat a 2. példához
Mivel egyik kocka sem tud 5-nél nagyobb számot mutatni, nem lehet 5-nél hosszabb sorozatot alkotni. Többféle módon is létrehozható pontosan 5 hosszú sorozat. Például: válasszuk a 4-et és az 5-öt a két $D_5$-ből, majd az 1, 2 és 3 számokat három $D_4$-ből, így megkapjuk az $1,2,3,4,5$ sorozatot.

### 3. Példa bemenet
    10
    10 10 7 6 7 4 4 5 7 4

### 3. Példa kimenet
    9

### 3. Példa magyarázata
Lehetséges létrehozni az $1,2,3,4,5,6,7,8,9$ sorozatot úgy, hogy az egyik $D_4$-et elhagyjuk és felhasználjuk a $D_4$-eket, a $D_5$-öt és a $D_6$-ot az 1–4 számokhoz; a $D_7$-eket a 4–7 számokhoz; valamint a $D_{10}$-eket a 8 és 9 számokhoz. Nem lehetséges 10 hosszú sorozatot létrehozni, így 9 a legjobb eredmény.

### 4. Példa bemenet
    1
    10

### 4. Példa kimenet
    1

### 4. Példa magyarázata
Csak 1 hosszú sorozatot tudunk létrehozni.
