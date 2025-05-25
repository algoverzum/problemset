## Expedíciók
A Galaktikus Régészeti Liga elindította az Ősi Relikviák Expedícióját, melynek célja, hogy feltérképezze és kiemelje az elveszett civilizációk technológiáit bolygók felszíne alól.
A bolygó felszíne szektorokra van osztva, és minden expedíciós csapat egy adott, összefüggő szektorsávra adhat be feltárási engedélykérelmet. A kérelmek titkosítva érkeznek. Minden kérelem tartalmazza, hogy melyik szektortól melyikig szeretnének kutatni, valamint, hogy mennyi kreditet ajánlanak a Liga számára cserébe a kutatási jogért.
A Liga célja kiválasztani azokat az engedélyeket, amelyek összesen a legtöbb kreditet hozzák – úgy, hogy egy szektoron csak egy csapat dolgozhat.
Segíts a Ligának meghozni a döntést!

### Bemenet
Az első sor két egész számot tartalmaz:  
$N$ : kérelmek száma  
$M$ : szektorok száma a bolygón  
A következő $N$ sor mindegyike három egész számot tartalmaz:  
$A_i$ : A kezdő szektor, $B_i$ : A záró szektor, $K_i$ : az expedícióért felajánlott kreditmennyiség  


### Kimenet
Az első sorba az elérhető maximális kreditmennyiséget írd ki.  
A második sorba azoknak az engedélyeknek a sorszámait írd növekvő sorrendben, amelyeket elfogadtak.

### Korlátok
* $1 \le N, M \le 1000$
* $1 \le A_i \le B_i \le 1000$ minden $i=1 \dots N$-re
* $1 \le K_i \le 1000$ minden $i=1 \dots N$-re

### Példa bemenet
    5 7
    2 3 600
    6 6 180
    3 4 900
    1 6 990
    4 7 600


### Példa kimenet
    1200
    1 5

### A példa magyarázata
Az első és az ötödik kérelmet érdemes elfogadni. Az első 600 és az ötödik is 600 kreditet ad, ami összesen 1200. Belátható, hogy nem szerezhető ennél több kredit.

