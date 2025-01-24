## Két Csoportra Osztás
A Csillagflotta Akadémia előtt álló kihívás: $N$ tisztet a korábbi küldetéseken szerzett teljesítménye (pontszáma) alapján két nem üres csoportra kell osztani. Az első csoportban az Elit tisztek lesznek, míg a második csoportba az Alaptisztek.
A csoportokat úgy kell meghatározni, hogy a két csoport közötti teljesítménytávolság, vagyis az Elit csoport leggyengébb tagjának és az Alap csoport legerősebb tagjának pontszámkülönbsége a lehető legnagyobb legyen.
Az Akadémia fő számítógépe, a Starfleet Analytical Core éppen elromlott, így arra kérünk, hogy írj egy algoritmust, amely meghatározza a két csoport közötti maximális teljesítménytávolságot, ezzel segítve a Flotta küldetéseinek sikerességét.

### Bemenet
A bemenet első sorában egyetlen egész szám van: $N$, a tisztek száma.
A második sorban $N$ szám van: $T_0, T_1, \lodts, T_{N-1}$, a tisztek teljesítménypontszáma.

### Kimenet
Egyetlen számot kell kiírnod, a két csoport közötti maximális teljesítménytávolságot.

### Korlátok
* $2 \le N \le 10^5$
* $0 \le T_i \le 10^6$ minden $i$-re.

### Példa bemenet
    8
    15 8 17 22 5 7 25 27

### Példa kimenet
    7

### A példa magyarázata
Ha a két csoport $\{8,5,7\}$ illetve $\{15,17,22,25,27\}$, akkor a különbség 7. Belátható, hogy ennél többet nem lehet elérni.
