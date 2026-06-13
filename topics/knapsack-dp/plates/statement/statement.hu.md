## Tányérok
Dr. Patelnak $N$ darab tányéroszlopa van. Minden oszlopban $K$ tányér található. Minden tányérhoz tartozik egy **szépségérték** (pozitív egész szám), amely megmutatja, mennyire szép.

Dr. Patel pontosan $P$ tányért szeretne kiválasztani a vacsorához úgy, hogy a kiválasztott tányérok összes szépségértéke a lehető legnagyobb legyen.

**Fontos szabály:**  
Ha egy oszlopból ki szeretne venni egy tányért, akkor az összes fölötte lévő tányért is ki kell vennie. Vagyis egy oszlopból csak a tetejétől kezdve választhat ki tányérokat.

### Bemenet
Az első sor a tesztesetek számát tartalmazza: $T$.  
Minden teszteset első sora három egész számot tartalmaz:

* $N$ – a oszlopok száma,
* $K$ – az egy oszlopban lévő tányérok száma,
* $P$ – a kiválasztandó tányérok száma.
 
Ezután $N$ sor következik.

* Az $i$-edik sor $K$ darab egész számot tartalmaz, amelyek az adott kupac tányérjainak szépségértékeit adják meg **felülről lefelé**.

### Kimenet
Minden tesztesetre írd ki a maximálisan elérhető összes szépségérték, tesztesetenként új sorba.

### Korlátok
* $1 \le T \le 10$
* $1 \le K \le 30$
* $1 \le N \le 50$
* $1 \le P \le N\cdot K$
* A szépségértékek 1 és 100 között vannak (beleértve az 1-et és a 100-at is).

### Példa bemenet
    2
    2 4 5
    10 10 100 30
    80 50 10 50
    3 2 3
    80 80
    15 50
    20 10

### Példa kimenet
    250
    180

### A példa magyarázata
1. teszteset: 5 tányért kell választani. Az első kupacból a felső 3 tányért: $10 + 10 + 100 = 120$. A második kupacból a felső 2 tányért: $80 + 50 = 130$. Összesen: $120 + 130 = 250$

2. teszteset: 3 tányért kell választani. Az első kupacból a felső 2 tányért: $80 + 80 = 160$. A második kupacból semmit. A harmadik kupacból az első tányért: $20$. Összesen: $160 + 20 = 180$
