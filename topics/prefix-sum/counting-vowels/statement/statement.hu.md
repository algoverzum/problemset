## Magánhangzók számlálása
Adott egy $S$ string, amely csak angol kisbetűket tartalmaz.
Továbbá adott $Q$ darab kérdés (intervallum), mindegyik két egész számot tartalmaz: $i$ és $j$ ($1 \leq i \leq j \leq |S|$). Itt $|S|$ az $S$ string hosszát jelöli.

Minden kérdésre meg kell határozni, hogy az $S$ string $i$-edik és $j$-edik karakterei között (beleértve mindkettőt) hány magánhangzó található.

A magánhangzók: a, e, i, o, u.

### Bemenet
Az első sor tartalmazza az $S$ sztringet.

A második sorban egy egész szám van: $Q$, a kérdések száma.

A következő $Q$ sor mindegyike két egész számot tartalmaz: $i$ és $j$ ($1 \leq i \leq j \leq |S|$).

### Kimenet
Minden kérdésre egy-egy sort kell kiírni: az adott intervallumban található magánhangzók számát.

### Korlátok
* $1 \le |S| \le 10^5$
* $S$ angol kisbetűket tartalmaz
* $1 \le Q \le 10^5$
* $1 \leq i \leq j \leq |S|$ minden kérdésre

### Példa bemenet
    abrakadabra
    3
    1 3
    2 5
    5 11

### Példa kimenet
    1
    1
    3

### A példa magyarázata
Az első kérdésre (abr) egy magánhangzó van: a.

A másodikra (brak) egy: a.

A harmadikra (kadabra) három: a, a, a.
