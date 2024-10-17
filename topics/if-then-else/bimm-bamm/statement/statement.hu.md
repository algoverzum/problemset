## Bimm, bamm, bumm
Az itteni gyerekek szeretik a következő játékot játszani a számokkal: hangosan mondják a számokat 1-től kezdődő sorrendben, de néha az aktuális számot helyettesíteniük kell egy szóval. Konkrétan:

* ha az aktuális szám a 3 többszöröse, akkor azt kell mondaniuk, hogy `bimm`,

* ha a szám az 5 többszöröse, akkor azt kell mondaniuk, hogy `bamm`,

* és ha egyaránt a 3 és az 5 többszöröse is, akkor `bumm`-ot kell mondaniuk
a szám helyett.

A bemenetben van egy szám, ami az aktuális szám a játékban. Írd ki a szót, amit a gyerekeknek ki kell mondaniuk, vagy magát a számot, ha nem kell helyettesíteniük.

### Bemenet
A bemenetben egyetlen egész szám van: $N$ - az aktuális szám 


### Kimenet
Írd ki, hogy mit kell a gyerekeknek mondaniuk, magát a számot, vagy a `bimm`/`bamm`/`bumm` szót a 3-mal és 5-tel való oszthatóság alapján.  

### Korlátok
* $1 \le N \le 100$

### Példa bemenet
    7

### Példa kimenet
    7

### Második példa bemenet
    5

### Második példa kimenet
    bamm

### A példa magyarázata
A 7 nem többszöröse sem a 3-nak sem az 5-nek, ezért a gyerekeknek magát a számot kell kimondaniuk. Az 5 többszöröse az 5-nek, de a 3-nak nem, ezért azt kell mondaniuk, hogy `bamm`.


