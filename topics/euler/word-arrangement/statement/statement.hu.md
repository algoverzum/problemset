## Szó rendezés
Egy titkos ajtó nagyon érdekes szókirakót tartalmaz. A régészek csapatának meg kell oldania
hogy kinyissa az ajtót. Mivel másképp nem lehet kinyitni az ajtót, ezért a rejtvény nagyon fontos.
számunkra.
Az ajtón nagyszámú mágneses lemez található. Minden lemezre egy szó van írva.
A lemezeket úgy kell sorrendbe állítani, hogy minden szó ugyanazzal a betűvel kezdődjön, mint amivel az előző szó végződik. Például az „acm” szót követheti a „motorola” szó.
Az Ön feladata, hogy írjon egy olyan számítógépes programot, amely elolvassa a szavak listáját, és meghatározza, hogy
lehetséges-e az összes táblát sorrendbe állítani (a megadott szabály szerint), és ezzel
kinyitni az ajtót.

### Bemenet
A bemenetben első sorában egyetlen egész szám van: $N$
A következő $N$ sorban $S$ szavak vannak. 

### Kimenet
Egyetlen szót kell kiírnod, YES-t, ha lehet a szavakat megfelelő sorrendbe rendezni, NO ha nem.

### Korlátok
* $1 \le N \le 100000$
Az $S$ szavak legalább 1 és legfeljebb 10 karakter hosszúak. És az angol ábécé kisbetűiből állnak.
### Példa bemenet
    6
    entrance
    exit
    code
    token
    cryptic
    enigmatic

### Példa kimenet
    YES

### A példa magyarázata
enigmatic -> cryptic -> code -> entrance -> exit -> token
