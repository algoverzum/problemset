Egy állatkertben $N$ rozmár [^1] ül szépen egy sorban. A rozmárokat
$0$-tól $N-1$-ig számozzuk.

![*Odobenus Rosmarus*, más néven *rozmár*.](walrus.jpg){width="60%"}

A rozmárok állapotát egy $N$ karakterből álló
$\overline{c_0c_1\ldots c_{N-1}}$ karakterlánc jellemzi, ahol:

-   $c_i=$`’.’`, ha az $i$. rozmár alszik,

-   $c_i=$`’-’`, ha az $i$. rozmár ébren van.

Minden másodpercben a következő két dolog történik:

1.  választhatsz egy alvó rozmárt, és felébresztheted,

2.  minden olyan rozmár, amelyiket az előző másodpercben felébresztett
    valaki, felébreszti a szomszédait. (Azok a rozmárok, amelyek a
    legelején ébren voltak, **sohasem** ébresztik fel a szomszédaikat.)

Minden rozmárt szeretnénk ébren látni. Mivel a rozmárok felébresztése
veszélyes, a következő kérdésekre szeretnénk választ kapni:

1.  Legkevesebb hány rozmárt kell felébresztened ahhoz, hogy garantáltan
    végül minden rozmár felébredjen?

2.  Ha a lehető legkevesebb rozmárt ébreszted fel, mi a legkorábbi
    lehetséges időpont (másodpercekben), amikor minden rozmár felébred?

::: warning
Az értékelő rendszerből letölthető csatolmányok közt találhatsz
`morse.*` nevű fájlokat, melyek a bemeneti adatok beolvasását valósítják
meg az egyes programnyelveken. A megoldásodat ezekből a hiányos minta
implementációkból kiindulva is elkészítheted.
:::

Minden teszt több tesztesetet tartalmaz. A bemenet első sora egyetlen
egész számot tartalmaz a tesztesetek $T$ számát.

Minden teszteset első sora egyetlen egész számot tartalmaz, a rozmárok
$N$ számát.

Minden teszteset második sora egy $N$ karakterből álló
$\overline{c_0c_1\ldots c_{N-1}}$ karakterláncot tartalmaz.

Minden tesztesethez írj ki két szóközzel elválasztott egész számot egy
sorba:

1.  a legkisebb számot, amennyi rozmár felébresztése elég ahhoz, hogy
    végül mindegyik felébredjen

2.  a legkorábbi lehetséges időpont (másodpercben), amikor az összes
    rozmár felébred ebben az esetben.

A megoldásodat sok különböző tesztesetre lefuttatjuk. A tesztesetek
részfeladatokba vannak csoportosítva. Egy-egy részfeladatot akkor
tekintünk megoldottnak, ha volt legalább egy olyan beadásod, amely az
adott részfeladat minden tesztesetére helyes megoldást adott. A feladat
összpontszámát a megoldott részfeladatokra kapott pontszámok összege
adja.

-   $1 \le T \le \constraints{MAXT}$.

-   $1 \le N \le \constraints{MAXN}$.

-   Legalább egy rozmár kezdetben alszik.

-   Az $N$ értékek összege az összes tesztesetben nem haladja meg a
    $\constraints{MAXN}$ értéket.

::: example
:::

Optimális stratégia a példa **első tesztesetére**:

Az első másodpercben felébreszthetjük az $1$-es rozmárt ($0$-val
kezdődik a számozás): $$\texttt{..-.. } \rightarrow \texttt{ .{-}-.. }$$
A második másodpercben fel tudod ébreszteni a $4$-es rozmárt. Ezen kívül
az $1$-es rozmár felébreszti a $0$-dik rozmárt:
$$\texttt{.-{-}.. } \rightarrow \texttt{ .-{-}.- } \rightarrow \texttt{ -{-}-.- }$$
A harmadik másodpercben nem ébresztünk fel egyetlen rozmárt sem. A
$3$-as rozmárt azonban a $4$-as rozmár ébreszti fel:
$$\texttt{-{-}-.- } \rightarrow \texttt{ -{-}-{-}-}$$ Összesen $2$
rozmárt ébresztettél fel, ami minimálisan szükséges ahhoz, hogy minden
rozmár felébredjen.

Miközben $2$ rozmárt ébresztettünk fel, az összes rozmár felébredéséhez
szükséges minimális idő $3$ másodperc.

Optimális stratégia a **második tesztesetre**:

Az első másodpercben az $1$-es rozmárt ébresztjük fel. A másik két
rozmár a következő másodpercben az $1$-es rozmár ébreszti fel:
$$\texttt{... } \rightarrow \texttt{ .-. } \rightarrow \texttt{ -{-}-}$$

[^1]: románul ,,*morse*"
