## Rendezés
A bolygónkon földtani kutatás érdekében kőzetmintákat vettünk és felbontottuk elemekre, amiket a periódusos rendszerbeli rendszámaik alapján szeretnénk őket sorba rendezni két csoportnyi kutatónak. Az egyik kutató csoport növekvő sorrendben szeretné megkapni őket, a másik pedig csökkenőben. Írj egy programot, ami kiírja mind a két fajta rendezést.

### Bemenet
A bemenet első sorában egyetlen egész szám van, az elemek száma: $N$.
A bemenet második sorában $N$ szám van, az elemek rendszámai: $A_1, A_2, \ldots, A_N$.

### Kimenet
A kimenet első sorába $N$ számot kell kiírnod, az elemek rendszámait növekvő sorrendben.
A kimenet második sorába $N$ számot kell kiírnod, az elemek rendszámait csökkenő sorrenben.

### Korlátok
* $1 \le N \le 100$
* $1 \le A_i \le 103$

### Példa bemenet
    8
    3 12 5 7 9 9 10 1

### Példa kimenet
    1 3 5 7 9 9 10 12
    12 10 9 9 7 5 3 1

### A példa magyarázata
A bemenetben szereplő számokat először növekvő, majd aztán csökkenő sorrendbe rendeztük.
