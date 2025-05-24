## Útvonaltervező
A Millennium Falcon a Tatooine-ról indul, és különböző bolygók között mozoghat adott útvonalakon keresztül. A bolygókat $1$-től $N$-ig számozzuk, a Tatooine az $1$-es. Minden útvonalhoz tartozik egy költség, mely az úrhajó üzemanyag fogyasztásából ered. Néhány útvonalat azonban a Lázadók Szövetsége támogat, így ezek negatív költségűek is lehetnek. Például egy útvonal mehet a Naboo-ról a Kamino-ra, aminek a költsége $5$. Előfordulhat, hogy visszafelé nem lehet menni. Az is lehet, hogy a visszafelé útvonal is elérhető, ám annak költsége más, pl. $-2$.

Írj programot, amely kiszámítja a Millennium Falcon számára a legkisebb összköltségű utakat a Tatooine-ról kiindulva az összes bolygó esetén! Az útvonalak gráfja negatív költségű irányított kört nem tartalmaz.

### Bemenet
A bemenet első sorában két szám található: $N$ és $M$, a bolygók száma és a lehetséges útvonalak száma.

A következő $M$ sor az útvonalakat írja le, a $k$-adik sor három számot tartalmaz: $U_k, V_k, W_k$, ahol $U_k$ az induló bolygó sorszáma, $V_k$ a célállomás sorszáma, és $W_k$ az útvonal költsége (lehet negatív is).

### Kimenet
A program $N$ szóközzel elválasztott értéket írjon ki. A $j$-edik szám megadja, hogy a $j$-edik bolygó elérésének mi a minimális költsége. Ha nem lehet elérni így a $j$-edik bolygóra, akkor írj ki egy nagy `X` betűt.

### Korlátok
* $2 \le N \le 1000$
* $0 \le M \le 2000$
* $1 \le U_k \not= V_k \le N$ minden $k=1,2,\ldots,M$ esetén
* $-10^6 \le W_k \le 10^6$ minden $k=1,2,\ldots,M$ esetén

### Példa bemenet
    6 7
    1 2 3
    2 3 -1
    3 5 4
    3 4 2
    4 2 2
    5 4 -3
    6 5 -5

### Példa kimenet
    0 3 2 3 6 X

### A példa magyarázata
A példához tartozó gráf:

![](tex/abra.png)

Például a 4. bolygóra több úton is eljuthatunk, de a legkisebb költségű út: $1\to 2\to 3\to 5\to 4$.
