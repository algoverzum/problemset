## Termek kihasználtsága
Egy kisebb egyetem kis kampusza számára fejlesztünk alkalmazást, mely egy adott épület termeinek kihasználtságáról tárol adatokat és készít statisztikákat. Az épületnek E emelete van, minden emeletén N darab terem található, melyek befogadóképessége $K$ fő. (Minden teremnek egyforma a kapacitása.) Ismerjük minden teremnek az aktuális létszámadatát ($T_{i,j}$).
Írj olyan programot, amely megadja annak a szintnek a számát, ahol a termek kihasználtságának (aktuális létszám osztva $K$-val, százalékban, egész számként) az átlaga a legkisebb, valamint a megadott szinten a termek aktuális foglaltságát növekvő sorrendbe rendezve! Az osztás esetében az egész osztást kell használni, azaz tört esetében az egész részt tároljuk. 

### Bemenet
Az első sorban $E$ és $N$ és $K$ értéke van. A következő E sor N darab számot tartalmaz, az egyes termek aktuális létszámadatát ($T_{i,j}$.

### Kimenet
A kimenet első sorába írasd ki annak a szintnek a számát, amelynél a termek kihasználtságának az átlaga a legkisebb, alá pedig a szinten lévő termek aktuális létszámadatait a kihasználtság szerint növekvő sorrendben. 

### Korlátok
* $2 \leq E \leq 20.$
* $2 \leq N \leq 10.$
* $15 \leq K \leq 100.$
* $0 \leq T_{i,j} \leq K.$

### Példa bemenet
    4 5 40
    25 30 22 25 30
    20 30 22 25 10
    25 30 22 25 34
    0 15 16 12 12

### Példa kimenet
    4
    0 12 12 15 16

### A példa magyarázata
A 4. emeleten lévő termek kihasználtsága a legkisebb. Az egyes termek aktuális létszámadatai a 4. emeleten, növekvő sorrendben: 0 12 12 15 16.