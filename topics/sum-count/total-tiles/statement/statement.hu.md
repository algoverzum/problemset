## Járólapok száma
Baltazár király kastélyában $N$ szoba van. Minden szoba négyzet alakú, ráadásul minden helyiség oldalhossza egy egész szám. Baltazár minden szobába új padlólapokat szeretne rakni. Az új lapok négyzet alakúak, oldalhosszuk 1. Hány új lapra lesz szüksége összesen?

### Bemenet
A bemenet első sorában $N$ található - a szobák száma. A következő $N$ sor mindegyike egyetlen számot tartalmaz: $S_i$ - az $i$-edik szoba oldalhosszát ($i =1, 2, \ldots, N$).

### Kimenet
Egyetlen számot írj ki, a szükséges padlólapok számát.

### Korlátozások
* $1 \le N \le 100$
* $1 \le S_i \le 100$

### Példa bemenet
    4
    3
    4
    1
    4

### Példa kimenet
    42

### A példa magyarázata
A 4 szoba oldalhosszai 3, 4, 1, 4. Padlójuk lefedéséhez a Baltazárnak $3 \cdot 3 = 9$, $1 \cdot 1 = 1$, $4 \cdot 4 = 16$, $4 \cdot 4 = 16$ járólapra van szüksége, azaz összesen 42-re.
