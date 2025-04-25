## Kalózzsákmány
A rettegett űrkalóz, Korg kapitány kifigyelt egy teherhajót, amely titokzatos ládákat szállít a galaxis peremére. Sajnos a hajó rendszereit nem sikerült teljesen feltörnie: csak a rakomány összsúlyát tudta lekérdezni, de azt nem, hogy pontosan milyen ládák vannak a hajó gyomrában.

Ami biztos: a feketepiaci adatbázisból tudja, milyen típusú ládákat szállíthat ez a hajó. Minden ládának ismert az értéke (mennyiért adható el) és a súlya (hány kilót nyom). Egy adott típusú ládából akár több is lehet a rakományban.

Korg kapitány számításba veszi a legrosszabb esetet – azt akarja tudni, hogy a teljes rakomány **legalább mennyit érhet**, ha az ismert ládatípusokból van benne valamilyen kombináció.

### Bemenet
Az első sor két számot tartalmaz $N, S$: a lehetséges ládatípusok száma ($1 \le N \le 500$), és a teherhajó rakományának összsúlya ($1 \le S \le 10\,000$).

Ezután $N$ sor következik. Mindegyik sorban két egész szám van $T_i, W_i$: az $i$-edik ládatípus értéke és súlya (mindkettő maximum $1000$).

### Kimenet
Egyetlen számot kell kiírnod: a legkisebb összértéket, amit a hajó rakománya **biztosan ér**.

### Korlátok
* $1 \le N \le 500$
* $1 \le S \le 10\,000$
* $1 \le T_i, W_i \le 1000$

### Példa bemenet
    4 15
    1 2
    2 3
    5 6
    10 4

### Példa kimenet
    8

### A példa magyarázata
Lehetséges, hogy a rakomány ládáinak súlya rendre $2+2+2+2+2+2+3=15$, és ekkor az értékük $1+1+1+1+1+1+2=8$. Igazolható, hogy ez a lehető legkisebb érték.
