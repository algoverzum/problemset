## Kaszinó
Egy távoli bolygón a helyiek szeretnek szerencsejátékozni, emiatt a kaszinóik tele vannak nyerőgépekkel. Minden gép egy zsetonnal működik. A helyiek azt hiszik, hogy a gépek véletlenszerűek, de neked sikerült megfejteteni a logikájukat! Ha egy `N` értékű zsetont helyezel be, a gép három zsetont ad ki: `N/2`, `N/3` és `N/4` értékben, mindegyik értéket lefelé kerekítve, ezzel biztosítva azt, hogy a kaszinók mindig előnyben legyenek.

Ezeket a zsetonokat a bolygó valutájára, az úgynevezett "Galaktikus Kreditre" is be lehet váltani, 1:1 arányban, de az átváltás után a valuta már nem használható zsetonok vásárlására.

A feladatod az, hogy túljárj a kaszinók eszén azzal, hogy kiszámolod a maximálisan megszerezhető Galaktikus Kreditek mennyiségét egy `N` értékű zsetonból.

### Bemenet
A bemenet első sora $T$ - a tesztesetek száma.
Minden teszteset egyetlen sorból áll, amely egy számot tartalmaz, $N$ - a kezdeti zseton értéke.

### Kimenet
Minden tesztesethez egyetlen számot írj ki, a zsetonból maximálisan megszerezhető Galaktikus Kreditek mennyiségét.

### Korlátok
* $1 \le T \le 100$
* $1 \le N \le 10^9$

### Példa bemenet
    2
    12
    2

### Példa kimenet
    13
    2

### Példa magyarázata
Az első tesztesetben behelyezheted a zsetont egy gépbe, mely három zsetont ad ki: 6, 4 és 3 értékben. Ezután beválthatod a zsetonokat és $6+4+3=13$ Galaktikus Kreditet kapsz értük.

A második tesztesetben, ha behelyezed a zsetont egy gépbe, 1, 0 és 0 értékű zsetonokat kapsz vissza. Innen nem szerezhetsz többet, mint 1 Galaktikus Kredit, ezért az eredeti zsetonodat jobban megéri 2 Galaktikus Kreditre váltani.