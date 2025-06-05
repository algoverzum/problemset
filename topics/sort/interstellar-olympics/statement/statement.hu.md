## Csillagközi olimpia
A Tejútrendszerben éppen most értek véget az olimpiai játékok, amin $N$ bolygó sportolói vettek részt. Az eseményt követően feljegyeztük, hogy az egyes bolygók hány arany-, ezüst- és bronzérmet szereztek. Az adatokat egy táblázatba rendeztük, ahol az $i$-edik sor az $i$-edik sorszámú bolygó eredményeit tartalmazza ($1 \le i \le N$).  
A bolygókat az alábbi szabályok alapján szeretnénk sorrendbe állítani az éremeredményeik szerint:

* Az a bolygó kerül előrébb, amelyik több aranyérmet szerzett.
* Ha az aranyérmek száma megegyezik, akkor az kerül előrébb, amelyik több ezüstérmet szerzett.
* Ha az ezüstérmek száma is megegyezik, akkor az kerül előrébb, amelyiknek több bronzérme van.
* Ha minden éremtípusból ugyanannyit szereztek, akkor a kisebb sorszámú bolygó kerül előrébb.

Rendezés után írd ki a bolygók sorrendjét!

### Bemenet
A bemenet első sorában egy egész szám van, a bolygók száma: $N$.  
A következő $N$ sorba rendre három szám van, az arany, ezüst és bronz medálok száma (az $i$-edik sorban az $i$ sorszámú bolygó érmeinek a száma):

$G_1, S_1, B_1$  
$G_2, S_2, B_2$  
$\vdots$  
$G_N, S_N, B_N$

### Kimenet
A kimenetbe egyetlen sorba kell kiírnod $N$ számot, a bolygók sorszámait az érmek alapján sorba rendezve.

### Korlátok
* $1 \le N \le 100\,000$
* $1 \le G_i \le 10^6$ minden $i=1,\ldots,N$ esetén
* $1 \le S_i \le 10^6$ minden $i=1,\ldots,N$ esetén
* $1 \le B_i \le 10^6$ minden $i=1,\ldots,N$ esetén

### Példa bemenet
    5
    4 4 4
    3 2 3
    3 3 1
    1 5 5
    2 1 1

### Példa kimenet
    1 3 2 5 4

### A példa magyarázata
Az 1. bolygónak van a legtöbb aranyérme (négy), a második legtöbb (három) holtversenyben a 2. és 3. bolygónak, köztük az ezüstérmek száma dönt a 3. bolygó javára. Majd az 5. bolygó jön két aranyéremmel, és végül a 4. bolygó egy aranyéremmel, hiába van sok érme összesen.
