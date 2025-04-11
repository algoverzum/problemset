## Leghosszabb tükörszó
A Csillagflotta egy kódolt üzenetet kapott. A dekódoláshoz az első lépés: azonosítani a leghosszabb tükörszót (palindrómot) a kódolt üzenetben. Egy tükörszó balról és jobbról olvasva is azonos. Az üzenetből tetszőleges betűk elhagyásával is létrejöhet!

### Bemenet
A bemenetben egyetlen sorában egy string van: $S$ - a kódolt üzenetet.

### Kimenet
Egyetlen számot kell kiírnod, a kódolt üzenetben található leghosszabb tükörszó hosszát. 

### Korlátok
* $1 \le |S| \le 1000$
* $S$ angol kisbetűket tartalmaz

### Példa bemenet
    abrakadabra

### Példa kimenet
    7

### A példa magyarázata
Egy lehetséges 7 hosszú tükörszó (piros): <span style="color:red">ab</span>r<span style="color:red">aka</span>da<span style="color:red">b</span>r<span style="color:red">a</span>
