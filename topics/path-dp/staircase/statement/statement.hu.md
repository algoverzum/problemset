## Lépcső
A Jedi Templom bejáratához egy lépcső vezet, $N$ lépcsőfokkal. Egy fiatal padawan egyszerre legfeljebb $K$ lépcsőfokot tud ugrani az Erő segítségével.
Minden nap egyszer kell feljutnia a templomba edzésre.

Készíts egy programot, amely kiszámolja, hány napig tud a padawan más és más módon feljutni a lépcső tetejére!

### Bemenet
A bemenetben egyetlen sorban két egész szám van: $N, K$ - a lepcsőfokok száma, és a maximális ugrás nagysága. 

### Kimenet
Egyetlen számot kell kiírnod, ami megadja az összes különböző feljutások számát.

### Korlátok
* $1 \le N \le 32$
* $1 \le K \le 16$

### 1. Példa bemenet
    3 2

### 1. Példa kimenet
    3

### A példa magyarázata
A lehetséges feljutások $(1,1,1)$, $(1,2)$ és $(2,1)$, ahol a számok az ugrások nagysága. 

### 2. Példa bemenet
    20 5

### 2. Példa kimenet
    400096