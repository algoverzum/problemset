## Feladatkitűzés
*A feladat megtörtént eseményeken alapszik.*

Egy meg nem nevezett programozási verseny szervezőbizottsága idén több
forduló megrendezését tervezi, melyek mindegyike $N$ darab, különböző
nehézségű feladatból áll. Azt szeretnénk, hogy a feladatok nehézségi
szintjei $1, 2, \ldots, N$ legyenek.

A versenyre rengeteg feladatjavaslat érkezett. Ezek mindegyikéhez
tartozik egy nehézségi szint, mely lehet

-   egy $i$ egész szám ($1 \le i \le N$), ami azt jelenti, hogy a
    javaslat valamelyik forduló $i$ nehézségű feladataként használható;
    vagy

-   egy $i.5$ alakú érték, ahol $i$ egész szám, ($1 \le i < N$), mely
    akár $i$ nehézségű, akár $i+1$ nehézségű feladat is lehet.

Az $N$ értékének és az egyes feladatok nehézségének ismeretében határozd
meg, hogy legfeljebb hány fordulót lehet összeállítani ezen
feladatokból. Minden feladatot legfeljebb egy fordulóban használhatsz
fel!

### Bemenet
Minden teszt több tesztesetet tartalmaz. A bemenet első sora egyetlen
$T$ egész számot tartalmaz, a tesztesetek számát.

Minden teszteset első sora egyetlen $N$ egész számot tartalmaz, az egy
fordulóba választandó feladatok számát.

A teszteset második sora $N$ darab, $A_1, A_2,\ldots, A_N$ egész számot
tartalmaz, ahol $A_i$ az $i$ nehézségű feladatok száma.

A harmadik sorában $N-1$ darab $B_1,B_2,\ldots,B_{N-1}$ egész szám
található, ahol $B_i$ az $i.5$ nehézségű feladatok száma.

### Kimenet
Minden tesztesethez egyetlen egész számot adj meg, az adott nehézségű
feladatokból összeállítható fordulók maximális számát.

### Korlátok
-   $1 \le T \le 10\,000$.

-   $2 \le N \le 200\,000$.

-   $0 \le A_i \le 1\,000\,000\,000$ minden $i=1 \ldots N$-re.

-   $0 \le B_i \le 1\,000\,000\,000$ minden $i=1 \ldots N-1$-re.

-   Az $N$-ek összege tesztenként nem haladja meg a
    $200\,000$-t.



### Példa bemenet
    5
    6
    0 1 1 0 1 1
    1 0 1 0 1
    5
    0 1 1 1 0
    1 0 1 0
    2
    1 1
    2
    6
    0 0 0 0 0 0
    5 2 5 100 9
    7
    1 3 0 4 1 0 2
    4 3 1 3 1 5


### Példa kimenet
    1
    0
    2
    3
    4


### A példa magyarázata
Az **első tesztesetben** $7$ feladatjavaslat van, amelyeknek a nehézsége
rendre $1.5$, $2$, $3$, $3.5$, $5$, $5.5$ és $6$.

Ezekből a feladatokból egyetlen fordulót hozhatunk létre:

-   A $1.5$-es nehézségi szintű javaslat a forduló első feladata lesz.

-   A $2$-es nehézségi szintű javaslat a forduló második feladata lesz.

-   A $3$-as nehézségi szintű javaslat a forduló harmadik feladata lesz.

-   A $3.5$-es nehézségi szintű javaslat a forduló negyedik feladata
    lesz.

-   A $5.5$-es nehézségi szintű javaslat a forduló ötödik feladata lesz.

-   A $6$-os nehézségi szintű javaslat a forduló hatodik feladata lesz.

Belátható, hogy nem hozható létre egyetlen teljes forduló sem a
**második tesztesetben** található feladatokból.

A **harmadik tesztesetben** két fordulót állíthatunk össze, melyek ilyen
nehézségű feladatokat tartalmaznak:

-   $[1,1.5]$

-   $[1.5,2]$

A **negyedik tesztesetben** az alábbi fordulók létrehozása lehetséges:

-   $[1.5,1.5,3.5,3.5,5.5,5.5]$

-   $[1.5,1.5,3.5,3.5,5.5,5.5]$

-   $[1.5,2.5,2.5,3.5,5.5,5.5]$

