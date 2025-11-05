## Tripla Dupla
Frici **két** dobókockával dobott egyszerre egymás után $N$-szer. A társasjátékban, amit éppen játszik, az a szabály, hogyha háromszor egymás után ugyanazt dobja a két dobókockával, akkor a börtön mezőre kell lépnie. A bemenetben megkapod $N$ értékét, aztán pedig az $N$ dobáspár eredményét. Írd ki, hogy **Yes**, ha történt egymás után három duplázás, és **No**, ha nem.

### Bemenet
A bemenetet első sorában találjuk $N$ értékét, amit $N$ sor követ, mindegyikben szóközzel elválasztva a két kockadobás értékével. (Az $i$-edik sorban a két dobás: $D_{i,1}$ és $D_{i,2}$.)

### Kimenet
Írd ki, hopy **Yes**, ha legalább háromszor egymás után előfordult duplázás. Ellenkező esetben írd ki, hogy **No**.

### Korlátok
* $3 \le N \le 100$
* $1 \le D_{i,1}, D_{i,2} \le 6$
* Ezek mindegyike egész szám.

### 1. példa bemenet
    5
    1 2
    6 6
    4 4
    3 3
    3 2

### 1. példa kimenet
    Yes

### Az 1. példa magyarázata
A második, harmadik és a negyedik dobások is dupláztak.

### 2. példa bemenet
    5
    1 1
    2 2
    3 4
    5 5
    6 6

### 2. példa kimenet
    No

### 3. példa bemenet
    6
    1 1
    2 2
    3 3
    4 4
    5 5
    6 6

### 3 példa kimenet
    Yes
