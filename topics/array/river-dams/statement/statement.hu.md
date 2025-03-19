## Vízerőművek
Új vízerőműveket szeretnénk építeni egy folyóra, amelynek a szélességét megmértük $N$ kijelölt ponton. A kijelölt pontok közül azokon tudunk vízerőművet építeni, ahol a folyó szélessége nagyobb, mint az előző és következő pontnál. Mivel az első pont előtt és az utolsó pont után nincs mérési adatunk, így azok nem jönnek szóba vízerőmű építésére. Hány ponton tudunk vízerőművet építeni?

### Bemenet
A bemenet első sorában egy szám van, a folyón kijelölt pontok száma: $N$.
A második sorban $N$ darab szám van, az egyes pontokon mért szélesség: $W_1, W_2, \ldots, W_N$.

### Kimenet
Egyetlen számot kell kiírnod, a vízerőmű építésére megfelelő helyek számát, azaz az olyan mérési pontok számát, ahol a mért szélesség szigorúan nagyobb, mint az előtte és utána lévő ponton mért szélesség.

### Korlátok
* $1 \le N \le 100$
* $1 \le W_i \le 10\,000$

### Példa bemenet
    5
    5 1 5 1 5

### Példa kimenet
    1

### A példa magyarázata
A harmadik pontnál a folyó szélesebb, mint a második és a negyedik pontnál. Bár az első és az ötödik pontnál is szélesebb, mint mellette, de mivel ezek a szélén vannak, így ezek nem minősülnek jó helynek.
