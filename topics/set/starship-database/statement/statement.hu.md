## Űrhajó adatbázis
A Csillagflotta megbízott téged, hogy kezeld az adatbázisában a *titkos* csillaghajó lajstromkódokat. A feladatod a Csillagflotta Parancsnokságtól beérkező parancsok kezelése, amelyek a következő három típusba tartoznak:

* $1 x$ - Regisztrálj egy új csillaghajót $x$ lajstromkóddal a Csillagflotta adatbázisában.
* $2 x$ - Egy $x$ lajstromkódú csillaghajó leselejtezése az adatbázisból. (Ha nincs ilyen csillaghajó, a parancsot figyelmen kívül hagyjuk.)
* $3 x$ - Egy csillaghajó létezésének ellenőrzése az adatbázisban. Ha a $x$ lajstromkód megtalálható, **1**, ellenkező esetben **0**.

Az a feladatod, hogy hatékonyan hajtsd végre ezeket a parancsokat, biztosítva, hogy a Csillagflotta adatbázisa pontos és naprakész maradjon. (Kezdetben az adatbázis üres, nincs regisztrált hajó.)

### Bemenet
A bemenet első sora $Q$-t, a végrehajtandó parancsok számát tartalmazza.

A következő $Q$ sor egyenként 1 lekérdezést tartalmaz. Minden lekérdezés két egész számból áll: $y$ és $x$, ahol $y$ a lekérdezés típusa, $x$ pedig a hajó lajstromszáma.

### Kimenet
A 3. típusú lekérdezések esetén **1**-t ír ki, ha az $x$ lajstromszám szerepel az adatbázisban, ha pedig nem szerepel, akkor **0**-t ír ki.
Minden egyes 3. típusú lekérdezést új sorban kell kiírni.

### Korlátok
* $1 \le Q \le 10^5$
* $1 \le y \le 3$
* $1 \le x \le 10^9$

### Példa bemenet
    10
    1 9
    1 6
    1 10
    1 4
    3 6
    3 14
    2 6
    3 6
    1 9
    2 6

### Példa kimenet
    1
    0
    0

### A példa magyarázata
A 6-os hajó az első alkalommal szerepel az adatbázisban, de a második alkalommal már nem. A 14-es hajó soha nem volt regisztrálva az adatbázisban.
