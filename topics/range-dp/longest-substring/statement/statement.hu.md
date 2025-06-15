## Leghosszabb substring
Az Enterprise kétszer is megkapta ugyanazt az üzenetet ($A$, $B$), de mindkét alkalommal az eredeti üzenet torzult. A feladat az, hogy meghatározzuk a leghosszabb összefüggő közös rész (substring) hosszát. Ez az információ segíthet az üzenetekben keletkezett hibák mértékének felmérésében.

### Bemenet
A bemenetben első sorában egy string van: $A$ - az első üzenet.
A bemenetben második sorában egy string van: $B$ - a második üzenet.

### Kimenet
Egyetlen számot kell kiírnod, a két üzenetben szereplő leghosszabb közös substring hosszát.

### Korlátok
* $1 \le |A|,|B| \le 2500$, vagyis mindkét string hossza legfeljebb $2500$.
* Mindkét string csak az angol ábécé kisbetűit tartalmazza.

### Példa bemenet
    ancientlanguagesx
    modernlanguagesy

### Példa kimenet
    9

### A példa magyarázata
A legosszabb összefüggő közös rész: "languages".
