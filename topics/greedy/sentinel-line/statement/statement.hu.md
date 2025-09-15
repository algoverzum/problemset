## Védelmi vonal
A Föderáció egy egyenes határvonal mentén $N$ megfigyelő állomást üzemeltet. Most álcázó generátorokat szeretnénk telepíteni, amelyek $H$ sugarú körben elrejtik az állomásokat. Az álcázó generátorokat **csak a megfigyelő állomások helyére lehet telepíteni**.

A feladat: válaszd ki a szükséges állomásokat úgy, hogy **minimális számú álcázó generátor** lefedje az összes állomást.

Például, ha az állomások koordinátái $0, 10, 30, 40, 60, 85, 100$, és a generátorok $20$ egység sugarúak, akkor elég három generátor: a 10., 60. és 100. koordinátánál (de több megoldás is lehetséges).

![](tex/abra.png)

### Bemenet
A bemenet első sorában két szám van: $N, H$ - a megfigyelő állomások száma és a generátorok sugara.

A második sorban $N$ szám szerepel: $A_1, A_2, \ldots, A_N$ - a megfigyelő állomások távolságai az elsőtől ($A_1 = 0, A_i < A_{i+1} (1 \le i \le N-1$).

### Kimenet
A kimenet első sorában egyetlen szám legyen: $M$, a szükséges generátorok minimális száma.

A második sor pontosan $M$ egész számot tartalmazzon, sorrendben azon megfigyelő állomások sorszámait, ahova generátort kell telepíteni.

Több megoldás esetén bármelyik megadható.

### Korlátok
* $1 \le N \le 10^5$
* $1 \le H \le 10^9$
* $0 \le A_1 < A_2 < \ldots < A_N \le 10^9$

### Példa bemenet
    7 20
    0 10 30 40 60 85 100

### Példa kimenet
    3
    2 5 7

### A példa magyarázata
Az álcázó generátorokat a 2., 5. és 7. állomásokhoz telepítve minden állomás lefedett. Más kombinációk is lehetségesek, pl. 1., 4., 6. állomások.

