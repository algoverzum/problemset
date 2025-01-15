## Aszteroida kérdések
Üdvözlünk a bolygónkon! Szükségünk van a segítségedre!
Már $N$ nap telt el azóta, hogy az aszteroida-zápor elkezdett ránk zúdulni.
Minden nap feljegyeztük az észlelt aszteroidák számát 
$(A_i, i=1, 2, \ldots, N)$.

Mágusunk, Sigissimus azt mondja, hogy meg tudja zavarni az erőt, hogy megállítsa a katasztrófát, de azonnal tudnia kell a választ kétféle kérdésre:

1. Hány aszteroidát észleltek az első $K$ napban összesen?
2. Hány aszteroidát észleltek összesen két adott nap között (beleértve az elejét és a végét is)?

Sigissimus sok kérdést tesz fel, kérlek segíts a válaszok megadásában!

### Bemenet
Az első sorban $N$ és $Q$ - a napok száma és a kérdések száma szerepel. A második sorban N egész szám van $(A_1, A_2, \ldots, A_N)$ - a naponta észlelt aszteroidák száma.

A következő $Q$ sor mindegyike egy-egy kérdést ír le `1 K` vagy `2 L R` formában.
Az első szám a kérdés típusát jelöli, és ettől függően:

* az 1. típus esetében van egy második szám, a kérdésben szereplő $K$ érték,
* a 2. típus esetében van még két szám, $L$ és $R$ - az időszak kezdő és zárónapja.

### Kimenet
$Q$ egész számot kell kiírni, külön sorokban, a kérdésekre adott válaszokat, a bemenettel megegyező sorrendben.

### Korlátok
* $1 \le N \le 100\,000$
* $1 \le Q \le 100\,000$
* $0 \le A_i \le 10\,000$
* $1 \le K \le N$
* $1 \le L \le R \le N$

### Példa bemenet
    5 2
    4 11 0 6 1
    1 3
    2 3 5


### Példa kimenet
    15
    7

### A példa magyarázata
Az első kérdés az aszteroidák teljes számát kérdezi az első 3 napban: 4 + 11 + 0 = 15.
A második kérdésben a 3., 4. és 5. nap aszteroidáinak összegét kell kiszámolnunk: 0 + 6 + 1 = 7.

