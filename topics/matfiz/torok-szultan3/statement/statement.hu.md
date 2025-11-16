## Török Szultán 3
A török szultánnak a börtönében $N$ db cella van, amelyek 1-től kezdve egyesével számozottak, így az utolsó sorszáma $N$. Születésnapjára gyönyörű ajándékot kapott, így jókedvében elhatározta, hogy kiengedi őket, így elküldi az 1. szolgát, hogy nyissa ki minden cella ajtaját, de az őrök a biztonság kedvéért még nem engedték el a rabokat, hátha meggondolja magát a szultán.

Így is lett, a szultánnak nem tetszett a következő ajándék, és elküldte a 2. szolgát, hogy zárja be minden 2. cella ajtaját.

Aztán újra meggondolta magát, és elküldte a 3. szolgát, hogy minden 3. cella ajtaját nyissa ki, ha be volt zárva, és zárja be, ha ki volt nyitva.

Utána ment a 4. szolga, 5. szolga és folytatódott egészen a $N$. szolgáig, ha a $N$. cella nyitva van zárja be, ha zárva van, nyissa ki.

Írj programot, amely kiírja, hogy a végén mely ajtók maradnak nyitva, azaz mely rabok szabadulnak ki!

### Bemenet
A bemenetben egyetlen egész szám van: $N$ - a börtöncellák száma. 

### Kimenet
Írd ki, hogy a végén mely ajtók maradnak nyitva, azaz mely rabok szabadulnak ki!
A cellaszámokat egy sorban, növekvő sorrendben, szóközzel elválasztva írd ki.

### Korlátok
* $1 \le N \le 1000\,000\,000$

### 1. példa bemenet
    6

### 1. példa kimenet
    1 4

### Az 1. példa magyarázata
Az 1. szolga után mindegyik nyitva lesz: nyitva, nyitva, nyitva, nyitva, nyitva, nyitva

A 2. szolga után: nyitva, zárva, nyitva, zárva, nyitva, zárva

A 3. szolga után: nyitva, zárva, zárva, zárva, nyitva, nyitva

A 4. szolga után: nyitva, zárva, zárva, nyitva, nyitva, nyitva

Az 5. szolga után: nyitva, zárva, zárva, nyitva, zárva, nyitva

A 6. szolga után: nyitva, zárva, zárva, nyitva, zárva, zárva

Azaz az első és a negyedik cella lesz nyitva.

### 2. példa bemenet
    50

### 2. példa kimenet
    1 4 9 16 25 36 49
