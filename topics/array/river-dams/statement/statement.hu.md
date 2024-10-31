## River Dams
Új vízerőműveket szeretnénk építeni, mivel megnövekedett az energia felhasználásunk. Már ki is szemeltük, hogy melyik folyóra szeretnénk építeni, de ezen a folyón nem találtuk még meg a tökéletes helyet erre. Tudjuk a folyó egyes szakaszain a víz szélességét és az egyes szakaszok közül szeretnénk kiválasztani a lehetséges helyeket. Egy szakasz akkor megfelelő, ha szélesebb, mint az azt megelőző és az azután következő két szakasz. Mivel az első és az utolsó szakasznak csak egy szomszédja van, így azok nem lehetnek lehetséges helyek. Feladatod az, hogy egy N szakaszból álló folyóból válaszd ki a gátra alkalmas pontokat.

### Bemenet
A bemenet első sorában egy szám van, a szakaszok darabszáma: $N$
A második sorban $N$ darab szám van, az egyes szakaszok szélessége: $A_i$

### Kimenet
Egyetlen számot kell kiírnod, a megfelelő szakaszok darabszáma

### Korlátok
* $1 \le N \le 100$
* $1 \le A_i \le 10000$

### Példa bemenet
    5
    5 1 5 1 5

### Példa kimenet
    1

### A példa magyarázata
A harmadik szakasz szélesebb, mint a második és a negyedik. Bár az első és az ötödik is szélesebb, mint a saját szomszédja, de mivel ezek a szélén vannak, így ezek nem minősülnek jó helynek.
