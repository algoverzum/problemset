## Gyár
Egy gyárban dolgozol felügyelőként, ahol robotokat szerelnek össze. Minden robot egy testből és páros számú végtagból áll, vagyis páratlan darab alkatrészre van szükség a megépítéséhez. Kapsz egy listát ami tartalmazza az egyes robotokhoz rendelt alkatrészek számát. Az a dolgod, hogy ha találsz egy robotot amihez páros számú alkatrészt rendeltek, mihamarabb értesítsd a gyárat a hibáról. Mivel gyorsan készülnek a robotok, sajnos nincs idő elküldeni az összes hibás robotot. Csak az első páros alkatrészű robot indexét várják tőled (0-tól kezdve a számozást). Ha nincs ilyen robot, akkor az eredmény $-1$ legyen. Írj egy függvényt ennek a feladatnak a teljesítésére!

### Sablon
Indulj ki az előre készített sablon kódból! Ne változtass a főprogramon semmit, mert különben nem lesz elfogadva. A `first_even` függvényt kell megírnod, ami paraméterként kapja a számokat tartalmazó sorozatot, és az első páros szám helyét adja vissza, 0-tól számozva.

### Korlátok
* $1 \le N \le 1000$, ahol $N$ a számsorozat mérete.
* A sorozat minden eleme $1$ és $1000$ között van.

### Példa
A (1 5 9 3 2 4) számsorban az először felbukkanó páros szám a 2, az 4. indexen.