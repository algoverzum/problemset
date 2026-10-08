## Rókatenyészet
Nemes Tihamér OKSZTV 2012. Harmadik forduló.

Egy rókatenyészetben minden róka legfeljebb $L$ évig él.

Minden év végén:
* minden róka egy évvel idősebb lesz,
* az $L$ éves rókák elpusztulnak,
* minden olyan róka, amelynek életkora legalább $K$ év és legfeljebb $L$ év, pontosan egy új utódot hoz világra.

Ismerjük a kezdeti állapotot, vagyis hogy hány 1 éves, 2 éves, \dots, $L$ éves róka van a tenyészetben.

Határozzuk meg, hogy $N$ év elteltével hány róka él!

Mivel az eredmény nagyon nagy lehet, az eredményt $1000000$-val vett maradékként kell kiírni.

### Bemenet
A standard bemenet első sora három egész számot tartalmaz:

* $N$ -- az eltelt évek száma,
* $L$ -- a rókák maximális életkora,
* $K$ -- az első életkor, amikor egy róka szaporodni kezd.

A következő $L$ sor közül az $i$-edik sor egyetlen egész számot tartalmaz: a kezdetben élő $i$ éves rókák számát.

### Kimenet
A kimenet egyetlen egész számot tartalmazzon: az $N$ év után élő rókák számát modulo $1000000$.
Ez azt jelenti, hogy nem a kiszámolt értéket, hanem annak 1000000-re való osztásának a maradékát kell kiírni. Pl. 1000001 helyett 1000001 osztva 1000000-rel maradékát, azaz 1-et kell kiírni!

### Korlátok
* $1 \le N \le 100$
* $1 \le L \le 10$
* $1 \le K \le L$
* $0 \le DB_i \le 100$

### Példa bemenet
    2 5 3
    2
    3
    4
    5
    6

### Példa kimenet
    36

### A példa magyarázata
Kezdetben:

| Életkor | Darabszám |
|---------|-----------|
| 1       | 2         |
| 2       | 3         |
| 3       | 4         |
| 4       | 5         |
| 5       | 6         |

Összesen:

2 + 3 + 4 + 5 + 6 = 20 róka.

Egy év múlva:
- a 3, 4 és 5 éves rókák szaporodnak,
- ezért 4 + 5 + 6 = 15 új róka születik,
- a korábbi 5 éves rókák elpusztulnak,
- minden más róka egy évvel idősebb lesz.

Az állomány:
15, 2, 3, 4, 5

Összesen: 29 róka.

Két év múlva:
12, 15, 2, 3, 4

Összesen: 36 róka.

### Hint 1
Tároljuk külön, hogy hány 1 éves, 2 éves, \dots, L éves rókánk van!

### Hint 2
Minden évben meg kell határozni, hány új róka születik. Mely korcsoportok szaporodnak?

### Hint 3
Gondold végig, mi történik az életkorokkal egy év elteltével!
A 2 évesekből 3 évesek lesznek, a 3 évesekből 4 évesek stb.

### Hint 4
Az L éves rókák a következő évre már nem maradnak életben.

### Hint 5
Az életkorok természetes sorrendje miatt érdemes olyan adatszerkezetet használni, amelynek elejéről törölni és a végére beszúrni is gyorsan lehet.

### Hint 6
A született rókák mindig az 1 éves korcsoportba kerülnek.
