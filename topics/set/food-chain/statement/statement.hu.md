## Tápláléklánc
Egy idegen bolygón biológiai felmérést végeztünk, ún. táplálkozási párokat azonosítottunk (mi
eszik mit?). E párok száma legfeljebb 30. A növények nem esznek semmilyen élőlényt, az állatok
pedig vagy növényeket, vagy más állatokat esznek. A táplálkozási pár jelentése: az elsőnek megadott eszi a másodiknak megadottat, pl. "róka eszi fogoly", "csiga eszi fű".
Írj programot, amely a táplálkozási párok közül megadja azoknak az állatoknak a nevét, amelyek
esznek állatot (és esetleg növényt is)! Figyelem: ami nem eszik semmit, az növény.


### Bemenet
A standard bemenet első sora a táplálkozási párok számát tartalmazza (1≤N≤30). A következő N sor mindegyikében egy-egy táplálkozási pár van megadva két szóközzel elválasztott szó
formájában. Az első szóban megadott élőlény eszi meg a másodikban megadottat. A táplálkozási
párokban szereplő nevekben csak ékezet nélküli betűk lehetnek.

### Kimenet
A standard kimenet első sora azon állatok számát tartalmazza, amelyek esznek állatot (és
esetleg növényt is)! A következő sorokba ezeket az állatokat kell kiírni soronként, ábécé sorrendben! Ha a megadott táplálkozási láncban nincs ilyen állat, akkor egyedül a 0-t kell a kimenetre
írni!


### Korlátok
* $1 \le N \le 30$<br>
Az élőlények nevei az angol ábécé kisbetűiből állnak és legfeljebb 100 karakter hosszúak.

### Példa bemenet
    7
    fox partridge 
    fox blackbird
    partridge  worm
    snail grass
    blackbird snail
    worm roots 
    blackbird seeds
    
### Példa kimenet
    3
    blackbird
    fox
    partridge

### A példa magyarázata
    A feketerigó csigákat eszik, amelyek állatok, mert füvet esznek. Tehát a feketerigó egy állat, amelyik állatot eszik.
    A róka megeszi a partifecskét és a feketerigót, amelyek mindketten állatok. Tehát a róka is állatevő állat.
    A fogoly gilisztákat eszik, amelyek gyökereket esznek. Tehát a fogoly is állat, amelyik állatot eszik.
