## Kiegyensúlyozás
Han Solo és Chewbacca azt a megbízást kapták Jabbától, hogy rakjanak fel konténereket a Millennium Falconra úgy, hogy a bal és jobb oldali raktér összsúlyának különbsége a lehető legkisebb legyen. Minden konténer előre megadott súlyú (kg-ban).

### Bemenet
A bemenet első sora tartalmazza a konténerek számát $N$-et, ahol $2 \le N \le 100$.

A második sorban $N$ egész szám szerepel, amelyek a konténerek súlyát adják meg kilogrammban (mindegyik $1$ és $100$ közötti érték).

### Kimenet
Az első sorban a két raktér összsúlya közötti legkisebb különbséget kell kiírni.

A második sorban a bal oldali raktérbe pakolt konténerek darabszámát, majd az eredeti listában szereplő sorszámaikat kell felsorolni.

A harmadik sorban a jobb oldali raktérbe került konténerek darabszámát, majd sorszámaikat.

Ha több optimális megoldás is létezik, akkor bármelyik megadható.

### Korlátok
* $2 \le N \le 100$
* $1 \le W_i \le 100$, ahol $W_i$ az $i$-edik konténer súlya ($i = 1, 2, \ldots, N$)

### Példa bemenet
    5
    10 20 15 5 25

### Példa kimenet
    5
    3 1 4 5
    2 2 3

### A példa magyarázata
A bal raktérbe került az 1., 4. és 5. konténer, ezek összsúlya $10+5+25=40$.
A jobb raktérbe került a 2. és 3. konténer, ezek összsúlya $20+15=35$.
A különbség $|40-35|=5$, ami minimális.
