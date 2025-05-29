## Csillagközi olimpia
A tejút rendszerben most értek véget az olimpiai játékok. Az esemény után feljegyeztük az egyes bolygók által elért összes arany-, ezüst- és bronzérmet. Ezeket egy táblázatba írtuk, ahol egy adott $i$-edik sorba az $i$ sorszámú bolygó adatai vannak beírva. Ezek alapján szeretnénk sorrendbe állítani az egyes bolygókat, hogy ki szerezte a legtöbb érmet. A sorba állítás szabálya a következő: Egy bolygó előrébb kerül, ha több arany érme van, mint egy másik bolygónak. Ha két bolygó azonos darabszámú aranyérmet szerzett, akkor az kerül előrébb, amelyik több ezüstérmet szerzett. Ha abból is egyenlő darabszámút szerzett a két bolygó, akkor az kerül előrébb, amelyiknek több bronzérme van. Ha mindegyik érem darabszáma megegyezik, akkor a kisebb sorszámú kerül előrébb. Ez alapján rendezd sorrendbe a bolygókat.

### Bemenet
A bemenet első sorában egy egész szám van, a bolygók száma: $N$
A bemenet következő $N$ sorába rendre három szám van, az arany-, ezüst és bronz medálok száma: $G_1 \dots, G_N; S_1 \dots S_N; B_1 \dots B_N$

### Kimenet
A kimenetbe egyetlen sort kell írnod $N$ számmal, a bolygók sorszámait az érmek alapján sorba rendezve.

### Korlátok
* $1 \le N \le 100$
* $1 \le G_i \le 1000$
* $1 \le S_i \le 1000$
* $1 \le B_i \le 1000$

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
Az arany medálok szerint sorba rendezhető az első, negyedik és ötödik sor. A második és harmadik sor között az ezüst érmek száma dönt.
