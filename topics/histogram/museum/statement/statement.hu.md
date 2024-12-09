## Múzeum
Egy múzeumban $N$ napon át $M$ őr teljesít szolgálatot. Ismerjük mindegyikről annak a két napnak a sorszámát, amelyek között folyamatosan szolgálatban volt.

Írj programot, amely megadja a leghosszabb sorozat első és utolsó napját, amikor kettőnél kevesebb őr volt szolgálatban!

### Bemenet
A bemenetben első sorában két szám van: $N, M$ - a napok és az őrök száma.
A következő $M$ sorban két szám van: $F_i, L_i$ - az $i$. őr első és utolsó munkanapjának a sorszáma.

### Kimenet
Egyetlen sorba a leghosszabb sorozat első és utolsó napját kell kiírni, amikor kettőnél kevesebb őr volt szolgálatban! Ha több ilyen volt, akkor a legkisebb első napút, ha nem volt ilyen, akkor egy 0-t kell kiírni!

### Korlátok
* $1 \le N \le 1000$
* $1 \le M \le 1000$
* $1 \le F_i \le U_i \le M$ minden $1 \le i \le M$-re.

### 1. Példa bemenet
    6 5
    1 3
    6 6
    1 2
    2 3
    3 4

### 1. Példa kimenet
    4 6

### Az 1. példa magyarázata
Az első nap 2, a második nap 3, a harmadik nap 3, a negyedik nap 1, az ötödik nap 0 végül a hatodik nap 1 őr volt szolgálatban. Azaz a negyedik és a hatodik nap között volt 2-nél kevesebb őr szolgálatban.

### 2. Példa bemenet
    10 10
    8 10
    4 5
    2 3
    7 10
    1 8
    5 9
    1 3
    6 7
    5 6
    6 10

### 2. Példa kimenet
    0

