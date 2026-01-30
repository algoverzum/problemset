## X túlsúly
Lili egy fiatal tündér, akinek nagyon fontos az "x" betű. Lili egy $s$ nevű varázsszót kapott. Ő jónak nevez egy szót, ha a szó karaktereinek több mint a fele "x" betű. Például az "xxbxx", "axxx" jó szavak, de a "bxcx", "xvvvx", vagy az üres szó ("") nem jó.

Lili törölhet néhány karaktert az $s$ szóból. Arra kíváncsi, hogy néhány karakter (esetleg semmi) eltávolítása után mi lehet a leghosszabb jó szó, amit így kap. Garantált, hogy a szóban legalább egy "x" betű van, tehát mindig létezik legalább egy jó megoldás.

### Bemenet
Az első sorban egy $s$ string található, amely kisbetűs angol betűkből áll.
Garantált, hogy az $s$ string legalább egy "x" betűt tartalmaz.

### Kimenet
Írd ki egyetlen egész számként a leghosszabb jó szó hosszát, amelyet Lili kaphat, miután néhány (akár nulla) karaktert eltávolított az $s$-ből.

### Korlátok
* $1 \le |s| \le 100$
* Garantált, hogy a szóban legalább egy "x" betű van.

### 1. Példa bemenet
    axaaaax

### 1. Példa kimenet
    3

### Az 1. példa magyarázata
Az első példában elég, ha bármelyik négy "a"-t kitöröljük. A válasz 3, mivel ez a maximálisan megmaradó karakterek száma.

### 2. Példa bemenet
    xxxbxx

### 2. Példa kimenet
    6

### A 2. példa magyarázata
A második példában egyetlen karaktert sem kell törölnünk.
