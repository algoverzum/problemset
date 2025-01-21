## Naprendszer
Bolygónk népe kíváncsi arra, hogy hány égitest van a naprendszerünkben. Ennek érdekében összegyűjtöttük, hogy a naprendszerünk egyes bolygóinak hány holdja van. Készíts egy programot, amely megállapítja, hogy hány égitest van a naprendszerben, ha adott egy lista, amely az egyes bolygók holdjainak számát tartalmazza. (A feladat szempontjából égitestnek csak holdakat, bolygókat és csillagokat számítjuk és feltételezzük, hogy csak egy csillag van a naprendszer közepén.)

### Bemenet
A bemenet első sorában egyetlen egész szám van, a bolygók száma: $N$.
A második sorban $N$ egész szám van, az egyes bolygók holdjainak száma: $A_1, A_2, \dots, A_N$.

### Kimenet
Egyetlen számot kell kiírnod, a naprendszer égitesteinek számát.

### Korlátok
* $1 \le N \le 100$
* $0 \le A_i \le 1000$

### Példa bemenet
    8
    0 0 1 2 9 14 3 14

### Példa kimenet
    52

### A példa magyarázata
A holdakból összesen 43 van, amihez ha hozzáveszünk még 8 bolygót és 1 csillagot, akkor 52 égitestet kapunk.
