## Táblázat szorzás
A Jedi Archívum harci stratégiai táblázatokat tárol, hogy a Köztársaság megtervezhesse a védelmét. Minden tábláyat $N$ sorból és $M$ oszlopból áll, amelyek taktikai értékeket képviselnek.

A feladatod az, hogy egy adott táblázatot úgy erősítsd fel, hogy minden egyes értéket megszorozol egy $C$ erő-erősítő faktorral.

### Bemenet
Az első sor két egész számot tartalmaz, $N$ (sorok száma) és $M$ (oszlopok száma).
A következő $N$ sor egyenként $M$ egész számot tartalmaznak, amelyek a táblázat értékeit képviselik.
Az utolsó sor egy egész számot tartalmaz $C$-t, az erő-erősítő tényezőt.

### Kimenet
Írd ki a $C$-vel megszorzott táblázatot.

### Korlátok
* $1 \le N, M \le 10$
* $-100 \le C \le 100$
* a táblázat értékei is $-100$ és $100$ között vannak.

### Példa bemenet
    3 4
    11 12 13 14
    21 22 23 24
    31 32 33 34
    2

### Példa kimenet
    22 24 26 28
    42 44 46 48
    62 64 66 68
