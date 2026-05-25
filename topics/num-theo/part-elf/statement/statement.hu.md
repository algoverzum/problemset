## Tünde felmenők
Vida azt állítja, hogy részben tünde, vagyis legalább egy őse teljes tünde volt. Nem tudja, hogy ez a szülője, nagyszülője vagy egy még régebbi felmenője volt-e.

Ha egy szülő $A/B$ részben tünde, a másik pedig $C/D$ részben tünde, akkor a gyermek tünde-aránya:

$$\frac{A/B+C/D}{2}$$

Például egy ember ($0/1$) és egy félig tünde ($1/2$) gyermeke $1/4$ részben tünde.

Tudjuk, hogy 40 generációval korábban minden őse vagy teljes tünde ($1/1$), vagy teljes ember ($0/1$) volt.

Feladat: Adott Vida tünde-aránya $P/Q$ (nem feltétlenül egyszerűsített alakban). Határozd meg, hogy legkevesebb hány generációval ezelőtt lehetett egy teljes tünde őse.

Ha ilyen származás nem lehetséges, írd ki: "impossible".

### Bemenet
A bemenet első sorában egyetlen egész szám van: $P$.  
A bemenet második sorában egyetlen egész szám van: $Q$.

### Kimenet
Egyetlen számot kell kiírnod, hogy legkevesebb hány generációval ezelőtt lehetett egy teljes tünde őse vagy azt, hogy "impossible", ha a megadott arány nem állhat elő.

### Korlátok
* $1 \le P < Q \le 10^{12}$

### 1. Példa bemenet
    1
    2

### 1. Példa kimenet
    1

### Az 1. példa magyarázata
Vida lehetett egy teljes tünde ($1/1$) és egy ember ($0/1$) gyermeke. Ebben az esetben egy teljes tünde őse már 1 generációval ezelőtt létezett, ezért a válasz 1.

### 2. Példa bemenet
    3
    4

### 2. Példa kimenet
    1

### A 2. példa magyarázata
Vida lehetett egy teljes tünde ($1/1$) és egy félig tünde ($1/2$) gyermeke. Így szintén volt teljes tünde őse 1 generációval ezelőtt, tehát a válasz 1.

### 3. Példa bemenet
    1
    4

### 3. Példa kimenet
    2

### A 3. példa magyarázata
Vida lehetett egy ember ($0/1$) és egy félig tünde ($1/2$) gyermeke. A félig tünde szülő pedig lehetett egy teljes tünde ($1/1$) és egy ember ($0/1$) gyermeke. Így a legközelebbi teljes tünde ős 2 generációval ezelőtt élt, ezért a válasz 2.

### 4. Példa bemenet
    2
    23

### 4. Példa kimenet
    impossible

### A 4. példa magyarázata
Nem lehetséges pontosan $2/23$ részben tündének lenni. Ezért a válasz "impossible".

### 5. Példa bemenet
    123
    31488

### 5. Példa kimenet
    8
