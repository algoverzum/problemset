## Egyensúly
A Csillagkapu Parancsnokság egy különös számsorozatra bukkant egy idegen bolygóról érkezett üzenetben. Ez nem tűnik véletlenszerű kódnak, bizonyos számok egyensúlyban állnak: értékük megegyezik a közvetlen szomszédaik átlagával.

Ki tudnád válogatni ezeket az egyensúlyban álló számokat? A sorrendjükön ne változtassál!

### Bemenet
A bemenet első sorában egy szám van: $N$, az üzenetben szereplő számok száma.<br>
A következő sorban $N$ darab szám van, az üzenetben szereplő számok: $A_1, A_2, \ldots, A_{N}$.

### Kimenet
Azokat a számokat kell kiírnod szóközzel elválasztva, amelyek megegyeznek a szomszédjaik átlagával.

### Korlátok
* $1 \le N \le 10000$
* $1 \le A_i \le 1000$

### Példa bemenet
    8
    1 4 7 11 10 8 6 10

### Példa kimenet
    4 8

### A példa magyarázata
Mivel $\frac{1+7}{2}=4$ és $\frac{10+8}{2}=8$, erre a két számra teljesül a feltétel. Másra nem, például  $\frac{4+11}{2}\not=7$.
