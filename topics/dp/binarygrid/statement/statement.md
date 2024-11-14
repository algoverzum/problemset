Adott egy $A$ táblázat, amely $N$ sorból és $M$ oszlopból áll, és csak
$0$-t és $1$-et tartalmaz. A sorokat és oszlopokat $0$-tól indexeljük. A
következő műveleteket végezhetjük el $A$-n:

-   Választunk egy $i$ indexet ($0 \le i \le N - 1$), és az $i$-edik
    sort invertáljuk (azaz a sorban minden $0$-ból $1$, és minden
    $1$-ből $0$ lesz).

-   Választunk egy $j$ indexet ($0 \le j \le M - 1$), és a $j$-edik
    oszlopot invertáljuk (azaz az oszlopban minden $0$-ból $1$, és
    minden $1$-ből $0$ lesz).

Egy táblázat akkor **szép**, ha nincs három egymást követő egyenlő érték
ugyanabban a sorban, illetve oszlopban. Formálisabban: nincs olyan
$i, j$ ($0 \le i \le N - 1, 0 \le j \le M - 3$), hogy
$A_{i, j} = A_{i, j + 1} = A_{i, j + 2}$, és nincs olyan $i, j$
($0 \le i \le N - 3, 0 \le j \le M - 1$), hogy
$A_{i, j} = A_{i + 1, j} = A_{i + 2, j}$.

A feladatunk az, hogy eldöntsük, lehet-e az adott táblázatot széppé
tenni, és ha igen, akkor megmondjuk az ehhez szükséges minimális
műveletszámot.

::: warning
Az értékelő rendszerből letölthető csatolmányok közt találhatsz
`binarygrid.*` nevű fájlokat, melyek a bemeneti adatok beolvasását
valósítják meg az egyes programnyelveken. A megoldásodat ezekből a
hiányos minta implementációkból kiindulva is elkészítheted.
:::

A bemenet első sora egyetlen egész számot tartalmaz, a tesztesetek $T$
számát.

Ezután $T$ teszteset következik, mindegyik előtt egy üres sor.

Minden egyes teszteset a következő sorokból áll:

-   egy sor, amely két szóközzel elválasztott egész számot tartalmaz,
    $N$-et és $M$-et, a táblázat sorainak és oszlopainak a számát,

-   további $N$ sor, melyek mindegyike $M$ darab `0` vagy `1` számjegyet
    tartalmaz, a táblázat egy sorának elemeit. Az $i$-edik sor $j$-edik
    számjegye az $A_{i-1,j-1}$ értéket határozza meg.

Mind a $T$ tesztesetre egyetlen egész számot kell kiírni (összesen $T$
sor lesz). Ha a táblázatot széppé lehet változtatni, akkor az ehhez
szükséges minimális műveletszámot, ellenkező esetben, ha ez lehetetlen,
akkor a `-1`-et írd ki.

-   $1 \le T \le 100$.

-   $1 \le N \le \constraints{MAXN}$.

-   $1 \le M \le \constraints{MAXM}$.

-   $A_{i, j}$ (a táblázat $i$-edik sorának $j$-edik eleme) $0$ vagy $1$
    minden $i = 0\ldots N-1$ és $j = 0\ldots M-1$ esetén.

-   Az $N$ értékek összege az összes tesztesetben legfeljebb $2000$.

-   Az $M$ értékek összege az összes tesztesetben legfeljebb $2000$.

A megoldásodat sok különböző tesztesetre lefuttatjuk. A tesztesetek
részfeladatokba vannak csoportosítva. Egy-egy részfeladatot akkor
tekintünk megoldottnak, ha volt legalább egy olyan beadásod, amely az
adott részfeladat minden tesztesetére helyes megoldást adott. A feladat
összpontszámát a megoldott részfeladatokra kapott pontszámok összege
adja.

::: example
:::

Az **első példában** egy lehetséges módja annak, hogy a táblázatot 3
művelet segítségével széppé tegyük:

-   Invertáljuk a $0$. oszlopot.

-   Invertáljuk a $2$. sort.

-   Invertáljuk az $1$. oszlopot.

Igazolható, hogy 2 művelet nem elég.

A **második példában** a táblázat már szép, így nincs szükség
műveletekre.

A **harmadik példa** esetében a táblázatot nem lehet az említett
műveletekkel széppé tenni.
