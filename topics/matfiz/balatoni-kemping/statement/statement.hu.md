## Balatoni Kemping
Az Andromeda Kft. egy kempinget üzemeltet a Balaton mellett. A kempingben $K$ darab egyforma faház található. A szezon $D$ napig tart (a napok $1$-től $D$-ig vannak számozva).

A cég $N$ darab foglalási igényt kapott. Minden igényt két szám jellemez:
* $t$ -- a foglalás kezdőnapja $(1 \le t \le D)$
* $h$ -- a foglalás hossza napokban $(1 \le h \le D)$

Egy faházban egyszerre csak egy vendég lakhat. Két foglalás nem fedheti át egymást ugyanabban a faházban: ha egy foglalás a $t$. naptól a $t+h-1$. napig tart, akkor ezekre a napokra más nem foglalhatja ugyanazt a faházat. A $t+h$. napon a faház már újra kiadható.

A kemping célja a kiszolgált foglalások számának maximalizálása. Válasszuk ki az igények egy olyan részhalmazát, amelyek átfedés nélkül kioszthatók a $K$ faházba, és a darabszámuk a lehető legnagyobb!

### Bemenet
```
D K N
t_1 h_1
t_2 h_2
...
t_N h_N
```

* Az első sor három egész számot tartalmaz: $D$ a napok száma $(1 \le D \le 10^5)$, $K$ a faházak száma $(1 \le K \le 10^5)$, $N$ az igények száma $(1 \le N \le 2\cdot 10^5)$.
* A következő $N$ sor mindegyike egy-egy foglalási igényt ír le: $t_i$, $h_i$ $(1 \le t_i \le D$, $1 \le h_i \le D)$.

### Kimenet
Egyetlen egész szám: az elfogadható foglalási igények maximális száma.

### Korlátok
* $1 \le D \le 10^5$, 
* $1 \le K \le 10^5$, 
* $1 \le N \le 2\cdot 10^5$

### Példa bemenet
    10 2 6
    1 3
    2 2
    4 2
    5 3
    7 1
    8 3

### Példa kimenet
    6

### A példa magyarázata
Az alábbi igényeket választjuk ki:

* 1. igény: napok $1,2,3$ (1. faház)
* 2. igény: napok $2,3$ (2. faház) -- párhuzamosan fut az elsővel, de van 2 faházunk.
* 3. igény: napok $4,5$ (1. faház) -- mivel az első faház a $3$. nap végén felszabadul.
* 5. igény: napok $7$ (1. faház) -- a $3$. igény lefutása után szabad helyre.
* 6. igény: napok $8,9,10$ (1. faház) -- az $5$. igény lefutása után szabad helyre.

Összesen $5$ igényt tudunk teljesíteni.

### Hint 1
Érdemes saját struktúrát használni az igények tárolására. Gondoljuk végig a klasszikus intervallum-ütemezési feladatot: mi alapján érdemes sorba rendezni az igényeket, ha a legtöbbet szeretnénk elvállalni? (Segítség: a legkorábban véget érő igények hagynak legtöbb helyet a többinek.)

### Hint 2
Rendezzük az igényeket a felszabadulási napjuk ($t_i + h_i$) szerint növekvő sorrendbe! Így a mohó stratégia elve szerint haladhatunk végig rajtuk: minden igényt elfogadunk, ha van számára szabad faház.

### Hint 3
Mivel $K$ darab faházunk van, egyszerre több igény is futhat. Nem kell mind a $K$ faház állapotát külön ciklussal ellenőrizni, mert az túl lassú lenne. Elég a faházak felszabadulási napjait egy rendezett adatszerkezetben tárolni.

### Hint 4
Ha több faház is szabad az igény kezdőnapján, **nem mindegy, melyiket választjuk!** Ne a legkorábban felszabaduló faházat foglaljuk el, hanem azt, amelyik **a legkésőbb szabadult fel, de legkésőbb a kezdőnapon**. A korán felszabaduló faházat érdemes megtartani egy későbbi, de korábban kezdődő igénynek.

Ellenpélda a „legkorábban felszabaduló” választásra ($K = 2$): az igények `1 1`, `1 4`, `6 1`, `3 5`. Ha a `6 1` igény a 2. napon felszabaduló faházat kapja, a `3 5` már nem fér be (eredmény: 3). Ha az 5. napon felszabadulót kapja, mind a 4 igény teljesíthető.

### Hint 5
Tartsuk nyilván egy listában a már használt faházak felszabadulási napjait, a még érintetlen faházakat pedig egy számlálóval (kezdetben $K$). Mivel az igényeket végnap szerint növekvő sorrendben dolgozzuk fel, az új végnap mindig a lista végére kerül, így a lista magától rendezett marad.

Egy $(t, h)$ igény feldolgozása:
* Bináris kereséssel keressük meg a lista utolsó olyan elemét, amely legfeljebb $t$ (ez a legkésőbb felszabaduló, de már szabad faház).
* Ha van ilyen: vegyük ki a listából, tegyük a lista végére a $t + h$ értéket, és növeljük a számlálót.
* Ha nincs, de van még érintetlen faház: csökkentsük az érintetlen faházak számát, tegyük a lista végére a $t + h$ értéket, és növeljük a számlálót.
* Különben az igényt elutasítjuk.


