## Oszlop csere
A Lázadók Szövetsége elfogta a titkos birodalmi tervrajzokat, amelyeket egy adattáblázatban tároltak. Ez a táblázat $N$ sorból és $M$ oszlopból áll, amelyek mindegyike létfontosságú információkat tartalmaz. Egy birodalmi titkosítási anomália miatt azonban két oszlop felcserélődött, és a lázadóknak vissza kell állítaniuk a helyes sorrendet az adatok elemzéséhez.

A feladatod az, hogy átvedd a lehallgatott $N\,{\times}\,M$ adattáblázatot, majd cseréld ki a két megadott oszlop tartalmát, amelyek indexe $i$ és $j$. Ha a csere megtörtént, küldd el a javított adattáblázatot a lázadók bázisára.

Az Erő (és a hatékony tömbmanipuláció) legyen veled!

### Bemenet
Az első sor két egész számot tartalmaz, $N$ (sorok száma) és $M$ (oszlopok száma).
A következő $N$ sor egyenként $M$ egész számot tartalmaznak, amelyek az adattáblázat étékeit képviselik.
Az utolsó sor két egész számot tartalmaz $i, j$-t, a két felcserélt oszlop indexét.

### Kimenet
Írd ki a javított adattáblát. 

### Korlátok
* $1 \le N, M \le 100$
* $1 \le I < J \le M$
* Az adattábla értékei $0$ és $1000$ között vannak.

### Példa bemenet
    3 4
    11 12 13 14
    21 22 23 24
    31 32 33 34
    1 2    

### Példa kimenet
    12 11 13 14
    22 21 23 24
    32 31 33 34
