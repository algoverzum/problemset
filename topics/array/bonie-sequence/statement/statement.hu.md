## Boni sorozat
A bonik érdekes állatok, $N$ évig élnek, és minden boni tud szülni egy kis bonit évente. Először két év után lesz kicsinyük, és ezt követően életük végéig évente egy-egy kis boninak adnak életet. Kezdetben egy újszülött bonim van. Meg tudod mondani, hogy az $N$ év alatt, amíg ő él, hogy alakul a bonijaim száma évente?

### Bemenet
A bemenetben egyetlen egész szám van: $N$ - az évek száma.

### Kimenet
$N + 1$ számot kell kiírnod egy sorban szóközzel elválasztva: $B_0, B_1, \ldots, B_N$, ahol $B_0=1$ és $B_i$ a bonik száma $i$ év elteltével.

### Korlátok
* $1 \le N \le 30$

### Példa bemenet
    5

### Példa kimenet
    1 1 2 3 5 8

### A példa magyarázata
Egy év után még csak egy boni van, de két év után születik egy új boni, így ketten lesznek. Három év után szintén egy boni születik, így 3 lesz a bonik száma. Négy év után már az elsőként született boni is szülni fog, így 2 új boni lesz, vagyis összesen 5. Öt év után már 3 boni lesz, amelyik legalább két éves, így 3 új boni születik, és összesen 8 lesz, és a történetnek itt van vége, mert ezután el fog pusztulni a legelső boni.

