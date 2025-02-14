## Jobb űrhajó
Űrhajó modellek tulajdonságait értékeljük egészszámokkal, mivel szeretnénk megtalálni azokat, amik feleslegesek. Írj egy olyan programot, amely megtalálja, hogy melyik az az űrhajó, amelynek értékelései minden szempontból **jobbak**, mint egy másik-é.

### Bemenet
A bemenet első sorában kettő egész szám van, az űrhajók száma és az értékelési szempontok száma: $N$ és $M$.
A következő $N$ sorban $M$ darab egész szám van, az $i$-edik űrhajó $j$-edik kategóriában kapott értékelése: $S_{i,j}$.

### Kimenet
Egyetlen számot kell kiírnod, annak az űrhajónak a sorszámát, aminek minden értékelése jobb, mint egy másiké. Ha több ilyen van, akkor a legkisebb sorszámot írd ki, ha pedig egy sincs, akkor pedig -1-et.

### Korlátok
* $1 \le N,M \le 100$
* $1 \le S_{i,j} \le 1000$

### Példa bemenet
    3 5
    10 15 12 10 10
    11 11 11 11 20
    12 16 16 16 20

### Példa kimenet
    3

### A példa magyarázata
A harmadik űrhajó tulajdonságai jobbak, mint az első űrhajóé (de nem jobb a másodiknál).
