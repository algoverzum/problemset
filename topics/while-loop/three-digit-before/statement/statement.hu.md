## Háromjegyűek száma
Bolygónkon a Bingót úgy játsszuk, hogy a műsorvezető sorsol ki számokat, amíg a nulla ki nem jön. Ekkor véget ér a játék, és akinek a szelvényén a legtöbb szám jött ki, az a nyertes. A Te szelvényeden az összes háromjegyű szám szerepel. Meg tudod mondani, hogy hány számodat sorsolták ki?

### Bemenet
A bemenetben egész számok vannak, minden sorban egy szám. Az $i.$ sorban található szám az $i.$ kisorsolt szám, $S_i$. Garantáltan az utolsó sorban nulla van.

### Kimenet
Egyetlen számot kell kiírnod, a háromjegyű számok számát. 

### Korlátok
* $0 \le S_i \le 1\, 000\, 000$.
* Ha $i\not=j$ akkor $S_i\not=S_j$.
* a nem üres sorok $N$ számára $1 \le N \le 1000$.

### Példa bemenet
    5
    123
    12345
    12
    555
    678
    2
    0

### Példa kimenet
    3

### A példa magyarázata
A nulla előtt 3 háromjegyű szám volt: 123, 555, 678.
