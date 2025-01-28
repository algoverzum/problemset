## Kristályok gyűjtése
Egy $N$ sorból és $M$ oszlopból álló, feltérképezetlen bolygófelszín rácstérképén minden mező vagy egy veszélyes csapdát, vagy értékes energiakristályokat tartalmaz. Egy Csillagflotta tiszt feladata, hogy a rácson keresztülhaladjon, a bal felső sarokból indulva elérje a jobb alsó sarkot, miközben a lehető legtöbb kristályt gyűjti össze. A küldetés szabályai a következők:

-   Csapda mezőre nem lehet lépni, mert az a tiszt életét veszélyezteti.

-   A tiszt minden lépésben csak jobbra vagy lefelé mozoghat.

-   A tiszt összeszedi az energiakristályokat az olyan mezőkről, amelyre rálép.

A küldetés célja: készíts egy programot, amely kiszámítja, hogy a Csillagflotta tisztje legfeljebb hány energiakristályt tud összegyűjteni, és megadja az optimális útvonalat, amely a legtöbb kristályt eredményezi.
Ha a csapdák miatt nem lehet eljutni a jobb alsó sarokba, akkor $-1$-et kell kiírni.
Ha több optimális útvonal is van, akkor bármelyik megadható.

### Bemenet
A bemenet első sora két szóközzel elválasztott egész számot tartalmaz, $N$-et és $M$-et, a rácstérkép sorainak és oszlopainak a számát.

További $N$ sor következik, melyek mindegyike $M$ darab számot tartalmaz, a térkép celláin lévő energiakristályok számát, illetve $-1$-et ha ott csapda van. Az $i$-edik sor $j$-edik száma $A_{i,j}$.

### Kimenet
A kimenet első sorába egyetlen számot kell írnod, a megszerezhető energiakristályok maximális számát. Ha nem lehet eljutni a jobb alsó sarokba, akkor írj ki $-1$-et.

Ha el lehet jutni a jobb alsó sarokba, akkor a kimenet második sorában add meg az oda vezető utat. Az utat egy $N+M-2$ karakterből álló sztringgel add meg, ahol az $i$-edik karakter legyen $R$ ha az $i$-edik lépésben jobbra lépünk. Ha pedig lefele lépünk, akkor a karakter legyen $D$. 

### Korlátok
* $1 \le N, M \le 1000$
* $-1 \le A_{i,j} \le 10000$ minden $i,j$-re
* $A_{1,1} \not= -1$
* $A_{N,M} \not= -1$

### 1. példa bemenet
    5 6
    1 2 3 4 0 1
    2 -1 2 1 -1 3
    -1 0 6 0 0 0
    4 1 0 -1 1 -1
    0 0 1 2 0 0

### 1. példa kimenet
    17
    RRDDDDRRR

### 1. példa magyarázata
Könnyen ellenőrizhető, hogy a 4 lehetséges útvonalból ez a legjobb.

### 2. példa bemenet
    3 3
    1 2 -1
    2 -1 2
    -1 0 6

### 2. példa kimenet
    -1

### 2. példa magyarázata
Nem lehet eljutni a bal felső mezőről a jobb alsóra.
