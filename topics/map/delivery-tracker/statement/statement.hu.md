## Csomagszállítás
A Galaktikus Postaszolgálat a Tatuinon kézbesíti a csomagokat. A bolygó felszínét földrajzi koordinátákhoz hasonló módon adják meg: szélesség és hosszúság értékekkel.

Minden kézbesítés során feljegyzik:

* a célpont szélességi koordinátáját ($X_i$)
* a hosszúsági koordinátáját ($Y_i$),
* és a kézbesített csomagok számát ($P_i$).

Több kézbesítés is történhet ugyanarra a helyre. A feladat: meghatározni azt a helyet Tatuin felszínén, ahová a legtöbb csomagot vitték ki összesen.

### Bemenet
A bemenetben első sorában egyetlen egész szám van: $N$ - a kiszállított csomagok száma.
Ezt $N$ sor követi, az $i$-edik sorban három számmal $X_i, Y_i, P_i$, ahol $X_i$ és $Y_i$ a kiszállítás koordinátái (egész számok), illetve $P_i$ a csomagok száma.

### Kimenet
Három számot kell kiírnod egy sorban ($X, Y, P$): a koordinátáit annak a helynek ahova a legtöbb csomagot kiszállították és az oda összesen kiszállított csomagok számát.
Ha több pont is ugyanennyi csomagot kapott, bármelyik közülük kiírható.

### Korlátok
* $1 \le N \le 10^5$
* $-10^9 \le X_i, Y_i \le 10^9$ minden $i=1,\ldots,N$-re.
* $1 \le P_i \le 10^9$ minden $i=1,\ldots,N$-re.

### Példa bemenet
    5
    2 3 5
    1 4 2
    2 3 4
    0 0 1
    1 4 1

### Példa kimenet
    2 3 9

### A példa magyarázata
A $(2,3)$ koordinátájú helyre összesen $4+5=9$ csomagot szállítottak ki. Minden más helyre ennél kevesebbet.
