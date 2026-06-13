## Edzésprogram
Tambourine-nak $N$ edzése van, ahol minden edzés hossza percekben van megadva ($M_i$). Minden alkalommal egyre több percet edz, tehát a számok **szigorúan növekednek**.

Az edzésprogram **nehézsége** a szomszédos edzések közti legnagyobb különbség (percben).

Legfeljebb $K$ új edzést szúrhat be bárhová. Ezek hossza pozitív egész perc lehet, és a teljes sorrendnek továbbra is szigorúan növekvőnek kell maradnia.
A feladat: úgy adja hozzá az új edzéseket, hogy a végső sorozatban a szomszédos edzések közti legnagyobb perc-különbség a lehető legkisebb legyen. Azaz legfeljebb $K$ edzés hozzáadásával az edzésprogramot szeretnénk a lehető legkönnyebbé tenni.

### Bemenet
A bemenet első sorában $N$ és $K$ (az edzések száma és a beszúrható új edzések száma) van.

A második sorban $N$ darab egész szám: $M_1, M_2, \ldots, M_N$, ahol $M_i$ az i-edik edzés hossza percben. A számok szigorúan növekvőek.

### Kimenet
Egyetlen számot kell kiírnod, a legfeljebb $K$ edzés hozzáadásával elérhető legkönnyebb edzésprogram nehézségét.

### Korlátok
* $2 \le N \le 10^5$
* $1 \le K \le 10^5$
* $1 \le M_i \le 10^9$
* $M_i < M_{i+1}$ minden $i = 1, 2, \ldots, N{-}1$ esetén

### 1. Példa bemenet
    3 1
    100 200 230

### 1. Példa kimenet
    50

### Az 1. példa magyarázata
Egyetlen beszúrás engedélyezett ($K = 1$). Beillesztünk egy új edzést 150 perccel:

$100 \to 150 \to 200 \to 230$

Ekkor a szomszédos különbségek:

$100 \to 150 = 50$

$150 \to 200 = 50$

$200 \to 230 = 30$

A legnagyobb különbség 50, ez a minimum, amit el lehet érni.

### 2. Példa bemenet
    5 2
    10 13 15 16 17

### 2. Példa kimenet
    2

### A 2. példa magyarázata
Tambourine legfeljebb két új edzést adhat hozzá. A beszúrt edzések félkövérrel jelölve:
$10, \mathbf{12}, 13, \mathbf{14}, 15, 16, 17$.
A nehézség ezután 2.

### 3. Példa bemenet
    5 6
    9 10 20 26 30

### 3. Példa kimenet
    3

### A 3. példa magyarázata
Tambourine legfeljebb hat új edzést adhat hozzá. A beszúrt edzések félkövérrel jelölve:
$9, 10, \mathbf{12}, \mathbf{14}, \mathbf{16}, \mathbf{18}, 20, \mathbf{23}, 26, \mathbf{29}, 30$.
A nehézség ezután 3.

### 4. Példa bemenet
    8 3
    1 2 3 4 5 6 7 10

### 4. Példa kimenet
    1

### A 4. példa magyarázata
Tambourine legfeljebb három új edzést adhat hozzá. A beszúrt edzések félkövérrel jelölve:
$1, 2, 3, 4, 5, 6, 7, \mathbf{8}, \mathbf{9}, 10$.
A nehézség ezután 1. (Tambourine valójában csak **két** új edzést adott hozzá.)
