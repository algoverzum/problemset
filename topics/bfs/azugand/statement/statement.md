Azugand, a Prahovand-völgy híres városa sajátos úthálózatáról ismert:
$N$ kereszteződése van, amelyek $1$-től $N$-ig vannak számozva, és
mindegyiknek van egy $V_i$ hozzárendelt értéke. Két különböző
kereszteződés között akkor és csak akkor van utca, ha értékeik
bitenkénti ÉS-e nem nulla.

Formálisan, adott egy $N$ csúcsú gráf, amelynek minden egyes csúcsához
egy $V_i$ értéket rendeltünk. Két különböző, $i$ és $j$ csúcs között
akkor és csak akkor van él, ha $V_i \ \& \ V_j \neq 0$.

![Üdv Azugand városában!](azugand.jpg){width="60%"}

Egy ismert fiú a völgyből, Andrei egy táblázatot szeretne készíteni
bizonyos pontok közötti legrövidebb távolságokról, de a sok számolás
túlzottan leterhelhi, ezért a segítségedet kéri! Adott $Q$ lekérdezés,
mindegyikben egy-egy $cost(X, Y)$ értékeket kell kiszámítanod. A
$cost(X, Y)$ a gráfban az $X$ és $Y$ csúcsok között a legrövidebb úton
lévő **élek** száma. Ha az $X$ csúcsból nem tudjuk elérni az $Y$
csúcsot, akkor a $cost(X, Y)$ értéke $-1$.

::: warning
Az értékelő rendszerből letölthető csatolmányok közt találhatsz
`azugand.*` nevű fájlokat, melyek a bemeneti adatok beolvasását
valósítják meg az egyes programnyelveken. A megoldásodat ezekből a
hiányos minta implementációkból kiindulva is elkészítheted.
:::

A bemenet első sorában két egész szám van: $N$ és $Q$, a gráf csúcsainak
száma, illetve a lekérdezések száma.

A második sorban $N$ egész szám van: $V_1, V_2, \dots, V_N$, a gráf
csúcsaihoz rendelt értékek.

A következő $Q$ sor mindegyike két-két különböző egész számot tartalmaz:
$X_i$-t és $Y_i$-t, két csúcs azonosítóját, amelyekre ki kell számolni a
$cost(X_i, Y_i)$ értéket.

$Q$ egész számot írj ki, mindegyiket külön sorban: a $cost(X_i, Y_i)$
értéket minden egyes lekérdezéshez.

-   $1 \le N \le \constraints{MAXN}$.

-   $1 \le Q \le \constraints{MAXQ}$.

-   $0 \le V_i < 2^{\constraints{MAXB}}$ minden $i = 1\ldots N$ -re.

-   $1 \le X_i \neq Y_i \le N$ minden $i = 1\ldots Q$-ra.

A megoldásodat sok különböző tesztesetre lefuttatjuk. A tesztesetek
részfeladatokba vannak csoportosítva. Egy-egy részfeladatot akkor
tekintünk megoldottnak, ha volt legalább egy olyan beadásod, amely az
adott részfeladat minden tesztesetére helyes megoldást adott. A feladat
összpontszámát a megoldott részfeladatokra kapott pontszámok összege
adja.

::: example
:::

Az **első példa bemenetben**:

-   Az első lekérdezésben $V_1 = 9$ és $V_2 = 3$, $9\& 3 = 1$, tehát van
    egy él az $1$-es és $2$-es csúcs között, tehát a minimális távolság
    $1$.

-   A második lekérdezésben $V_2 = 3$ és $V_4 = 6$, $3\& 6 = 2$, tehát
    van egy él a $2$-es és $4$-es csúcs között, tehát a minimális
    távolság $1$.

-   A harmadik lekérdezésben $V_4 = 6$ és $V_1 = 9$, $6\& 9 = 0$, tehát
    nincs él a $4$-es és $1$-es csúcsok között, tehát a minimális
    távolság legalább $2$. A $4, 2, 1$ útvonal esetében a csúcsok
    értékei $6, 3, 9$, ami azt jelenti, hogy a $4$-es és $2$-es csúcs
    között van egy él, valamint a $2$-es és $1$-es között is, tehát a
    $4$-es és $1$-es csúcs között van egy $2$ hosszúságú útvonal.

-   A negyedik lekérdezésben $V_1 \& V_3 = 0$, $V_2 \& V_3 = 0$ és
    $V_4 \& V_3 = 0$, ami azt jelenti, hogy a $3$-as csúcsból nem indul
    ki egy él sem, tehát nincs út a $2$-es és $3$-as csúcs között.
