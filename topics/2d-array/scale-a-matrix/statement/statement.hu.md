## Vulkáni tea árak
Spock egy összejövetelt akar szervezni, ahová meghívja $K$ tiszttársát, és mindegyikük számára biztosít egy-egy adag vulkáni teát. Már csak ki kell választania a találkozó helyszínét és időpontját. Az Egyesült Föderáció adatbázisából $N$ lehetséges űrállomás jöhet szóba, és Spock ismeri minden helyszínen az italok árát a következő $M$ csillagnapra előre.

Ezeket az árakat egy $T$ táblázat tartalmazza, ahol az $i$-edik sor $j$-edik eleme, $T_{i,j}$ azt mutatja, hogy az $i$-edik helyszínen a $j$-edik csillagnapon egy adag vulkáni tea mennyibe kerül.

Spock szeretné látni, hogy az egyes helyszíneken és időpontokban összesen mennyibe fog kerülni $K$ adag ital, hogy a logikus döntést hozhassa meg. Tudnál neki egy $S$ táblázatot készíteni, amelyben $S_{i,j}$ azt mutatja meg, hogy az $i$-edik helyszínen a $j$-edik csillagnapon $K$ adag tea összesen mennyibe fog kerülni?

### Bemenet
Az első sor két egész számot tartalmaz, $N$ (űrállomások száma) és $M$ (csillagnapok száma).
Ezt követi a $T$ táblázat, vagyis a következő $N$ sor mindegyike egyenként $M$ egész számot tartalmaz, amelyek egy-egy adag vulkáni tea árát adják meg a különböző helyszíneken és időpontokban.
Az utolsó sorban egy egész szám van: $K$, Spock tiszttársainak száma.

### Kimenet
Írd ki a fent leírt $S$ táblázatot, azaz a $K$ adag ital árát az egyes helyszíneken és időpontokban.

### Korlátok
* $1 \le N, M \le 10$
* $1 \le K \le 100$
* $1 \le T_{i,j} \le 100$

### Példa bemenet
    3 4
    1 3 2 5
    7 6 4 8
    2 9 1 4
    2


### Példa kimenet
    2 6 4 10
    14 12 8 16
    4 18 2 8
