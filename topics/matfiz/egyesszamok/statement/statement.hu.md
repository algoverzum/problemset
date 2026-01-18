## Egyes Számok
Írj programot, amely összeadja egy legfeljebb 500 jegyű természetes szám számjegyeit! Ha a kapott szám nem egyjegyű, akkor ennek újra adjuk össze a számjegyeit, s az eljárást folytassuk, amíg egyjegyű számot nem kapunk.

Bizonyos kiinduló számok esetén a végeredmény 1 lesz. Ha az eredmény 1 lesz, akkor a program 1-et íron ki, egyébként 0-át.

### Bemenet
A bemenetben egyetlen egész szám van: $N$. 

### Kimenet
Ha az eredmény 1 lesz, akkor a program 1-et íron ki, egyébként 0-át.

### Korlátok
* $1 \le N \le 10^{500}$

### 1. Példa bemenet
    91

### 1. Példa kimenet
    1

### Az 1. példa magyarázata
$91 \to 9+1=10 \to 1+0=1$

### 2. Példa bemenet
    1998

### 2. Példa kimenet
    0

### A 2. példa magyarázata
$1998 \to 1+9+9+8=27 \to 2+7=9$

### 3. Példa bemenet
    28

### 3. Példa kimenet
    1

### A példa magyarázata
$28 \to 2+8=10 \to 1+0=1$
