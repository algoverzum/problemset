## Raktárkészlet Csökkenése
Egy raktárban bizonyos termékből $sz$ darab van készleten.  
A raktárat csak addig lehet üríteni, amíg két feltétel teljesül:

- még van legalább **1 darab** a raktárban,  
- és a vállalat **bevétele** ($ered$) **nagyobb, mint** $N$ **egység**.

Írj egy programot, amely minden lépésben:  
- egy darabbal csökkenti a készletet,  
- kettővel csökkenti az eredményt,  
- és közben **kiírja, mennyi maradt**, külön sorokban!

### Bemenet
A bemenet első sorában egyetlen egész szám van: $sz$ - az aktuális `raktárkészlet`.  
A bemenet második sorában egyetlen egész szám van: $ered$ - az aktuális `eredmény`.  
A bemenet első sorában egyetlen egész szám van: $N$ - a cél értéke.

### Kimenet
Minden sorba azt kell kiírnod, hogy mennyi maradt a termékből.

### Korlátok
* $1 \le sz, ered, N \le 1001$

### Példa bemenet
    5
    100
    50

### Példa kimenet
    4
    3
    2
    1
    0

### A példa magyarázata
Kezdetben $5$ volt, aztán $4$, a végén $0$.
