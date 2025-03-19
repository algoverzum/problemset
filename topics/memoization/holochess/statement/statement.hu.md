## Holosakk
Miután Dejarik holosakkozott Chewbacca és R2-D2, úgy döntöttek, hogy egy egyszerűbb játékot játszanak a $100 \times 100$-as táblán. A játék szabályai a következők:

A játék úgy kezdődik, hogy egyetlen érme van az $(x,y)$ koordinátájú mezőn. A bal felső mező koordinátái $(1,1)$.

A játékosnak minden egyes lépésben az érmét az $(x,y)$ celláról a következő helyek egyikére kell áthelyeznie:

* $(x-2,y+1)$
* $(x-2,y-1)$
* $(x+1,y-2)$
* $(x-1,y-2)$

Megjegyzés: Az érmének a táblán belül kell maradnia!

Az alábbi ábra mind a négy lehetséges lépést mutatja:

![példa](tex/abra.pdf)

Az 1. játékos kezd. Utána a játékosok felváltva lépkednek. Az a játékos, aki nem tud lépni, elveszíti a játékot.

R2-D2-nak tesztelnie kell a kvantumprocesszorát. Az érme kezdeti koordinátái alapján, feltételezve, hogy mindketten optimálisan játszanak, határozzuk meg, hogy melyik játékos nyeri a játékot!

### Bemenet
A bemenet első sorában $T$, a tesztesetek száma szerepel.

A következő $T$ sor mindegyike 2 szóközzel elválasztott egész számot tartalmaz: $x_i$ és $y_i$, az érme kezdőpozíciója.

### Kimenet
Minden egyes tesztesethez egy sort írj ki. Ha az első játékos a győztes, írd ki, hogy "First". Ellenkező esetben írd ki, hogy "Second".

### Korlátok
* $1 \le T, x_i, y_i \le 100$

### Példa bemenet
    3
    2 5
    3 5
    8 8

### Példa kimenet
    Second
    First
    First

### A példa magyarázata
Az első esetben az 1. játékos bármelyik kék pozícióba léphet. Függetlenül attól, hogy melyiket választja, a 2. játékosé az utolsó lépés, és megnyeri a játékot (lásd alább).

![példa](tex/example25.pdf)

A második esetben az 1. játékosnak 4 lehetséges lépése van. Ha az $(1,6)$-ra lép, akkor a 2. játékos kénytelen a $(2,4)$-re lépni. Innen az 1. játékos $(1,2)$-re lép és nyer (lásd alább).

![példa](tex/example35.pdf)
