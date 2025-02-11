## Szólánc
Egy ősi, titkos ajtó rejtélyes szókirakót tartalmaz. A régészek csapata csak akkor tudja kinyitni, ha sikerül megfejteni a rejtvényt. Mivel nincs más mód a bejutásra, a feladvány megoldása létfontosságú számukra.

Az ajtón számos mágneses lemez található, mindegyiken egy-egy szóval. A lemezeket úgy kell sorrendbe állítani, hogy minden szó ugyanazzal a betűvel kezdődjön, amellyel az előző szó végződik. Például a "delta" szót követheti a "arrow" szó, mert az "a" betűvel kezdődik.

A feladatod, hogy készíts egy számítógépes programot, amely megvizsgálja a kapott szavak listáját, és eldönti, hogy lehetséges-e az összes lemezt a megadott szabály szerint sorrendbe állítani – és ezzel kinyitni az ajtót.

### Bemenet
A bemenet első sorában egyetlen egész szám van: $N$, a szavak száma.
A következő $N$ sorban egy-egy szó van. 

### Kimenet
Egyetlen szót kell kiírnod, ami `YES`, ha lehet a szavakat megfelelő sorrendbe rendezni, `NO` ha nem.

### Korlátok
* $1 \le N \le 100\,000$
* A szavak legalább 1 és legfeljebb 10 karakter hosszúak, az angol ábécé kisbetűiből állnak.

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
