## Maximális repülési magasságok
Van egy érdekes madár a bolygónkon, az *arboreon*, ami útmenti fák tetején él. Egy út mentén van $N$ fa, amelyek magasságai $H_1, H_2, \ldots, H_N$. $Q$ arboreon madár csücsül egyes fák tetején, mindegyikről még azt is tudjuk, hogy hány éves: az $i$-edik madár az $S_i$ sorszámú fa tetején van, és életkora $K_i$ év.

Mindegyik madár az életkorától függő darabszámú fa tetejét fogja meglátogatni táplálékot keresve, az induló pozíciójától kezdve egyesével sorrendben. Egy 0 éves madár nem megy sehova, így csak a kezdő fáját látogatja meg, egy 1 éves madár átmegy még a következőre, így két fát látogat meg, egy 2 éves madár négy fát látogat meg sorban, és így tovább, azaz egy $K$ éves madár $2^K$ fát látogat meg. Tehát az $i$-edik madár a következő sorszámú fáknak a tetejét látogatja meg: $S_i, S_i+1, \ldots, S_i+2^{K_i}-1$. Garantált, hogy egyik madár sem megy túl az $N$-edik fán.

Határozd meg minden madárra, hogy mi lesz a maximális magasság, amit meglátogat! Formálisan, minden $i$-re a következő értéket keresd meg: $max\{ H_j| S_i \le j < S_i+2^{K_i} \}$. 

### Bemenet
A bemenetben első sorában két egész szám van: $N$ és $Q$ - a fák és a madarak száma. A második sorban $N$ szám van, az egyes fák magasságai ($H_1, H_2, \ldots, H_N$). Ezt követően $Q$ sorban két-két szám található: $S_i$ és $K_i$ - az $i$-edik arboreon madár kezdő pozíciója és életkora. 

### Kimenet
$Q$ számot kell kiírnod külön sorokba, az $i$-edik sorba az $i$-edik madár által meglátogatott legmagasabb fa magassága kerüljön. 

### Korlátok
* $1 \le N \le 100\,000$
* $1 \le Q \le 300\,000$
* $1 \le H_i \le 10^9$ $(i = 1, 2, \ldots, N)$
* $1 \le S_i \le N$ $(i = 1, 2, \ldots, Q)$
* $0 \le K_i \le 17$ $(i = 1, 2, \ldots, Q)$
* $1 \le S_i + 2^{K_i} \le N$ $(i = 1, 2, \ldots, Q)$


### Példa bemenet
    9 4
    13 42 7 9 1 25 7 1 2
    2 1
    4 2
    1 3
    9 0

### Példa kimenet
    42
    25
    42
    2

### A példa magyarázata
Az első madár a második és harmadik fát látogatja meg, a magasságaik: 42, 7, ezek közül a legnagyobb a 42.

A második madár által meglátogatott fák magasságai: 9, 1, 25, 7, a legnagyobb a 25.

A harmadik madár által meglátogatott fák magasságai: 13, 42, 7, 9, 1, 25, 7, 1, a legnagyobb a 42.

A negyedik madár csak az utolsó fát látogatja meg, amely magassága 2.

