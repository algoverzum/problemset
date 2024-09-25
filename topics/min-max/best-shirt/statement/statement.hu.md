## Legjobb ing
A barátnőm Nena egy inget akar venni a barátjának szülinapjára. A boltban $N$ ing közül választhat, amelyek árai $P_1, P_2, \ldots, P_N$ peták. Nenának $K$ petákja van, ebből szeretné a lehető legdrágább inget megvenni, amire még van elég pénze, mert tudja, hogy minél jobb egy ing, annál drágább. Melyik inget válassza, és hány petákjába fog ez kerülni?

### Bemenet
A bemenet első sorában két egész szám van: $N$ és $K$ - az ingek száma és Nena zsebpénze petákban. A második sorban $N$ egész szám van szóközzel elválasztva, az ingek árai ($P_1, P_2, \ldots, P_N$). 

### Kimenet
Két számot írj ki külön sorokban, az első szám a kiválasztott ing sorszáma, a második pedig az ára legyen. Ha több ilyen árú ing is van, akkor ezek közül a legkisebb sorszámút kell megadni. Ha Nena nem tud megvenni egy inget sem, akkor a kimenet mindkét sorába egy 0-t írj.

### Korlátok
* $1 \le N \le 100$
* $1 \le K \le 1000$
* $1 \le P_i \le 1000$


### Példa bemenet
    7 333
    95 760 130 299 334 299 42

### Példa kimenet
    4
    299

### A példa magyarázata
Nena a 333 petákjával az 1., 3., 4., 6. és 7. inget tudja megvenni (áraik 95, 130, 299, 299, 42). Ezek közül a legdrágább a 4., ami 299 petákba kerül (illetve a 6. is ennyi, de a kisebb sorszámút kell megadni).

### 2. példa bemenet
    4 42
    150 50 900 299

### 2. példa kimenet
    0
    0

### A 2. példa magyarázata
Nena sajnos nem tud egy inget sem megvenni.
