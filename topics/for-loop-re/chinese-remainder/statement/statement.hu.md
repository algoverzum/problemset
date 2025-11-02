## Titkos kód
Egy legfeljebb 4 jegyű titkos számkódot szeretnénk megfejteni, a kód pozitív egész szám. Az tudjuk csak róla, hogy mennyi az 5-tel ($A$), a 7-tel ($B$), illetve a 11-gyel ($C$) osztásának maradéka.

Írj programot, amely beolvassa $A$ és $B$ és $C$ értékét, majd megadja a legkisebb olyan pozitív számkódot, ami a maradékok alapján lehetséges.

Ha nincs ilyen szám, akkor -1 legyen a kiírt szám.

### Bemenet
A bemenet első sorában egyetlen egész szám van: $A$, a titkos kód 5-ös maradéka.

A bemenet második sorában egyetlen egész szám van: $B$, a titkos kód 7-es maradéka.

A bemenet harmadik sorában egyetlen egész szám van: $C$, a titkos kód 11-es maradéka.

### Kimenet
Írd ki a legkisebb olyan számkódot, ami a maradékok alapján lehetséges, különben -1-et.

### Korlátok
* $0 \le A \le 4$
* $0 \le B \le 6$
* $0 \le C \le 10$

### 1. Példa bemenet
    3
    4
    0

### 1. Példa magyarázat
88 % 5 = 3, mert $88 = 17\cdot 5 + 3$.
88 % 7 = 4, mert $88 = 12\cdot 7 + 4$.
88 % 11 = 0, mert $88 = 8\cdot 11 + 0$.
Igazolható, hogy ez a legkisebb pozitív megoldás.

### 1. Példa kimenet
    88

### 2. Példa bemenet
    2
    1
    1

### 2. Példa kimenet
    232   

### 3. Példa bemenet
    1
    5
    2

### 3. Példa kimenet
    376
