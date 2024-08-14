## Bimm-bamm sorozat
Néhány gyerek azt a játékot játssza, hogy egyesével számolnak 1-től kezdve, viszont a 3-mal osztható számok helyett `bimm`-et mondanak, az 5-tel osztható számok helyett `bamm`-ot, a 3-mal és 5-tel is oszthatók helyett pedig `bumm`-ot. Írd ki, hogy miket mondanak, ha egy megadott $N$ számig mennek el!

### Bemenet
A bemenetben egyetlen egész szám van: $N$ - a játék felső határa.

### Kimenet
$N$ sort írj ki, minden sorban egy szám legyen, vagy pedig a helyette mondandó szó (`bimm` / `bamm` / `bumm`).

### Korlátok
* $1 \le N \le 100$

### Példa bemenet
    8

### Példa kimenet
    1
    2
    bimm
    4
    bamm
    bimm
    7
    8

### A példa magyarázata
A gyerekeknek `bimm`-et kell mondani a 3 és a 6 helyett, mert azok 3-mal oszthatók és `bamm`-ot az 5 helyett, mert az 5-tel osztható. A példában nincs `bumm`, hiszen az első alkalommal a 15 helyett kellene azt mondani.
