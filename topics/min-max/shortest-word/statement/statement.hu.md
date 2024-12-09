## Legrövidebb Szó
Egy ősi civilizáció kincstárába szeretnél bejutni. Kalandjaid során már megszerezted a listát ami tartalmazza a kulcsszót, de a listán van több szó is félrevezetésként. Szerencsére tudod, hogy a kulcsszó a legrövidebb szó a listán, ha több legövidebb szó is szerepel a listán, akkor a valódi kulcsszó, amelyik először szerepelt. Találd meg a kulcsszót!

### Bemenet
A bemenetben első sorában egyetlen egész szám van: $N$ 
A második sorában $N$ db szó szóközzel elválasztva.

### Kimenet
A bemenet legrövidebb szavát kell kiírnod. Ha több legrövidebb szó is van, akkor azt kell kiírnod amelyik először fordult elő.

### Korlátok
* $1 \le N \le 100$
A szavak az angol ábécé kisbetűiből állnak és legfeljebb 1000 betű hosszúak.

### Példa bemenet
    6
    silver gold iron bronze platinum copper

### Példa kimenet
    gold

### A példa magyarázata
    silver 6 betű
    gold 4 betű
    iron 4 betű
    bronze 6 betű
    platinum 8 betű
    copper 6 betű
    2 db 4 betűs szó van a gold és az iron, de a gold van előrébb ezért az a kulcsszó.
