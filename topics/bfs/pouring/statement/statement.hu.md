## Öntögetés
Egy távoli galaxisban, a Zog bolygón, a bölcs és jóindulatú Zorg király egy nagy találékonyságot igénylő feladattal állítja kihívás elé népét. A feladat az, hogy mérjenek ki pontosan $N$ egység Zogniumot, egy ritka és értékes folyadékot, mindössze két kannát használva. Ezeknek a kannáknak a térfogata $A$ és $B$ egység, amelyek a király kedvenc számai.

A kihívás győztese az, aki a lehető legkevesebb öntéssel pontosan $N$ egység Zogniumot tud kimérni a $B$ kannába. A hat lehetséges művelet, amit a kannákkal végre lehet hajtani:

1. Megtöltjük teljesen az első kannát.
2. Megtöltjük teljesen a második kannát.
3. Kiürítjük az első kannát.
4. Kiürítjük a második kannát.
5. Öntünk az első kannából a második kannába, amíg a második kanna tele nem lesz, vagy az első kanna ki nem ürül.
6. Öntünk a második kannából az első kannába, amíg az első kanna tele nem lesz, vagy a második kanna ki nem ürül.

Kezdetben mindkét kanna üres.

### Bemenet
A bemenet első sora tartalmazza a mérendő Zognium egységek számát ($N$). A második sor két egész számot tartalmaz, a két kanna térfogatát ($A$ és $B$).

### Kimenet
Egyetlen számot írj ki, a minimális öntések számát, amely szükséges ahhoz, hogy pontosan $N$ egység Zognium legyen a $B$ kannában, vagy $-1$-et, ha ezt lehetetlen elérni.

### Korlátok
* $1 \le N \le 1000$
* $1 \le A, B \le 1000$

### Példa bemenet
    2
    3 7

### Példa kimenet
    8

### A példa magyarázata
1. Megtöltjük az első kannát (3 egység).
2. Öntünk az első kannából a második kannába (3 egység a második kannában, 0 egység az első kannában).
3. Megtöltjük újra az első kannát (3 egység).
4. Öntünk az első kannából a második kannába (6 egység a második kannában, 0 egység az első kannában).
5. Megtöltjük az első kannát (3 egység).
6. Öntünk az első kannából a második kannába (7 egység a második kannában, 2 egység marad az első kannában).
7. Kiürítjük a második kannát (0 egység).
8. Öntünk az első kannából a második kannába (2 egység a második kannában, 0 egység az első kannában).

Bizonyítható, hogy a minimális szükséges öntések száma 8.
