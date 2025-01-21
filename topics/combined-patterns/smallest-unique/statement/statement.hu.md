## Legkisebb egyedi szám
Néhány gyerek azt a játékot játssza, hogy mindenki titokban leír egy pozitív számot egy kis papírra. Az nyer, aki a legkisebb olyan számot írja, amit senki más nem ír. A leírt számok listájának ismeretében határozd meg a nyertes számot! Ha nincs nyertese a játéknak írj ki -1-et.

### Bemenet
A bemenetben első sorában egyetlen egész szám van: $N$, a gyerekek száma. 
A bemenet második sorában $N$ egész szám van: $A_1, A_2, \ldots, A_N$, a gyerekek által leírt számok.

### Kimenet
Egyetlen számot kell kiírnod, a legkisebb számot ami csak egyszer fordul elő a számsorozatban. Ha nincs ilyen szám, akkor -1-et.

### Korlátok
* $1 \le N \le 100$
* $1 \le A_i \le 100$

### Példa bemenet
    7
    2 4 5 2 2 5 6

### Példa kimenet
    4

### A példa magyarázata
A legkisebb szám a 2, de többször előfordul. A 4 a második legkisebb szám és csak egyszer fordul elő ezért 4 a megoldás.
