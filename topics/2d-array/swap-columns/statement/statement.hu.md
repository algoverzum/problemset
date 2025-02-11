## Oszlop csere
A Lázadók Szövetsége elfogta a titkos birodalmi tervrajzokat, amelyeket egy adattáblázatban tároltak. Ez a táblázat $N$ sorból és $M$ oszlopból áll, amelyek mindegyike létfontosságú információkat tartalmaz. A sorokat felülről lefelé $1$-től $N$-ig, az oszlopokat balról jobbra $1$-től $M$-ig sorszámozzuk. Egy birodalmi titkosítási anomália miatt azonban két oszlop felcserélődött, és a lázadóknak vissza kell állítaniuk a helyes sorrendet az adatok elemzéséhez.

A feladatod az, hogy átvedd a lehallgatott $N\,{\times}\,M$ adattáblázatot, majd cseréld ki a két megadott oszlop tartalmát, amelyek sorszáma $i$ és $j$. Ha a csere megtörtént, küldd el a javított adattáblázatot a lázadók bázisára.

Az Erő (és a hatékony tömbmanipuláció) legyen veled!

### Bemenet
Az első sor két egész számot tartalmaz: $N$ (sorok száma) és $M$ (oszlopok száma).
A következő $N$ sor egyenként $M$ egész számot tartalmaz, az adattáblázat értékeit.
Az utolsó sorban két egész szám van: $i$ és $j$, a két felcserélt oszlop sorszáma.

### Kimenet
Írd ki a javított adattáblát. 

### Korlátok
* $1 \le N, M \le 100$
* $1 \le i < j \le M$
* Az adattábla értékei $0$ és $1000$ között vannak.

### Példa bemenet
    3 4
    6 7 1 4
    9 3 5 8
    1 5 2 6
    2 3

### Példa kimenet
    6 1 7 4
    9 5 3 8
    1 2 5 6

