## Feladatütemező
Egy operációs rendszer feladatokat kap végrehajtásra. Minden feladathoz tartozik egy prioritás. Minél nagyobb a prioritás értéke, annál hamarabb kell a feladatot végrehajtani. Ha két vagy több feladat prioritása megegyezik, akkor közülük az kerül előbb végrehajtásra, amelyik \*\*korábban érkezett\*\*, azaz a bemenetben korábban szerepel (FIFO-elv az egyenlő prioritásúak között).

Olvassuk be a feladatok nevét és prioritását, majd írjuk ki a végrehajtás sorrendjét!

### Bemenet
A standard bemenet első sora egyetlen egész számot tartalmaz, a feladatok számát ($n$).
A következő $n$ sor mindegyike egy feladat nevét és prioritását tartalmazza, szóközzel elválasztva. A feladat neve egyetlen nagybetű.

### Kimenet
A kimenet tartalmazza a feladatok nevét a végrehajtás sorrendjében, soronként egyet.

### Korlátok
*  $1 \le n \le 26$
*  az angol ábécé nagybetűi

### Példa bemenet
    5
    A 5
    B 2
    C 9
    D 1
    E 7

### Példa kimenet
    C
    E
    A
    B
    D

### A példa magyarázata
A legnagyobb prioritású feladat a C (9), ezt követi az E (7), majd az A (5), B (2) és végül a D (1).

### Hint 1
A prioritási sor tetején mindig a legnagyobb prioritású elem található.

### Hint 2
Érdemes egy saját struktúrát létrehozni, amely tárolja a feladat nevét, prioritását és a beolvasás sorszámát.

### Hint 3
A prioritási sorból addig vegyük ki az elemeket, amíg ki nem ürül. Az egyenlő prioritásúak sorrendjét a beolvasási sorszám dönti el: a kisebb sorszám kerül előbbre. A prioritási sorból addig vegyük ki az elemeket, amíg ki nem ürül.