## Kisebbek száma
Űrhajó reaktorokon futtatunk végre biztonsági teszteket. Az egyik fázisban azt teszteli a fedélzeti számítógép, hogy hány reaktor üzemel egy bizonyos terheltség alatt. Írj egy függvényt, amely képes egy listában tárolt terheltségi szintek között megszámolni, hogy hány van egy megadott határ alatt.

### Sablon
Indulj ki az előre készített sablon kódból! Ne változtass a főprogramon semmit, mert különben nem lesz elfogadva. A `count_lower` függvényt kell megírnod, ami paraméterként kapja a számokat tartalmazó sorozatot és a korlátot, és a korlát alatti elemek számát adja vissza.

### Korlátok
* $1 \le N \le 100$, ahol $N$ a számsorozat mérete.
* $1 \le M \le 10000$, ahol $M$ a megadott határ
* A sorozat minden eleme $1$ és $10000$ között van.

### Példa
A (6 3 4 1 2) számsorból az 1, a 2 és a 3 kisebb mint a megadott 4-es korlát, így a válasz az, hogy 3.
