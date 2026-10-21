## Könyvmásolás
Egy könyvtárban $n$ darab könyvet kell digitalizálni. A könyvek adott sorrendben helyezkednek el, ezért a sorrendjük nem változtatható meg.

A munkát $k$ darab másoló végzi. Minden másoló egy összefüggő könyvszakaszt kap, tehát egy könyvet nem lehet több részre bontani, és a könyvek sorrendjét sem lehet megváltoztatni.

Határozzuk meg, hogy legalább mekkora oldalszámot kell egy másolónak maximálisan feldolgoznia ahhoz, hogy az összes könyv lemásolható legyen!

### Bemenet
A standard bemenet első sora két egész számot tartalmaz:

*  $n$ -- a könyvek száma,

*  $k$ -- a másolók száma.

A második sor $n$ darab pozitív egész számot tartalmaz: $a_1,a_2,\dots,a_n$ ahol $a_i$ az $i$-edik könyv oldalszáma.

### Kimenet
A minimális lehetséges értéket kell kiírni, vagyis azt, hogy egy másolónak legfeljebb hány oldalt kell másolnia.

### Korlátok
* $1 \le n \le 100\,000$
* $1 \le k \le n$
* $1 \le a_i \le 10^6$

### Példa bemenet
    5 2
    10 20 30 40 50

### Példa kimenet
    90

### A példa magyarázata
Az optimális felosztás:
10 20 30 | 40 50

Az első másoló 60 oldalt kap.
A második másoló 90 oldalt kap.
A legnagyobb terhelés tehát 90.

Nem létezik olyan felosztás, ahol minden másoló legfeljebb 89 oldalt kapna.

### Hint 1
Tegyük fel, hogy tudjuk a választ! Legyen ez $X$.
Meg tudjuk mondani, hogy az összes könyv kiosztható-e úgy, hogy senki ne kapjon $X$ oldalnál többet?

### Hint 2
Haladjunk balról jobbra. Amíg a következő könyv még belefér az aktuális másoló terhelésébe, adjuk neki. Ha már nem fér bele, új másolót kell indítani. Célszerű megírni egy függvényt, amely eldönti, hogy a könyvek kioszthatók-e legfeljebb k másolónak úgy, hogy senki ne kapjon limit oldalnál többet.

### Hint 3
Ha egy adott $X$ értékkel megoldható a feladat, akkor minden nagyobb értékkel is megoldható.

### Hint 4
A válaszok monotonak: nem nem nem nem igen igen igen igen ...