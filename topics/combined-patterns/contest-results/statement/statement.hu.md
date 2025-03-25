## Verseny helyezések
A Galaktikus Verseny Archívum egy óriási adatbázist tartalmaz, amely a galaxison belüli versenyek eredményeit tárolja. A legendás "Nebulon Futam" legutóbbi eredményeit éppen most digitalizálták, és a Galaktikus Kutatók Szövetsége arra kérte a fejlesztő csapatot, hogy egy olyan programot készítsenek, amely segít gyorsan lekérdezni a futam eredményeit. A te feladatod egy program írása ami megadja, hogy a bemenetben felsorolt szereplő versenyzők az eredménylista hányadik helyén szerepelnek. Ha az eredménylista nem tartalmaz egy versenyzőt, akkor -1-et kell kiírni a helyezése helyett.

### Bemenet
A bemenet első sorában két egész szám van: $N$, a verseny eredménylistájának hossza és $Q$, a kérdéses versenyzők száma.
A második sorban $N$ string van szóközzel elválasztva, a futam eredménylistája, vagyis a versenyzők nevei felsorolva a helyezések sorrendjében.
A harmadik sorban $Q$ string van szóközzel elválasztva, a kérdéses versenyzők nevei.
Minden string az angol ábécé kisbetűiből áll és maximum 100 karakter hosszú.

### Kimenet
$Q$ számot kell kiírnod, minden kérdezett versenyzőre azt, hogy hanyadikként végzett a futamon, vagy ha nem vett részt rajta, akkor -1-et.

### Korlátok
* $1 \le N, Q \le 100$
* Minden string az angol ábécé kisbetűiből áll és maximum 100 karakter hosszú.

### Példa bemenet
    5 4
    nova odyssey phoenix voyager aurora
    nebula nova aurora phoenix

### Példa kimenet
    -1 1 5 3

### A példa magyarázata
A `nebula` nem szerepel, a `nova` első helyen van, az `aurora` ötödik helyen van, a `phoenix` harmadik helyen van.
