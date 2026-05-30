## Kör osztály
Egészítsd ki a `Circle` osztály metódusait!

A kör egyetlen adattagja a sugár (radius). Az osztály segítségével lehessen lekérdezni és módosítani a sugarat, kiszámítani a kör területét, kerületét, valamint két kört összehasonlítani.

Elvárások:

* A konstruktor tárolja el a kör sugarát.
* A `get_radius()` metódus adja vissza a kör sugarát.
* A `set_radius()` metódus állítsa be a kör új sugarát.
* A `get_area()` metódus számítsa ki a kör területét a következő képlet alapján: $T=3.14\cdot r^2$. (Azaz $\pi$ értéke legyen $3.14$.)
* A `get_perimeter()` metódus számítsa ki a kör kerületét a következő képlet alapján: $K=2\cdot 3.14\cdot r$. (Azaz $\pi$ értéke legyen $3.14$.)
* A `bigger()` metódus adja vissza azt a Circle objektumot, amelyiknek nagyobb a sugara. Ha a sugarak egyenlők, bármelyik objektum visszaadható.

### Sablon
Indulj ki az előre készített sablon kódból! Ne változtass a főprogramon semmit, mert különben nem lesz elfogadva. A `Circle` osztáy függvény metódusait kell megírnod.

### Korlátok
* $1 \le r \le 10^6$
