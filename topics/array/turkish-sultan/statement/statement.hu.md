## Török Szultán
A török szultán börtönében $N$ darab cella van, 1-től $N$-ig számozva. A cellák ajtói kezdetben mind zárva vannak.

Születésnapján a szultán először jókedvű lett, ezért elküldte az 1. szolgát, hogy nyissa ki az összes cella ajtaját (az $1., 2., 3., \ldots, N$. ajtót).

Később meggondolta magát, így a 2. szolgát arra utasította, hogy minden 2. cella ajtaját fordítsa meg: ha nyitva van, zárja be; ha zárva van, nyissa ki (tehát a $2., 4., 6., \ldots$ cellákat).

Ezután a 3. szolga következett, aki minden 3. cella ajtaját fordította meg ($3., 6., 9., \ldots$).

A folyamat így folytatódik egészen az $N$. szolgáig, aki csak a $N$. cella ajtaját fordítja meg.

Írj programot, amely kiírja, hogy a végén mely ajtók maradnak nyitva, azaz mely rabok szabadulnak ki!

### Bemenet
A bemenetben egyetlen egész szám van: $N$ - a börtöncellák száma.

### Kimenet
Írd ki, hogy a végén mely ajtók maradnak nyitva, azaz mely rabok szabadulnak ki!
A cellaszámokat egy sorban, növekvő sorrendben, szóközzel elválasztva írd ki.

### Korlátok
* $1 \le N \le 100$

### Példa bemenet
    6

### Példa kimenet
    1 4

### A példa magyarázata
Az 1. szolga után mindegyik nyitva lesz: nyitva, nyitva, nyitva, nyitva, nyitva, nyitva

A 2. szolga után: nyitva, zárva, nyitva, zárva, nyitva, zárva

A 3. szolga után: nyitva, zárva, zárva, zárva, nyitva, nyitva

A 4. szolga után: nyitva, zárva, zárva, nyitva, nyitva, nyitva

Az 5. szolga után: nyitva, zárva, zárva, nyitva, zárva, nyitva

A 6. szolga után: nyitva, zárva, zárva, nyitva, zárva, zárva

Azaz az első és a negyedik cella lesz nyitva.
