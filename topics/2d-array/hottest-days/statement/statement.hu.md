## Legmelegebb napok száma
Adott $N$ városra az elmúlt $M$ nap mindegyikére az aznap mért legmagasabb hőmérséklet. Jelöljük a maximális előfordult hőmérsékleti értéket $H$-val. Add meg minden városra, hogy ott hány napon volt $H$ fok.

### Bemenet
A bemenet első sorában két szám van: $N$ és $M$ - a városok és a napok száma. Az ezt követő $N$ sor mindegyikében $M$ darab egész szám van szóközökkel elválasztva. Az $i$-edik sorban a $j$-edik szám $T_{i,j}$, ami az $i$-edik városban a $j$-edik napon a napi maximum hőmérséklet. 

### Kimenet
$N$ számot kell kiírnod külön sorokban, az $i$-edik sorba azt, hogy az $i$-edik városban hány napon fordult elő a maximális $H$ hőmérséklet.

### Korlátok
* $1 \le N, M \le 100$
* $-50 \le T_{i,j} \le 50$

### Példa bemenet
    3 4
    2 -3 5 18
    18 18 18 18
    10 0 16 17

### Példa kimenet
    1
    4
    0

### A példa magyarázata
A maximális hőmérséklet $H = 18$ fok. Az első városban egyszer volt 18 fok, a második városban négyszer, a harmadik városban egyszer sem.
