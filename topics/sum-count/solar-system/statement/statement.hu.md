## Naprendszer
Bolygónk népe kíváncsi arra, hogy hány égi test van a naprendszerünkben. Ennek érdekében összegyűjtöttük, hogy melyik naprendszer béli bolygónak hány holdja van. Készíts egy programot, amely meg tudja állapítani, hogy hány égitest van a naprendszerben egy a bolygók holdjainak számát tartalmazó listából. (A feladat szempontjából égitestnek csak holdakat, bolygókat és csillagokat számítjuk és feltételezzük, hogy csak egy csillag van a naprendszer közepén.)

### Bemenet
A bemenet első sorában egyetlen egész szám van, a bolygók száma: $N$
A következő $N$ sorban egyetlen egy egész szám van, az $N$-edik bolygó holdjainak száma: $A_1, A_2, \dots, A_N$ 

### Kimenet
Egyetlen számot kell kiírnod, a naprendszer égitesteinek számát.

### Korlátok
* $1 \le N \le 100$
* $0 \le A_i \le 1000$

### Példa bemenet
    8
    0
    0
    1
    2
    95
    146
    27
    14

### Példa kimenet
    294

### A példa magyarázata
A holdakból összesen 285 van amihez ha hozzáveszünk még 8 bolygót és egy csillagot, akkor 294 égitestet kapunk.
