## Köztársasági csillagtérkép

A galaxisban $N$ bolygó van, ezeket $1$-től $N$-ig számozzuk. Az első $K$ bolygó a Köztársaság irányítása alatt áll, vagyis ezek a Köztársaság bolygói. A többi bolygó nem tartozik a Köztársasághoz.

A bolygók között irányított útvonalak vannak. Ez azt jelenti, hogy lehet út $A$ bolygóról $B$-re, miközben visszafelé nincs, vagy a két irány távolsága különböző.

A feladatod, hogy minden bolygópárra meghatározd a legrövidebb út hosszát úgy, hogy az út közben csak Köztársasághoz tartozó bolygókon szabad áthaladni.

Pontosabban: egy $P_1 \to P_2 \to \dots \to P_q$ út akkor megengedett, ha a közbenső bolygók, vagyis $P_2, P_3, \dots, P_{q-1}$ mind a Köztársasághoz tartoznak. A kezdő- és végpont lehet bármelyik bolygó.

### Bemenet
A bemenet első sora két egész számot tartalmaz: $N$ és $K$ ($1 \le K \le N \le 100$). Itt $N$ a bolygók száma, $K$ pedig a Köztársasághoz tartozó bolygók száma.

A következő $N$ sor mindegyike $N$ egész számot tartalmaz. Az $i$. sor $j$. száma a közvetlen út hosszát adja meg az $i$. bolygóról a $j$. bolygóra. Ha nincs közvetlen út, akkor ez az érték $-1$.

### Kimenet
Írj ki egy $N \times N$ mátrixot. Az $i$. sor $j$. eleme az $i$. bolygóról a $j$. bolygóra vezető legrövidebb megengedett út hossza legyen. Ha nincs ilyen út, akkor az adott helyre $-1$ kerüljön.

### Korlátok
* $1 \le K \le N \le 100$
* A távolságok nemnegatív egész számok vagy $-1$ (ha nincs közvetlen útvonal). ($-1 \leq d \leq 10^6$)
* Egy bolygó önmagától való távolsága mindig $0$.

### Példa bemenet
    5 3
    0 3 -1 1 -1
    -1 0 1 -1 -1
    -1 -1 0 1 -1
    4 1 -1 0 5
    -1 -1 -1 -1 0

### Példa kimenet
    0 3 4 1 -1
    -1 0 1 2 -1
    -1 -1 0 1 -1
    4 1 2 0 5
    -1 -1 -1 -1 0

### A példa magyarázata
![](tex/abra.png)

A kimeneti mátrix minden helyén egy legrövidebb megengedett út hossza szerepel. Itt a közbenső bolygók csak az $1$-től $K$-ig számozott, vagyis a Köztársasághoz tartozó bolygók lehetnek. Ha nincs ilyen út, akkor az érték $-1$. Például:

* Az $1$-es bolygóról a $3$-as bolygóra a legrövidebb megengedett út: $1 \to 2 \to 3$, ennek hossza $4$.  
* A $2$-es bolygóról az $1$-es bolygóra nincs megengedett út, ezért ott $-1$ szerepel.  
* A $2$-es bolygóról a $3$-as bolygóra van közvetlen út, ennek hossza $1$.  
* A $4$-es bolygóról a $3$-as bolygóra a legrövidebb megengedett út: $4 \to 2 \to 3$, ennek hossza $2$.  
* Az $5$-ös bolygóra nem vezet megengedett út, ha közben csak Köztársasági bolygókon haladhatunk át.  
