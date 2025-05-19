## Holo-Torony
A Millennium Falcon fedélzetén R2-D2 és C-3PO egy futurisztikus toronyépítő játékot játszanak, a **Holo-tornyot**.

* mindig R2-D2 kezdi a játékot.
* Minden körben egy droid **4, 5 vagy 11 holo-kockát** helyezhet a torony tetejére (4, 5 vagy 11 kockával növeli a torony magasságát).
* Az a droid, aki a torony magasságát **$N$ fölé emeli, elveszíti a játékot**. Pontosan $N$-ig elérni még szabályos.

Mindkét droid tökéletes logikával játszik — mindig a lehető legjobb lépést választják. A megadott maximális toronymagasság ($N$) alapján döntsd el, ki nyeri a játékot!

### Bemenet
Az első sorban egy egész szám található, $T$, a lejátszott játékok száma.
A következő $T$ sor mindegyikében egy egész szám szerepel: $N_i$ — az adott játékban megengedett maximális toronymagasság.

### Kimenet
Minden játékhoz egy sort írj ki, melynek tartalma:

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

$N=14$: 
- R2-D2 lerak 5 holo-kockát (magasság = 5)
- C-3PO nem tud 11 kockát lerakni (meghaladná a 14-et), így 4 vagy 5 kockát kell leraknia
- Ha C-3PO 4 kockát rak le, a magasság 9 lesz, és R2-D2 lerakhat 5 kockát, hogy pontosan 14-et érjen el és nyerjen
- Ha C-3PO 5 kockát rak le, a magasság 10 lesz, és R2-D2 lerakhat 4 kockát, hogy pontosan 14-et érjen el és nyerjen
