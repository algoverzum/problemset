## Pingpong meccs hossza
A pingpong meccsek bolygónkon nagyon sokáig tarthatnak, különösen, ha többkezes lények játszanak több ütővel. Egy pingpong mérkőzés kezdő és befejező időpontja a következő formátumban adott:

    H
    M

Itt $H$ és $M$ egész számok, amelyek az órát és a percet jelölik 24 órás időformátumban. A számok elején nincsenek nullák, például ha a kezdési időpont 13:05, akkor a bemenetben `13` és `5` szerepel.

Határozd meg a pingpong mérkőzés hosszát percben. Feltételezhető, hogy a meccs ugyanazon a napon ért véget, amikor elkezdődött, és legalább egy percig tartott, tehát a befejezési idő nagyobb, mint a kezdési idő. Egy óra 60 perc.

### Bemenet
A bemenet négy egész számot tartalmaz külön sorokban: $SH, SM, EH, EM$ - a pingpong meccs kezdő órája, kezdő perce, befejező órája és befejező perce.


### Kimenet
Egyetlen számot írj ki, a pingpong meccs hosszát percben.

### Korlátok
* $0 \le SH, EH \le 23$
* $0 \le SM, EM \le 59$

### Példa bemenet
    9
    59
    13
    5

### Példa kimenet
    186

### A példa magyarázata
A pingpongmérkőzés 9:59-kor kezdődik és 13:05-kor ér véget, tehát 3 óra 6 percig, azaz 186 percig tart.
