## Leghidegebb nap
Van egy mágikus állatunk, a josi, ami $N$ napra előre meg tudja mondani, hogy mi lesz az egyes napokon a napi középhőmérséklet. A hőmérsékletet egész számként adja meg (annál pontosabb előrejelzésre nem képes). A következő $N$ nap közül az egyik napra egy hócsatát szervezünk a barátaimmal és ehhez ki szeretnénk választani a leghidegebb napot. A josi által előrejelzett hőmérsékletek ismeretében meg tudod mondani, hogy melyik lesz a leghidegebb nap és hány fok lesz akkor a hőmérséklet?

### Bemenet
A bemenet első sorában egyetlen egész szám van: $N$ - a napok száma. A második sorban $N$ egész szám van szóközzel elválasztva, az egyes napok hőmérsékletei ($T_1, T_2, \ldots, T_N$).

### Kimenet
Két számot kell kiírnod két külön sorba, az első sorban a legalacsonyabb hőmérséklet legyen, a második sorban pedig annak a napnak a sorszáma, amikor ennyi lesz a hőmérséklet. Ha több ilyen nap is van, akkor ezek közül a legkisebb sorszámút kell megadni. 

### Korlátok
* $1 \le N \le 100$
* $-100 \le T_i \le 100$

### Példa bemenet
    5
    10 4 -5 -2 -5

### Példa kimenet
    -5
    3

### A példa magyarázata
A legalacsonyabb hőmérséklet -5 fok, és először a 3. napon lesz -5 fok.
