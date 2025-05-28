## Intergalaktikus megmérettetés
Az ICPC (Intergalactic Creatures' Programming Contest) a világegyetem legrangosabb programozó versenye. Minden évben számos csapat vesz részt rajta, ezért fontos hatékonyan kiszámolni a verseny eredményét.

A versenyről kapott adatok alapján minden csapatról tudod, hogy hány feladatot oldottak meg és mennyi büntetőpontot kaptak (amit a feladatok megoldásához szükséges idő és a korábbi hibás megoldások alapján számolnak). A feladatod a verseny végső rangsorának meghatározása. Az A csapat megelőzi a B csapatot, ha több feladatot oldott meg, vagy ha ugyanannyi feladatot oldott meg, de kevesebb büntetőpontot szerzett.

### Bemenet
A bemenet első sora egy egész számot tartalmaz: $N$ - a csapatok számát.
A következő $N$ sor mindegyike két számot tartalmaz, $A_i$-t és $B_i$-t, az $i$-edik csapat által megoldott feladatok számát és a csapat büntetőpontjait. Bármely két sor (legalább az egyik számban) különbözik.

### Kimenet
Egyetlen sort írj ki $N$ számmal, a csapatok azonosítóit a végső sorrendben (a győztes csapattal kezdve).

### Korlátok
* $1 \le N \le 100\,000$
* $0 \le A_i, B_i \le 10^9$ minden $i=1 \dots N$ esetén

### Példa bemenet
    5
    2 10
    2 20
    3 40
    1 20
    0 0

### Példa kimenet
    3 1 2 4 5

### A példa magyarázata
A 3-as csapat nyert 3 megoldott feladattal. Az 1-es csapat a második helyen végzett, megelőzve a 2-es csapatot az alacsonyabb büntetőpontszámmal, azonos számú megoldott feladat mellett.

