## Kamionok
Egy szállítmányozó cégnek $N$ darab rakományt kell elszállítania.
A rakományokat a megadott sorrendben kell felrakni a kamionokra, a sorrend nem változtatható meg.
A cég legfeljebb $K$ darab kamiont használhat. Minden kamion azonos kapacitású.
Határozzuk meg a legkisebb olyan kapacitást, amely mellett az összes rakomány elszállítható!

### Bemenet
A standard bemenet első sora két egész számot tartalmaz:
* $N$ -- a rakományok száma,
* $K$ -- a rendelkezésre álló kamionok száma.

A második sor $N$ darab pozitív egész számot tartalmaz, a rakományok tömegét: $t_1,t_2,\ldots,t_N$

### Kimenet
A minimálisan szükséges kamionkapacitást kell kiírni.

### Korlátok
* $1 \le N \le 100\,000$
* $1 \le K \le N$
* $1 \le t_i \le 10^9$

### Példa bemenet
    5 3
    10 20 30 40 50

### Példa kimenet
    60

### A példa magyarázata
A kapacitás legyen 60. Ekkor az egyik lehetséges felosztás:

10 + 20 + 30 = 60
40
50

Három kamion elegendő. Ha ismerjük a kamionok kapacitását, meg tudjuk mondani, hogy elegendő-e.

### Hint 1
A prioritási sor tetején mindig a legnagyobb prioritású elem található.

### Hint 2
A rakományokat sorrendben kell feldolgozni.

### Hint 3
Mindig addig pakoljunk egy kamionba, amíg még elfér a következő rakomány.

### Hint 4
A kapacitásra bináris keresést alkalmazhatunk.
