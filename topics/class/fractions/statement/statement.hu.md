## Törtek
Készíts egy **Fraction** osztályt, amely egy törtszámot reprezentál egy számláló és egy nevező segítségével.

A törtet két adattag segítségével kell tárolni. A belső állapotot leíró változókat privátként hozd létre (Pythonban használd a dupla alulvonás `__` előtagot, C++-ban a private láthatóságot), hogy kívülről ne lehessen őket közvetlenül módosítani!

* `num`: A tört számlálója (egész szám).
* `denom`: A tört nevezője (egész szám, értéke nem lehet 0). A nevező tárolt értéke legyen pozitív. num és denom legyenek relatív prímek. 

Metódusok (Függvények):

Írd meg az alábbi függvényeket az osztályon belül a sablonban megadott nevekkel:

* A konstruktor. Két egész számot kap paraméterként (számláló és nevező). Állítsa be a megfelelő adattagokat, majd egyszerűsítse a törtet a reduce() függvény meghívásával.
* `reduce()`: Egyszerűsítse a törtet a legnagyobb közös osztó segítségével. Gondoskodjon arról is, hogy a nevező mindig pozitív legyen.
* Szöveges megjelenítés: a törtet "számláló/nevező" formában jelenítse meg. Például: -1/2.
* Összeadás: két tört összegét adja vissza új törtként.
* Kivonás: két tört különbségét adja vissza új törtként.
* Szorzás: két tört szorzatát adja vissza új törtként.
* Osztás: két tört hányadosát adja vissza új törtként.

Megjegyzés:

A műveletek eredményeként létrejövő törteket is egyszerűsített alakban kell tárolni.
Az egyszerűsítéshez használható a beépített `gcd` függvény (math.gcd Pythonban, std::gcd C++-ban).
C++ esetén az összeadás, kivonás, szorzás, osztás és kiírás megvalósítható operátor-túlterheléssel (operator+, operator-, operator*, operator/, operator<<).

### Sablon
Indulj ki az előre készített sablon kódból! Ne változtass a főprogramon semmit, mert különben nem lesz elfogadva. A `Fraction` osztály függvény metódusait kell megírnod.

### Korlátok
* Minden érték a tesztelés alatt garantáltan kis pozitív egész szám.
* A nevező soha nem lesz 0 a tesztekben.
