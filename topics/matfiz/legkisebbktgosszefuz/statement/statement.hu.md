## Legkisebb költségű összefűzés
Adott n darab pozitív egész szám, amelyek „költségeket” jelentenek.  A feladat:
* mindig válasszuk ki a két legkisebb számot,
* adjuk össze őket,
* az összeget tegyük vissza a halmazba,
* ismételjük, amíg csak egy szám marad.

A végén írjuk ki a műveletek összköltségét!

### Bemenet
A standard input első sorában egyetlen szám van, az elemek száma ($n$). A következő sorban $n$ darab elem van, egymástól pontosan egy szóközzel elválasztva ($s_1, \dots, s_n$). 

### Kimenet
A kimenet egyetlen sort tartalmaz, az összköltséget!

### Korlátok
* $1 \leq n \leq 100$
* $1 \le b_i \le 1000$

### Példa bemenet
    4
    4 3 2 6

### Példa kimenet
    29

### A példa magyarázata
Lépések:
* 2 + 3 = 5 → összköltség: 5. (A 2 és a 3 a két legkisebb elem.)
* 4 + 5 = 9 → összköltség: 14.
* 6 + 9 = 15 → összköltség: 29.

### Hint 1
Prioritási sor kell, min-heap. Hogyan kell deklarálni?

### Hint 2
Melyik metódussal lehet a sorba berakni? Melyikkel kivenni?

### Hint 3
Mi lesz a ciklus fejrészében a feltétel? A size() adja vissza a prioritási sor elemeinek a számát!
