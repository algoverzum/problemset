## k-ismétlés
Egy karakterláncot akkor nevezünk $k$-stringnek, ha megadható úgy, mint egy karakterlánc $k$ összefűzött példánya. Például az "aabaabaabaab" karakterlánc egyszerre 1-string, 2-string és 4-string, de nem 3-string, 5-string vagy 6-string stb. Nyilvánvaló, hogy bármely karakterlánc 1-string.

Adott egy $s$ karakterlánc, amely angol kisbetűkből áll, és egy pozitív egész $k$ szám. Át lehet-e rendezni az $s$ karakterlánc betűit úgy, hogy az eredmény egy $k$-string legyen?

### Bemenet
Az első sor egy $k$ egész számot tartalmaz.  
A második sor tartalmazza $s$-et, amit $k$ részre szeretnénk vágni.

### Kimenet
Írd ki, hogy *YES* ha az $s$ karakterlánc betűit át lehet rendezni úgy, hogy az eredmény egy $k$-string legyen.  
Ha nem lehet átrendezni, akkor írd ki, hogy *NO*.

### Korlátok
* $1\le k\le 1000$
* $1\le |s| \le 1000$, ahol $|s|$ a $s$ karakterlánc hossza
* $s$ összes karaktere angol kisbetű

### 1. példa bemenet
    2
    aazz

### 1. példa kimenet
    YES

### Az 1. példa magyarázata
Két megoldás is van: azaz és zaza.

### 2. példa bemenet
    3
    abcabcabz

### 2. példa kimenet
    NO
