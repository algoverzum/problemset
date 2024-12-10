## Kétszer ugyanaz
Egy idegen bolygón különböző állatokat fogunk el megvizsgálásra, majd utána szabadon engedjük őket. Véletlenszerűen fogunk el állatot, de nem szeretnénk, ha kétszer egymás után ugyanazt az egyedet tanulmányoznánk. Feladatod, hogy $N$ elfogott állat kódjai közül találd meg az első olyan esetet, amikor egymás után ugyanazon kódú állatot fogtuk el. Ha nem fordul elő ilyen eset, akkor írj ki egy 0 számot.

### Bemenet
A bemenet első sorában egyetlen egész szám van, az elfogott állatok száma: $N$.
A bemenet második sorában $N$ szám van, az állatok kódjai: $A_1, A_2, \dots, A_N$

### Kimenet
Egyetlen számot kell kiírnod, az első olyan kód sorszámát, amely megegyezik a rákövetkezővel. Ha nincs ilyen sorszám, akkor 0-t kell kiírni.

### Korlátok
* $1 \le N \le 100$
* $1 \le A_i \le 1000$

### Példa bemenet
    5
    98 95 92 92 100

### Példa kimenet
    3

### A példa magyarázata
A harmadik és a negyedik sorszámú érték megegyezik, így 3 a jó válasz.
