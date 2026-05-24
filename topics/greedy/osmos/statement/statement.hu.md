## Gömböc
Árminnak van egy $A$ méretű gömböce, valamint adott $N$ további gömböc is.

* Egy gömböc csak nála kisebb gömböcöt tud elnyelni.
* Ha egy $X$ méretű gömböcöt elnyel, akkor a mérete $X$-szel nő.
* A gömböcök tetszőleges sorrendben nyelhetők el.

Egy művelet során az alábbi két lépés közül egyet végezhetünk el:

* hozzáadunk egy tetszőleges pozitív egész méretű új gömböcöt;
* eltávolítunk egy meglévő gömböcöt.

Határozzuk meg a minimális műveletszámot, amely szükséges ahhoz, hogy Ármin gömböce végül az összes többi gömböcöt el tudja nyelni.

### Bemenet
A bemenet első sora két egész számot tartalmaz: Ármin gömböcének méretét ($A$) és a többi gömböc számát ($N$).  
A második sor $N$ darab egész számot tartalmaz: $M_1, M_2, \ldots, M_N$, amelyek a többi gömböc méretét adják meg.  
Minden megadott méret egész szám.

### Kimenet
Egyetlen számot kell kiírnod, a minimális műveletszámot, amely szükséges ahhoz, hogy Ármin gömböce végül az összes többi gömböcöt el tudja nyelni.

### Korlátok
* $1 \le N \le 100$
* $1 \le A \le 10^6$
* $1 \le M_i \le 10^6$ minden $i=1, 2, \ldots, N$-re.

### 1. Példa bemenet
    2 2
    2 1

### 1. Példa kimenet
    0

### Az 1. példa magyarázata
A kezdetben 2 méretű gömböc először az 1-est lenyelve 3-as méretű lesz. Így viszont a 2-est is le tudja nyelni. Azaz nem kell sem hozzáadni, sem elvenni.

### 2. Példa bemenet
    2 4
    2 1 1 6

### 2. Példa kimenet
    1

### A 2. példa magyarázata
Ha a 6-ost elvesszük, akkor már a maradékot le tudja nyelni.
De az is megfelelő lenne ha hozzáadnánk például egy 3-as gömböcöt.

### 3. Példa bemenet
    10 4
    25 20 9 100

### 3. Példa kimenet
    2

### 4. Példa bemenet
    1 4
    1 1 1 1

### 4. Példa kimenet
    4
