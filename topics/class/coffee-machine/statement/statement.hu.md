## Kávéfőző
Készíts egy CoffeeMachine nevű osztályt, amely egy kávégép működését szimulálja!

Adattagok (Változók):  
A gépnek négy tulajdonsággal kell rendelkeznie. A belső állapotot leíró változókat privátként hozd létre (Pythonban használd a dupla alulvonás `__` előtagot), hogy kívülről ne lehessen őket közvetlenül módosítani!

* `brand`: A gép márkája (szöveg, lehet publikus).
* `is_on`: Jelzi, hogy a gép kap-e áramot (logikai érték, induláskor False).
* `water_ml`: A tartályban lévő víz mennyisége milliliterben (egész szám, induláskor 0).
* `coffee_g`: A betöltött kávé mennyisége grammban (egész szám, induláskor 0).

Metódusok (Függvények):  
Írd meg az alábbi függvényeket az osztályon belül a megadott nevekkel:

* A konstruktor. Állítsa be a gép márkáját a paraméter alapján, a többi privát változót pedig állítsa alaphelyzetbe (`False`/`false` és `0`).
* `set_electricity()`: Vár egy logikai (igaz/hamis) paramétert. Beállítja a gép áramellátását (`is_on`) a megadott értékre.
* `add_water()`: Vár egy szám paramétert. Hozzáadja a megadott mennyiséget a gép jelenlegi vízkészletéhez.
* `add_coffee(self, amount)`: Vár egy szám paramétert. Hozzáadja a megadott mennyiséget a gép jelenlegi kávékészletéhez.
* `brew_coffee()`: Ez végzi a kávéfőzést. Ellenőrizze, hogy a gép be van-e kapcsolva, van-e benne legalább 50 ml víz és legalább 15 g kávé.  
  Ha minden feltétel teljesül, vonjon le 50 vizet és 15 kávét, majd térjen vissza `igaz` értékkel.  
  Ha bármelyik feltétel hiányzik, ne vonjon le semmit, és térjen vissza `hamis` értékkel.
* `get_status()`: Egy "getter" függvény, amely nem módosít semmit, csak visszaad egy formázott szöveget a gép aktuális állapotáról (márka, be van-e kapcsolva ("ON"/"OFF"), víz- és kávészint). Pl.: "ABC ON 100ml 5g"-t ha a márkája ABC, be van kapcsolva, 100 ml víz van benne és 5 g kávé. 

### Sablon
Indulj ki az előre készített sablon kódból! Ne változtass a főprogramon semmit, mert különben nem lesz elfogadva. A `CoffeeMachine` osztáy függvény metódusait kell megírnod.

### Korlátok
* Minden érték a tesztelés alatt garantáltan kis pozitív egész szám.
