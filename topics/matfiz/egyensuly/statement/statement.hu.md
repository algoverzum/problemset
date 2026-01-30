## Egyensúly
Aranyvárban elérkezett az Egyensúly Napja. A birodalom uralkodója úgy határozott, hogy az ünnep alkalmából minden alattvaló életét azonos szintre hozza a királyi aranytár segítségével.

A birodalomban összesen $n$ lakos él. Az $i$-edik lakos jólétét egy egész szám írja le, $a_i$ aranypénzben mérve (ez Aranyvár hivatalos fizetőeszköze).

Te vagy a királyi számvevő, akinek ki kell számolnia, hogy az uralkodónak minimálisan mennyi aranypénzt kell kiosztania ahhoz, hogy mindenki jóléte egyenlő legyen. Fontos, hogy az uralkodó csak adományozhat, elvenni senkitől sem áll módjában.

### Bemenet
Az első sorban egy egész szám szerepel, $n$ – a birodalom lakosainak száma.

A második sor $n$ darab egész számot tartalmaz: $a_1, a_2, \ldots, a_n$, ahol $a_i$ az $i$-edik lakos jóléte.

### Kimenet
Írd ki azt az egyetlen egész számot, $S$-t, amely megadja, hogy az uralkodónak minimálisan hány aranypénzt kell elosztania.

### Korlátok
* $1 \le n \le 100$
* $0 \le a_i \le 10^6$ minden $i=1,2,\ldots,n$

### 1. Példa bemenet
    5
    0 1 2 3 4

### 1. Példa kimenet
    10

### Az 1. példa magyarázata
Ha az első polgárhoz 4, a másodikhoz 3, a harmadikhoz 2, a negyedikhez pedig 1 aranyat adunk, akkor az összes polgár jóléte 4 lesz.

### 2. Példa bemenet
    5
    1 1 0 1 1

### 2. Példa kimenet
    1

### Az 2. példa magyarázata
Elég, ha a harmadik polgárnak egy aranyat adunk.

### 3. Példa bemenet
    3
    1 3 1

### 3. Példa kimenet
    4

### Az 3. példa magyarázata
Két aranyat kell adni az első és a harmadik polgárnak, hogy a polgárok jóléte 3 legyen.

### 4. Példa bemenet
    1
    12

### 4. Példa kimenet
    0

### Az 4. példa magyarázata
Semmit sem kell adni, mert minden polgárnak 12 burlese van.
