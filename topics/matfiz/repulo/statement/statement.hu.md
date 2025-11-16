## Repülő
A repülő addig emelkedik, amíg a **sebessége** át nem lépi az $S$ értéket, **vagy** a **magasság** el nem éri az $M$ egységet.  
(Mindkettő legyen konstans: $S = 1000$, $M = 2000$.)

Közben:  
- a sebesség **2-vel nő** minden lépésben,  
- a magasság **4-gyel nő** minden lépésben.

A kezdőértékek ismeretlenek!  
Írj programot, amely:  
- beolvassa az aktuális sebességet és magasságot,  
- majd kiírja, hogy **hány lépésben száll fel a repülő!**

### Bemenet
A bemenetben első sorában egy egész szám van: $sebesseg$ - a repülő aktuális sebessége.  
A bemenet második sorában egy egész szám van: $magassag$ - az aktuális magassága.

### Kimenet
A kimenetben egyetlen szám van: **hány lépésben száll fel a repülő!**

### Korlátok
* $100 \le sebesseg \le 1000$  
* $100 \le magassag \le 2000$

### Példa bemenet
    880
    1201

### Példa kimenet
    60

### A példa magyarázata
A sebesség 2-vel, a magasság 4-gyel nő, azaz $882 1205$, majd $884 1209$, stb. lesz. $60$ lépésben lesz a $880$-ból $1000$. Elég, ha az egyik felső korlátot eléri a gép.
