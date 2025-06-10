## Hegymászás
Képzeld el, hogy egy felfedező vagy egy olyan bolygón, ahol a hegyek úgy néznek ki, mintha mesterségesen, hatalmas kockákból épültek volna! A terepet egy négyzet alakú rács ábrázolja. A rács minden cellája egy számot tartalmaz, amely az adott helyen található kockák oszlopának magasságát jelöli.

A küldetésed az, hogy megtaláld a lehető leghosszabb mászási útvonalat a következő szabályok betartásával:

* Kezdőpont: A mászásnak a rács szélén kell kezdődnie, azaz az első sorban, az utolsó sorban, az első oszlopban vagy az utolsó oszlopban.
* Mozgás: Minden lépésben egy szomszédos cellába léphetsz (fel, le, balra vagy jobbra). Átlós mozgás nem megengedett.
* Emelkedés szabálya: Csak akkor léphetsz egy szomszédos cellába, ha annak a magassága pontosan eggyel nagyobb, mint a jelenlegi celláé (például egy $H$ magasságú oszlopról csak egy $H+1$ magasságú szomszédba mehetsz).
* Az út vége: Az emelkedést addig kell folytatni, ameddig csak lehet. Az adott út véget ér, ha olyan cellába jutsz, ahonnan az emelkedés szabálya szerint már nem lehet továbbmenni.

Feladat: Írj egy programot, amely meghatározza, hogy egy felfedező egyetlen mászás során maximum hány lépést tehet meg, és ehhez hol kezdje a mászást! Az összes fenti szabályt be kell tartania. Ha nincs ilyen érvényes útvonal, akkor az eredmény 0 lépés (és bárhol kezdheti a szélén).

### Bemenet
Az első sor egyetlen egész számot tartalmaz: $N$ — a rács méretét.  
A következő $N$ sor mindegyike $N$ egész számot tartalmaz — a cellák magasságértékeit. A $i$. sor és $j$. oszlop metszetében lévő cella magassága $A_{i,j}$.  

### Kimenet
A kimenet két sorból áll:

* Az első sor egyetlen egész számot tartalmaz: a leghosszabb lehetséges út hosszát.
* A második sor két egész számot tartalmaz: a leghosszabb expedíció kezdőpontjának sor- és oszlopszámát.

Ha több érvényes kezdőpont is létezik, bármelyik megadható.

### Korlátok
* $1 \le N \le 500$
* $1 \le A_{i,j} \le 10^6$ minden $1 \le i,j \le N$ esetén

### Példa bemenet
    6
    5 1 6 1 5 4
    4 2 5 2 3 5
    3 3 4 9 4 5
    2 4 3 4 4 6
    1 5 4 5 5 4
    2 3 5 9 6 5

### Példa kimenet
    5
    1 2

### A példa magyarázata
Az első sor második és negyedik celláiból kiindulva egy $1\to 2\to 3\to 4\to 5\to 6$ útvonal járható be.
