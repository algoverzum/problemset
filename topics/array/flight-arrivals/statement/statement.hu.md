## Repülő érkezések
Mo Sais Leenak van két reptére: Espa és Pelgo. Tudjuk, hogy ma hány repülőgép érkezik és hogy ezeken a gépeken hány utas lesz. Szeretnénk ezeket a gépeket felváltva elosztani közöttük. Az első gép menjen Espára, a második Plegora, a harmadik Espára, stb. A két reptér szeretné mielőbb megtudni, hogy a hozzájuk érkező gépeken hány utas van. 


### Bemenet
A bemenet első sorában egyetlen egész szám van: $N$ - az aznap érkező repülőgépek száma.
A második sorban pedig $N$ szóközzel elválasztott szám $A_0, A_1, \ldots, A_{N-1}$ található, az egyes repülőgépeken érkezők száma.

### Kimenet
A kimenet első sorába írd ki az Espába menő gépeken utazók számát szóközzel elválasztva. (Azaz $A_0, A_2, A_4, \ldots$ írandó ide.)
A kimenet második sorába írd ki a Pelgoba menő gépeken utazók számát szóközzel elválasztva. (Azaz $A_1, A_3, A_5, \ldots$ írandó ide.)

### Korlátok
* $1 \le N \le 100$
* $0 \le A_i \le 100$

### Példa bemenet
    5
    1 2 3 4 5

### Példa kimenet
    1 3 5
    2 4

### A példa magyarázata
Az első gép 1 utasa Espába, a második gép 2 utasa Pelgoba, a harmadik gép 3 utasa Espába, a negyedik gép 4 utasa Pelgoba, míg az ötödik gép 5 utasa Espába jut el. Azaz Espába rendre 1, 3, 5 utas megy, mag Pelgoba 2, 4. 