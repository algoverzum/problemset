## Verseny helyezések
A Galaktikus Verseny Archívum egy óriási adatbázist tartalmaz, amely a galaxison belüli versenyek eredményeit tárolja. A legendás "Nebulon Futam" legutóbbi eredményeit éppen most digitalizálták, és a Galaktikus Kutatók Szövetsége arra kérte a fejlesztő csapatot, hogy egy olyan programot készítsenek, amely segít gyorsan lekérdezni a futam eredményeit. A te feladatod egy program írása ami megadja, hogy a kérdezett versenyzők az archívum, hányadik helyén szerepelnek. Ha az archívum nem tartalmazza, akkor pedig írj ki -1-et.

### Bemenet
A bemenetben első sorában két egész szám van: $N$ az adatbázis hossza és $M$ a kérdések száma.
A második sorban $N$ string van szóközzel elválasztva. Minden string az angol ábécé kisbetűiből áll és maximum 1000 karakter hosszú
A Harmadik sorban $M$ string van szóközzel elválasztva. Minden string az angol ábécé kisbetűiből áll és maximum 1000 karakter hosszú

### Kimenet
$M$ számot kell kiírnod, ha a kérdezett szó szerepel az adatbázisban akkor azt, hogy hanyadikként. ha nem akkor -1-et.

### Korlátok
* $1 \le N \le 1000$
* $1 \le M \le 1000$

### Példa bemenet
    5 4
    nova odyssey phoenix voyager aurora
    nebula nova aurora phoenix

### Példa kimenet
    -1 1 5 3

### A példa magyarázata
nebula nem szerepel
nova első helyen van
aurora ötödik helyen van
phoenix harmadik helyen van
