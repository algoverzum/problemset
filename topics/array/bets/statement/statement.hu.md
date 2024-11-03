## Fogadások
Akiko barátom szeret űrfogathajtó versenyekre fogadni. Az elmúlt $N$ napban minden nap végén feljegyezte, hogy mennyi pénze van. Kíváncsi arra, hogy az egyes napokon mennyi pénzt nyert, azaz mennyivel változott a pénze az előző naphoz képest (ha csökkent a pénze, akkor az negatív nyeremény). Arra is kíváncsi, hogy az egyes napokon mennyivel nyert többet vagy kevesebbet az előző napnál, tehát a nyeremények közötti változásokat is ki szeretné számolni (ugyanúgy előjelesen, tehát ha csökkent a nyeremény, akkor a változás negatív). Tudsz segíteni neki ebben?

### Bemenet
A bemenet első sorában a napok száma van: $N$.
A következő sorban $N$ darab szám van, az egyes napok végén Akiko pénze: $A_1, A_2, \ldots, A_{N}$.

### Kimenet
Két sort kell kiírnod, mindkettőben a számokat szóközzel elválasztva.
Az első sorba $N-1$ számot írj, Akiko nyereményeit az egyes napokon a második naptól kezdve (az első nap előtti pénzéről nincs adat).
A második sorba $N-2$ számot kell írnod, a szomszédos nyeremények közötti változásokat.

### Korlátok
* $3 \le N \le 100$
* $1 \le A \le 10000$

### Példa bemenet
    6
    4 9 2 5 13 10

### Példa kimenet
    5 -7 3 8 -3
    -12 10 5 -11


### A példa magyarázata
A második nap a pénze 9 volt, az első nap pedig 4, így a második napon a nyereménye $9 - 4 = 5$. A harmadik napon 2-re csökkent a pénze, tehát 7-et bukott, így a nyereménye -7, stb.

A nyeremények közötti változások vannak a második sorban, például az első szám az 5 és -7 közötti változást adja meg, ami -12.
