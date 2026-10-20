## Egyenletes Pakolás
Egy raktárból konténereket kell elszállítani kamionokkal. A konténerek egy sorban egymás után helyezkednek el. Minden konténer súlyát ismerjük, ezek sorrendben $s_1, s_2, \dots, s_N$.

Összesen $K$ kamion használható a szállításra. Minden kamionra csak a sorban **egymást követő** konténerek pakolhatók. Azt szeretnék elérni, hogy a lehető legegyenletesebb legyen a kamionok terhelése, ami azt jelenti, hogy a **maximálisan terhelt kamion terhelése a lehető legkisebb legyen**.

A kamionok súlykapacitása legalább akkora, hogy mindegyik biztosan elbírja a rárakandó konténerek súlyát. Kikötés továbbá, hogy **minden kamionra legalább egy konténert kell rakni**.

Írj programot, amely kiszámít egy legegyenletesebb pakolást!

### Bemenet
A standard bemenet első sorában két egész szám van:

* $N$ a konténerek száma $(500 \le N \le 3000)$,
* $K$ a kamionok száma $(4 \le K \le N)$.

A második sor pontosan $N$ pozitív egész számot tartalmaz, a konténerek súlyait. Az $i$-edik szám az $i$-edik konténer súlya, ami nem nagyobb, mint $10\,000$.

### Kimenet
A standard kimenet első sorába a legegyenletesebb terhelésre vonatkozó **maximálisan terhelt kamion terhelését** kell írni!

A második sor pontosan $K$ számot tartalmazzon (egy-egy szóközzel elválasztva). Az $i$-edik szám annak a konténernek a sorszáma legyen, amelyiktől kezdődő konténereket az $i$-edik kamionra kell pakolni. Több megoldás esetén bármelyik megadható.

### Korlátok

* Időkorlát: 0,2 másodperc
* Memóriakorlát: 256 MiB
* $500 \le N \le 3000$
* $4 \le K \le N$
* $1 \le s_i \le 10\,000$

### Példa bemenet
    12 4
    4 6 1 5 1 4 4 1 4 2 7 3

### Példa kimenet
    11
    1 4 7 11

### A példa magyarázata
A konténerek súlyai:

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

|--------|---|---|---|---|---|---|---|---|---|----|----|----|

| Súly | 4 | 6 | 1 | 5 | 1 | 4 | 4 | 1 | 4 | 2 | 7 | 3 |

A kimenet szerint a kamionok a következő konténerektől kezdenek: **1, 4, 7, 11**. Tehát a pakolás:
- **1. kamion:** 1–3. konténer → súlyok: 4 + 6 + 1 = 11
- **2. kamion:** 4–6. konténer → súlyok: 5 + 1 + 4 = 10
- **3. kamion:** 7–10. konténer → súlyok: 4 + 1 + 4 + 2 = 11
- **4. kamion:** 11–12. konténer → súlyok: 7 + 3 = 10

A maximális terhelés:

$$

\max(11, 10, 11, 10) = 11

$$

ami a kimenet első sora.

A kezdő indexek:

**1, 4, 7, 11**

ezek szerepelnek a második sorban.

### Hint 1

Ez a probléma a klasszikus **"minimális maximum részösszeg"** (minimax partitioning) probléma. Adott N számot K darab csoportra kell osztanunk (egymást követő elemekből), hogy a csoportösszegek maximuma minimális legyen. A megoldás: **paraméteres keresés** (bináris keresés) a maximális terhelésre.

### Hint 2

A bináris keresés alsó határa a legnagyobb egyedi konténer súlya (mert egy kamion legalább egy konténert visz). A felső határa az összes konténer összsúlya (ha mindet egy kamion vinné).

A bináris keresés minden lépésében egy **eldöntési függvényt** (predikátumot) kell meghívnunk, ami megmondja, hogy egy adott $X$ maximális terhelés mellett be lehet-e osztani a konténereket legfeljebb $K$ kamionba.

### Hint 3

Az eldöntési függvény **mohó**: haladjunk balról jobbra, és pakoljuk a konténereket az aktuális kamionba, amíg az összsúly nem haladja meg $X$-et. Ha túllépnénk, indítsunk új kamiont. A végén megnézzük, hogy a felhasznált kamionok száma $\le K$-e.

Ha a mohó $K$-nál több kamiont használ, akkor $X$ túl kicsi (növelni kell). Ha $K$-nál nem többet, akkor $X$ jó (lehet csökkenteni).

### Hint 4

A második kimeneti sor (a kezdő indexek) előállításához a bináris keresés után, a megtalált optimális $X$ értékkel újra le kell futtatnunk a mohó algoritmust, és közben elmenteni az egyes kamionok kezdő indexeit.
