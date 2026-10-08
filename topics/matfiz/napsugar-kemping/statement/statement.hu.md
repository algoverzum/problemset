## Napsugár Kemping
A Napsugár Kemping $K$ darab faházat üzemeltet az év minden napján. Minden vendég pontosan $M$ napra foglalhat egy faházat. A vendég egyetlen számot ad meg: annak a napnak a sorszámát, amelyen a foglalása kezdődik. Egy foglalás tehát a kezdőnapot és az azt követő $M-1$ napot foglalja le.A kemping az összes foglalási igényt előre ismeri. Egy faházban egyszerre legfeljebb egy vendég tartózkodhat.

Határozzuk meg, hogy legfeljebb hány foglalási igény teljesíthető!

### Bemenet
A standard bemenet első sora két egész számot tartalmaz:
* $K$ -- a faházak száma,
* $M$ -- egy foglalás hossza napokban.

A második sor egyetlen egész számot tartalmaz: a foglalási igények száma.
A következő $N$ sor mindegyike egyetlen egész számot tartalmaz: a foglalás kezdőnapja.

### Kimenet
A kimenet egyetlen egész számot tartalmazzon: a maximálisan teljesíthető foglalások számát.

### Korlátok
* $1 \le K \le 100$,
* $1 \le M \le 14$,
* $1 \le N \le 1000$,
* $1 \le d_i \le 365$.

### Példa bemenet
    2 7
    8
    1
    10
    2
    11
    1
    3
    4
    18

### Példa kimenet
    5

### A példa magyarázata
Két faház áll rendelkezésre, és minden foglalás 7 napig tart.
A foglalásokat kezdőnap szerint vizsgálva mindig azt kell eldönteni, hogy felszabadul-e valamelyik faház a vendég érkezéséig. A maximálisan elfogadható foglalások száma ebben a példában $5$.

### Hint 1
Két mohó stratégiát lehet megvalósítani: 
a) Az egyik napok szerint halad, az adott napon érkező összes igényt próbálja kiszolgálni tetszőleges sorrendben.
b) A másik az igények szerint halad (előtte rendezve a foglalási igényeket kezdőnap szerint növekvő sorrendben), és mindig a legkorábban felszabaduló faházat választja.

### Hint 2
a) Érdemes megszámolni, hogy az év egyes napjain hány foglalási igény érkezik. Mivel a napok száma legfeljebb 365, használhatunk egy tömböt, ahol az $i$-edik elem az $i$-edik napon kezdődő foglalások számát tárolja.
b) Egy új foglalási igény elbírálásához azt kell eldönteni, hogy van-e olyan faház, amely a vendég érkezésekor már szabad.

### Hint 3
a) Minden faházhoz tároljuk el, hogy legközelebb melyik napon lesz újra szabad. Kezdetben minden faház azonnal foglalható.
b) Mindig azt a faházat vizsgáljuk először, amelyik a leghamarabb válik szabaddá.

### Hint 4
a) Haladjunk végig az év napjain növekvő sorrendben! Ha egy adott napon érkezik foglalási igény, keressünk olyan faházat, amely ezen a napon már szabad. Ha találunk szabad faházat, akkor elfogadhatjuk a foglalást. A faház következő szabad napja ekkor a foglalás kezdőnapja után $M$ nappal lesz.
b) Ha több faház közül választhatunk, elegendő azt vizsgálni, amelyik a leghamarabb szabadul fel. Ha ez sem szabad még, akkor egyik másik faház sem lesz megfelelő.