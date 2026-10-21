## Vízellátás
Egy nemzetközi segélyszervezet $N$ darab falu vízellátását szeretné biztosítani egy hosszú, egyennes út mentén. A falvak koordinátáit az út elejétől mérve az $a_1, a_2, \ldots, a_N$ egész számok határozzák meg.

A szervezet kapott a kormánytól legfeljebb $K$ darab speciális víztisztító állomást. Minden egyes állomást az út egy tetszőleges pontjára lehet telepíteni (nem feltétlenül falu helyére). Egy állomásnak van egy $R$ hatósugara: ha egy állomást egy $X$ koordinátájú pontra telepítünk, akkor az összes olyan falut képes ellátni tiszta vízzel, amelynek a koordinátája a $[X - R, X + R]$ zárt intervallumba esik.

Mivel a költségvetés korlátos, a szervezet szeretné minimalizálni a beszerzendő állomások $R$ hatósugarát. Ugyanakkor az összes falu vízellátását biztosítani kell.

**Feladat:** Határozzuk meg a legkisebb olyan egész $R$ hatósugarat, amellyel legfeljebb $K$ darab állomás felhasználásával minden falu vízellátása biztosítható!

### Bemenet
* Az első sorban két egész szám: $N$ és $K$ ($1 \le K \le N \le 10^5$)
* A második sorban $N$ darab egész szám növekvő sorrendben: $a_1, a_2, \ldots, a_N$ ($1 \le a_i \le 10^9$), a falvak koordinátái.

### Kimenet
Egyetlen egész szám: a minimális lehetséges egész $R$ hatósugár.

### Korlátok
* $1 \le K \le N \le 10^5$
* $1 \le a_1 < a_2 < \ldots < a_N \le 10^9$

### Példa bemenet
    5 2
    1 4 7 9 15

### Példa kimenet
    3

### A példa magyarázata
Ha a hatósugár $R = 3$, akkor egy állomás maximális átfogása $2R = 6$ távolság lehet.
1. Az első állomást telepítsük a $4$-es koordinátára (ami egy falu). Ennek hatóköre $[4-3, 4+3] = [1, 7]$. Ez ellátja az $1, 4, 7$ koordinátájú falvakat.
2. A második állomást telepítsük a $12$-es koordinátára (ahol nincs falu). Ennek hatóköre $[12-3, 12+3] = [9, 15]$. Ez tökéletesen ellátja a megmaradt $9$ és $15$ koordinátájú falvakat.

Mivel $2$ állomással lefedtük az összes falut, az $R=3$ egy lehetséges megoldás. Kisebb egész sugárral ($R=2$) nem lehetne lefedni az összes falut $2$ állomással, így a minimális hatósugár $3$.

### Hint 1
Ha minden falu ellátható K darab R hatósugarú állomással, akkor bármely $R' > R$ hatósugárral is biztosan elláthatóak. Ha viszont egy $R$ hatósugár túl kicsi, akkor annál kisebbel sem fog sikerülni. Ezért a minimális $R$-re binárisan kereshetünk.

### Hint 2
Ha egy állomás hatósugara $R$, akkor az állomástól balra és jobbra is legfeljebb R távolságra lévő falvakat tudja ellátni. Ez azt jelenti, hogy egyetlen állomással lefedett legszélső falvak (a legbaloldalibb \(a_{l}\) és a legjobboldalibb \(a_{r}\)) közötti távolság legfeljebb 2R lehet (\(a_r - a_l \le 2R\)). Ha ez teljesül, mindig létezik olyan falu a kettő között (vagy maga az egyik végpont), ahová az állomást letéve mindkettőt (és a köztük lévőket is) eléri.

### Hint 3
Induljunk el a legelső (legbaloldalibb) ellátatlan falutól (\(a_{l}\)). Keressük meg azt a legtávolabbi \(a_{r}\) falut, amire még igaz, hogy \(a_r - a_l \le 2R\). Ekkor az \([l, r]\) intervallum falvait egyetlen állomással lefedhetjük. Ezután a következő állomást a még lefedetlen, soron következő első falutól indítjuk, és ezt ismételjük.

### Hint 4
A hatósugár legkisebb értéke 0 lehet (ha $K \ge N$). A maximális értéke pedig a legelső és legutolsó falu távolságának a fele (\(a_N - a_1\)).
