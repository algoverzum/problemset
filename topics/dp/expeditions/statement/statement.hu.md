## Expedíciók
A Galaktikus Régészeti Liga elindította az Ősi Relikviák Expedícióját, melynek célja, hogy feltérképezze és kiemelje az elveszett civilizációk technológiáit bolygók felszínéről.
A bolygó felszíne szektorokra van osztva, és minden expedíciós csapat egy adott, összefüggő szektorsávra adhat be feltárási engedélykérelmet. A kérelmek titkosítva érkeznek, és mindegyik tartalmazza:
hogy melyik szektortól melyikig szeretnének kutatni,
valamint hogy mennyi kreditet ajánlanak a Liga számára cserébe a kutatási jogért.
A Liga célja: kiválasztani azokat az engedélyeket, amelyek összesen a legtöbb kreditet hozzák – úgy, hogy egy szektoron csak egy csapat dolgozhat.
Segíts a Ligának meghozni a döntést!


### Bemenet
Az első sor két egész számot tartalmaz:
$N$ : kérelmek száma 
$M$ : szektorok száma a bolygón <br>
A következő $N$ sor mindegyike három egész számot tartalmaz:
$A$ : A kezdő szektor
$B$ : A záró szektor
$K$ : az expedícióért felajánlott kreditmennyiség<br>
A bemenetek a $B$ érték szerint nemcsökkenő sorrendben vannak.



### Kimenet
Az első sorban az elérhető maximális kreditmennyiség szerepel.<br>
A második sorban azoknak az engedélyeknek a sorszámai szerepelnek növekvő sorrendben, amelyeket elfogadtak.



### Korlátok
* $1 \le N \le 1000$
* $1 \le A,B \le 1000$
* $1 \le K \le 1000$

### Példa bemenet
    5 7
    2 4 600
    4 5 400
    6 6 180
    1 6 900
    4 7 600


### Példa kimenet
    1200
    1 5

### A példa magyarázata
Az első és az ötödik kérelmet fogadjuk el. Az első 600 és az ötödik is 600 kreditet ad, ami összesen 1200.

