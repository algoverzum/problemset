## Legnagyobb közös osztó
Írj programot, amely meghatározza két egész szám legnagyobb közös osztóját! Az alábbi megoldás, az ún.~euklideszi algoritmuson alapszik. Bizonyítható, hogy ha $a = q\cdot b+r$ akkor $(a,b) = (r,b)$, miközben $r<b$ **is teljesül**. Ekkor folytatjuk $(r,b)$ meghatározásával, hasonlóképpen: $(b,r)=(r,r_1)$.
(Így az is igaz, hogy $(a,b)=(r=r1)$!) Az új maradék $r_1$, amellyel tovább folytatjuk az algoritmust. A végén a maradék 0 lesz: $r_n = 0$. Ekkor $(a,b)=(r_{n-1}, 0)$. Mivel $(x,0)=x$, (hiszen 0-nak minden szám osztója), ezért $(a,b) = r_{n-1}$. Azt kaptuk tehát, hogy az lnko-t **az utolsó, nem 0 maradék** szolgáltatja.

### Bemenet
A bemenet első sorában egy egész szám van: $a$.
A bemenet második sorában egy egész szám van: $b$.

### Kimenet
Egyetlen számot kell kiírnod, a két szám legnagyobb közös osztóját.

### Korlátok
* $1 \le b \le a \le 10^9$

### 1. példa bemenet
    120
    21

### 2. példa kimenet
    3

### Az 1. példa magyarázata
$120=5\cdot 21+15$ tehát $(120,21)=(21,15)$, $21=1\cdot 15+6$ tehát $(120,21)=(15,6)$. $15=2\cdot 6+3$ tehát $(120,21)=(6,3)$. $6=2\cdot 3+0$ tehát $(120,21)=(3,0)$. Az utolsó nem 0 maradék 3, azaz: $(120,21)=3$.

Akár a legkisebb többszörös is megkapható ezután: $\frac{a\cdot b}{(a,b)}$.

### 2. példa bemenet
    340
    27

### 2. példa kimenet
    1
