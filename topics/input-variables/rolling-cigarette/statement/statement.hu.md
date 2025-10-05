## Cigaretta sodrás
Buta Bácsi dohányzik. Olyan "hagyományos" dohányos, aki a dohányt tartalmazó papír csövecskébe tölti a dohányt. Minden cigarettából megadott hosszúságú rész megmarad (csikk). A dohányos vásárolt $N$ darab kész cigarettát, amelyek hossza azonos ($hossz$), mindegyikből megmarad néhány cm (ugyanannyi) $csikk$. Miután elszívta az összes cigarettát, a dohányt kiszórja, és belőlük új cigarettákat tölt ("sodor"). Ezeket is elszívja.

Hány cigaretta  szívott el összesen, és hány cm-re elég dohány maradt összesen a végén?

### Bemenet
A bemenet első sorában egyetlen egész szám van: $N$, a kezdetben vásárolt cigaretták száma.  
A bemenet második sorában is egyetlen egész szám van: $hossz$, a cigaretták hossza.  
A bemenet harmadik sorában egyetlen egész szám van: $csikk$, a csikk hossza.  
Mindhárom szám egész.

### Kimenet
Két számot kell kiírnod szóközzel elválasztva, az elszívott cigaretták számát, és a legvégén megmaradt dohány hosszát.

### Korlátok
* $1 \le N \le 100$
* $1 \le csikk < hossz \le 20$

### Példa bemenet
    20
    12
    2

### Példa kimenet
    23 10

### A példa magyarázata
20 cigaretta elszívása után 20 darab 2 cm-es csikk marad. Ezekből 40 cm kijönne, azaz 3 teljes cigaretta, és 4 cm maradék. A három cigarettából is marad meg 3 darab 2 cm-es csikk. Azaz összesen 23 cigarettát szívott el, és 10 cm-nyi dohány maradt.