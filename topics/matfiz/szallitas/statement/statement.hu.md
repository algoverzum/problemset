## Szállítás

Egy raktárban $N$ darab tárgy van egymás után sorba rendezve. Minden tárgynak ismert a súlya.

A raktárból legfeljebb $K$ kamionnal kell elszállítani tárgyakat. Minden kamion azonos $S$ kapacitású, azaz egy kamionra kerülő tárgyak összsúlya nem haladhatja meg $S$-t.

A rakodás szabálya:

* tárgyakat balról jobbra haladva kell feldolgozni,
* minden tárgyat pontosan egy kamionra kell felrakni,
* egy kamionra csak **folyamatos szakasz** kerülhet,
* a kamionok sorrendben töltődnek.

Feladat: határozzuk meg, hogy legfeljebb hány tárgyat tudunk elszállítani a sor elejétől kezdve a $K$ kamion felhasználásával.

### Bemenet
A standard input első sorában 3 szám van. A tárgyak száma ($N$), a kaminonok száma ($K$) és a kapacitás ($S$)
A következő sorban a tárgyak súlya szerepel ($a_i)$. 

### Kimenet
A standard kimenet első és egyetlen sorába a legtöbb elszállítható tárgy száma kerüljön

### Korlátok
* $N$ ($1 \le N \le 10\,000$) – tárgyak száma
* $K$ ($1 \le K \le 100$) – kamionok száma
* $S$ ($1 \le S \le 1000$) – kapacitás
* $a_1, a_2, \dots, a_N$ ($1 \le a_i \le S$) – tárgyak súlya

### Példa bemenet
    8 3 100
    20 70 10 30 80 60 50 30

### Példa kimenet
    5

### A példa magyarázata
A sor elejétől kezdve legfeljebb 5 tárgyat tudunk elszállítani:
* 1. kamion: 20 + 70 + 10 = 100
* 2. kamion: 30
* 3. kamion: 80

A következő (6.) tárgy súlya 60, ami már egy újabb (4.) kamiont igényelne, de legfeljebb 3 kamionunk van. Így a maximálisan elszállítható tárgyak száma a sor elejétől: 5.

### Hint 1
Ha $X$ tárgy elszállítható a sor elejétől, akkor minden $Y \le X$ tárgy is biztosan elszállítható. Ez monotonitást biztosít, ami lehetővé teszi a bináris (parametrikus) keresést a darabszámra.

### Hint 2
Egy feltételezett $X$ érték ellenőrzésekor (a döntési függvényben) elegendő kizárólag a legelső $X$ darab tárgyat vizsgálni a tömb elejétől kezdve.

### Hint 3
A döntési függvényben egy kamiont mindig addig töltünk balról jobbra haladva, amíg a következő tárgy súlyával együtt sem lépjük túl a kamion $S$ kapacitását. Ha túlglépnénk, új kamiont kell indítanunk.

### Hint 4
Az eldöntés $O(X)$ időben megválaszolható egyetlen lineáris bejárással (szimulációval). Ezt a függvényt hívjuk meg a bináris keresés minden lépésében, így a teljes algoritmus futásideje $O(N \log N)$ lesz.
