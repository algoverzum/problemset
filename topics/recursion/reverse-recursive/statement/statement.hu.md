## Visszafelé Rekurzívan
A Jedi Tanács különleges próbát készített elő a fiatal Padawanok számára, hogy bizonyítsák, mennyire képesek uralni az Erőt. A Jedi Templom rejtett archívumaiban Yoda mester kihívást intéz hozzád: fordíts meg egy számokból álló sorozatot. A nehézség? Nem használhatsz tömböket (például listákat vagy vektorokat), csak az Erő tiszta áramlására támaszkodhatsz – azaz a **rekurzióra**.

### Bemenet
A bemenet minden sorában egy egész szám van: $V_i$.
Az utolsó sorban 0 van, és minden előtte lévő szám pozitív.

### Kimenet
Ugyanannyi sort kell kiírni mint amennyi a bemeneten van, minden sorba egy számot kell írni, a bemenetben lévő számokat fordított sorrendben (visszafelé).
Ne használj tömböt (vektort, listát, stb.)

### Korlátok
* $1 \le N \le 100$, ahol $N$ az input sorainak a száma.
* $1 \le V_i \le 10^9$, ahol $V_i$ az input $i$-edik sorában lévő szám.

### Példa bemenet
    1
    11
    7
    0

### Példa kimenet
    0
    7
    11
    1

### A példa magyarázata
Visszafelé kell kiírni a számokat... Ne használj tömböt (vektort, listát, stb.)
