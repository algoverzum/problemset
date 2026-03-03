## Fibonacci függvény
A Fibonacci-számsorozat első két eleme 0 és 1, és minden további elem az azt megelőző két szám összege.
Így tehát a számsorozat: $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 \dots$

Írjunk programot, amely beolvas egy pozitív egész számot, majd kiírja a sorozat elemeit az $N$ sorszámúig. (A sorozat 0. és 1. sorszámú eleme 0 és 1.)

### Korlátok
* $1 \le N \le 50$

### Sablon
Indulj ki az előre megadott sablon kódból! Ne változtass a főprogramon semmit, mert különben nem lesz elfogadva.
Egy `fibonacci` nevű függvényt kell definiálnod magadnak, ami paraméterként kapja az $N$ értékét és a (kezdetben üres) listát/vectort, amibe a sorozat elemeit kell gyűjtened. C++-ban a vectort referenciaként kell átvenned, hogy a függvényen kívül is elérhető legyen a módosított lista.

### Példa bemenet
    10

### Példa kimenet
    0 1 1 2 3 5 8 13 21 34
