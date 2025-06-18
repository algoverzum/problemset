## Központi átjáró

A Galaktikus Köztársaságban $N$ bolygó található, amelyeket $1$-től $N$-ig számoztak meg. Az $1.$ bolygó Coruscant, a Köztársaság fővárosa és politikai központja. Az egyre növekvő szeparatista fenyegetés miatt a Köztársaság új utazási szabályokat vezetett be a biztonság érdekében.

Az új szabályozás szerint a bolygók közötti utazás csak kétféleképpen lehetséges:
1. Közvetlen utazás szomszédos bolygók között (azaz ahol közvetlen út van a két bolygó között)
2. Utazás Coruscanton (az $1.$ bolygón) keresztül, mint központi csomóponton

Ez azt jelenti, hogy ha két bolygó között nincs közvetlen kapcsolat, akkor csak olyan útvonal engedélyezett, amely kizárólag Coruscanton keresztül vezet, és más bolygón nem halad át.

A galaxis közlekedési hálózata **irányított gráffal** van modellezve. Ez azt jelenti, hogy az $A$ bolygóról a $B$ bolygóra vezető út hossza nem feltétlenül egyezik meg a $B$-ről $A$-ra vezető úttal, illetve lehet, hogy csak az egyik irányban létezik út.

A feladatod, hogy kiszámítsd az összes bolygópár között a legrövidebb lehetséges utat a megadott utazási szabályok szerint.

### Bemenet
Az első sor egy egész számot tartalmaz: $N$ ($1 \le N \le 100$) — a bolygók száma.

A következő $N$ sor mindegyike $N$ egész számot tartalmaz. Az $i$-edik sor $j$-edik száma a $i$ bolygóról a $j$ bolygóra vezető közvetlen út hosszát adja meg. Ha nincs közvetlen út $i$ és $j$ között, akkor $-1$ szerepel. Egy bolygóról önmagára vezető út hossza mindig $0$.

### Kimenet
Egy $N \times N$-es mátrixot írj ki ($N$ sor, mindegyikben $N$ szóközzel elválasztott egész szám), ahol az $i$-edik sor $j$-edik eleme az $i$ bolygóról a $j$ bolygóra vezető legrövidebb út hosszát adja meg a szabályok szerint. Ha két bolygó között nem létezik érvényes út, akkor $-1$-et írj ki az adott helyre.

### Korlátok
* $1 \leq N \leq 100$
* Az utak hossza nemnegatív egész vagy $-1$ (ha nincs közvetlen út). ($-1 \leq d \leq 10^6$)
* Egy bolygóról önmagára vezető út hossza mindig $0$.

### Példa bemenet
    4 
    0 2 7 3
    4 0 5 -1
    -1 -1 0 6
    2 -1 -1 0

### Példa kimenet
    0 2 7 3
    4 0 5 7
    -1 -1 0 6
    2 4 9 0

### A példa magyarázata
![](tex/abra.png)

A kimenet egy $N \times N$-es mátrix, ahol az $(i, j)$ elem az $i$ bolygóról a $j$ bolygóra vezető legrövidebb utat tartalmazza, amely lehet közvetlen vagy Coruscanton (az $1.$ bolygón) keresztüli út.

Például:
- Az $1$-es bolygóról a $3$-asra: közvetlen út, hossza $7$
- A $2$-es bolygóról a $4$-esre: nincs közvetlen út, ezért Coruscanton keresztül kell menni: $2 \to 1 \to 4$, összesen $4 + 3 = 7$
- A $3$-as bolygóról a $2$-esre: nincs közvetlen út, és Coruscanton keresztül sem lehet eljutni (mivel $3 \to 1$ nincs), ezért $-1$
- A $4$-es bolygóról a $3$-asra: nincs közvetlen út, ezért Coruscanton keresztül: $4 \to 1 \to 3$, összesen $2 + 7 = 9$

