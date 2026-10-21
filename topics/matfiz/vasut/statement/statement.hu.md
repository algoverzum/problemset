## Vasút kocsik rendezése
Egy rendező pályaudvaron tehervonat érkezik. A vonat $N$ darab vasúti kocsiból áll, amelyek kezdetben $1,2,3,\dots,N$ sorrendben követik egymást (az 1-es kocsi van legelöl, majd a 2-es, stb., az $N$-es kocsi van legalul).

A pályaudvaron van egy **verem** (angolul: **stack**), amelybe ideiglenesen be lehet tolni kocsikat. A verem mélysége korlátlan (elméletileg végtelen). A következő műveleteket végezhetjük:

* **Betesz (push):** A bemeneti sor elejéről (a vonat elejéről) elveszünk egy kocsit, és betesszük a verem tetejére.
* **Kivesz (pop):** A verem tetejéről elveszünk egy kocsit, és áttesszük a kimeneti sor végére.


A cél az, hogy a kimeneti sorban a kocsik egy előre megadott sorrendben kövessék egymást. A kérdés: előállítható-e ez a sorrend a fenti műveletekkel?

### Bemenet
Az első sor egyetlen $N$ egész számot tartalmaz, a kocsik számát.
A második sor $N$ darab, egymástól pontosan egy szóközzel elválasztott egész számot tartalmaz: a kívánt kimeneti sorozatot ($s_1, \dots, s_n$ ).

### Kimenet
Egyetlen sort kell kiírni:
* **IGEN** ha a permutáció megvalósítható,
* **NEM** ha nem.

### Korlátok
*  $1 \le N \le 10^5$
* \* $1 \le s_i \le 10^5$

### Példa bemenet 1
    5
    1 2 3 4 5

### Példa kimenet 1
    IGEN

### Példa bemenet 2
    5
    5 4 3 2 1

### Példa kimenet 2
    IGEN

### Példa bemenet 3
    5
    3 4 5 1 2

### Példa kimenet 3
    NEM

### A példa magyarázata
**1. példa** A kimeneti sor $1,2,3,4,5$. Ezt úgy kaphatjuk meg, hogy minden kocsit egymás után tolunk a verembe, majd azonnal emeljük is ki. (Gyakorlatilag: push(1), pop(), push(2), pop(), ...)

**2. példa:** A kimeneti sor $5,4,3,2,1$. Ezt úgy kaphatjuk meg, hogy először betoljuk az összes kocsit a verembe ($1,2,3,4,5$), majd sorban kiemeljük őket. Ekkor a kiemelés sorrendje valóban $5,4,3,2,1$ lesz.

**3. példa** A kimeneti sor $3,4,5,1,2$. Ez nem valósítható meg, mert az 1-es és 2-es kocsi csak akkor kerülhetne a 3-as,4-es,5-ös után, ha előbb kijönnek, de akkor viszont nem jöhetnek a sor végén. Részletesen: először be kell tolnunk 1,2,3-at a verembe, hogy 3 kijöhessen, majd 4-hez tovább kell tolni 4-et, majd 5-höz 5-öt. Ekkor a veremben 1,2 marad, de 1 nem jöhet ki 2 előtt, mert a veremben 2 van felül. Így a sorrend nem állítható elő.

### Hint 1
A feladat ismert neve: **train sorting** vagy **stack permutation**. 
A lényeg: a kimeneti sorozatot balról jobbra kell előállítanunk. Mindig két lehetőségünk van: ha a következő kívánt kocsi éppen a bemenet elején van, kivehetjük onnan; ha a verem tetején van, onnan is kivehetjük. Egyéb esetben a bemenetről tolunk a verembe, amíg meg nem jelenik a keresett kocsi. Tehát kell egy verem, pl. stack<int> s;

### Hint 2
Algoritmus vázlat:
* Legyen $akt = 1$ (a következő kocsi, amit a bemenetről tolhatunk)!
* Végigmegyünk a kimeneti sorozaton.
*  Minden egyes kívánt kocsihoz: Ha a verem tetején éppen ez van $\rightarrow$ pop(). Különben addig tolunk a bemenetről, amíg a kívánt kocsi be nem kerül a verem tetejére (ha közben elfogy a bemenet, akkor lehetetlen).
        
### Hint 3
A bemenet kezdetben $1,2,\dots,N$ sorrendben van, ezért a "következő tolandó kocsi" mindig egy számlálóval nyomon követhető. Nem kell tömböt fenntartanunk a bemenetre, elég egyetlen egész változó ($next\_to\_push$).