## Ereszkedés
Egy repülő ereszkedése közben fontos értéke a gép **sebessége** ($S$) és a **magassága** ($M$).  
Írj programot, amely:

- beolvassa a gép aktuális sebességét és magasságát,  
- minden lépésben **10-zel csökkenti a sebességet**,  
  és **2-vel csökkenti a magasságot**,  
- amíg a repülő **nem landol**.

A repülő **landol**, ha:  
- a magassága 0, **vagy**  
- a sebessége **nem nagyobb, mint 1**.

A programod írja ki minden lépésben az aktuális értékeket, **beleértve a kezdeti adatokat is!**

### Bemenet
A bemenet első sorában egy szám van, a gép **sebessége** $S$.  
A bemenet második sorában egy egész szám van, a gép **magassága** $M$.

### Kimenet
A kimenet minden sorában az aktuális értékek vannak, **beleértve a kezdeti adatokat is!** 

### Korlátok
* $1 \le S, M \le 1001$

### Példa bemenet
    42
    10

### Példa kimenet
    42 10
    32 8
    22 6
    12 4
    2 2

### A példa magyarázata
A sebesség $10$-zel csökken, a magasság $2$-vel, így lesz a végén $2$ és $2$.
