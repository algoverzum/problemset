## Grow Bigger
A bolygónk állatvilágának tanulmányozása közben a kutatók a brumara kettő különböző alfaját találták meg, amit A és B típusú brumarának neveztek el. Az A típusú brumarák kisebb súllyal születnek, viszont gyorsabban növekednek, míg a B típus nagyobb súllyal születik, viszont lassabban növekszik.
Egy A típusú brumara egy év alatt megháromszorozza a saját súlyát, míg egy B típusú megduplázza a magáét. Segíts a kutatóknak megállapítani, hogy a vizsgált újszülött brumarák közül az A típusú hány év alatt fogja túlnőni a B típusút.

### Bemenet
A bemenet kettő sorból áll. Az első sor egyetlen számot tartalmaz, az A típusú brumara súlyát: $A$. A második sor egyetlen számot tartalmaz, a B típusú brumara súlyát: $B$.

### Kimenet
Egyetlen számot kell kiírnod, azoknak az éveknek a számát, aminek elteltével az A típusú brumara szigorúan nehezebb lesz mint a B típusú.

### Korlátok
* $1 \le A \le B \le 10$

### Példa bemenet
    4
    7

### Példa kimenet
    2

### A példa magyarázata

Egy év elteltével a brumarák súlya így fog kinézni: A = 4 * 3 = 12, B = 7 * 2 = 14. Ekkor még az A típus nem nőtte túl a B típust, így várunk még egy évet. A második évre ez így fog változni: A = 12 * 3 = 36, B = 14 * 2 = 28. Ekkor már az A típus szigorúan nehezebb, mint a B, ezért 2 évet kell kiírnunk.

### 2. példa bemenet
    4
    9

### 2. példa kimenet
    3

### A példa magyarázata
Két év után mindkét brumara súlya 36 lesz, így a harmadik év után lesz előszőr szigorúan nehezebb az A típusú.