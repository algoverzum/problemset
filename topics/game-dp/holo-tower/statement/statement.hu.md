## Holo-Torony
A Millennium Falcon fedélzetén R2-D2 és C-3PO egy futurisztikus toronyépítő játékot játszanak, a **Holo-tornyot**.

* R2-D2 mindig ő kezdi a játékot.
* Minden körben egy droid **4, 5 vagy 11 holo-kockát** helyezhet a torony tetejére (ennyivel növeli a torony magasságát 4, 5 vagy 11 kockával).
* Az a droid, aki a torony magasságát **$N$ fölé emeli, elveszíti a játékot**. Pontosan $N$-ig elérni még szabályos.

Mindkét droid tökéletes logikával játszik — mindig a lehető legjobb lépést választják. A megadott maximális toronymagasság ($N$) alapján döntsd el, ki nyeri a játékot!

### Bemenet
Az első sorban egy egész szám, $T$, a lejátszott játékok száma.
A következő $T$ sor mindegyikében egy egész szám szerepel: $N_i$ — az adott játékban megengedett maximális toronymagasság.

### Kimenet
Minden játékra külön sorba írd ki:

* "R2-D2", ha R2-D2 nyeri a játékot
* "C-3PO", ha C-3PO nyeri a játékot

### Korlátok
* $1 \le T \le 10$
* $1 \le N_i \le 10^5$ minden $i=1,\ldots,T$ esetén

### Példa bemenet
    5
    2
    5
    14
    20
    33

### Példa kimenet
    C-3PO
    R2-D2
    R2-D2
    R2-D2
    C-3PO

### A példa magyarázata
$N=2$: az első játékos bármelyik lépése már túl magasra emeli a tornyot — veszít.

$N=5$: az első játékos lerakhat 4 vagy 5 holo-kockát, és ezzel megnyeri a játékot.

$N=14$: az első játékos lerak 5 holo-kockát. A második nem tud 11-et rakni, csak 4 vagy 5-öt. Ezután az első ismét tud úgy lépni, hogy megnyerje a játékot.
