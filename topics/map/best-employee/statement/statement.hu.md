## Legjobb alkalmazott
Egy nem is olyan távoli galaxisban a híres Galactical Technology Solutions Inc. vállalat úgy döntött, hogy megjutalmazza a legelhivatottabb alkalmazottját — azt a dolgozót, aki a leghosszabb időt töltötte az irodában anélkül, hogy elhagyta volna azt. Ez az alkalmazott a cég leghűségesebb és legszorgalmasabb tagjaként lesz elismerve. Az alkalmazott azonosításához a cég rögzítette az alkalmazottak érkezési és távozási időpontjait.

A te feladatod, hogy segíts a cégnek kideríteni, ki ez a kivételes alkalmazott. Az adatok helyesek, azaz senki sem távozott anélkül, hogy előbb belépett volna, senki sem lépett be kétszer egymás után távozás nélkül, valamint az iroda üres volt mind az események előtt, mind pedig azok után. Továbbá a keresett alkalmazott személye egyértelműen megállapítható, azaz a maximális időtartam csak egy alkalmazott esetében fordul elő az adatok közt.

### Bemenet
A bemenet első sora tartalmazza $N$-t — a rögzített események számát.  
A következő $N$ sor mindegyike egy eseményt ír le három szóközzel elválasztott egész számmal:

* Az alkalmazott azonosítója ($A_i$).  
* Az esemény típusa ($E_i$, ahol 0 azt jelenti, hogy az alkalmazott elhagyta az épületet, és 1 pedig azt, hogy belépett az épületbe).  
* Az esemény időbélyege ($T_i$).

### Kimenet
Két számot írj ki szóközzel elválasztva:

* Annak az alkalmazottnak az azonosítóját, aki a leghosszabb időt töltötte az épületben.  
* Ennek a megszakítatlan benntartózkodásnak a hosszát.

### Megkötések
* $1 \le N \le 100\,000$
* $0 \le A_i \le 10^9$ minden $i = 1 \dots N$ esetén
* $0 \le T_i \le 10^9$ minden $i = 1 \dots N$ esetén
* Az események kronologikusan (idő szerint rendezve) vannak megadva.

### Példa bemenet
    8
    1 1 1
    2 1 2
    1 0 5
    3 1 7
    1 1 8
    2 0 8
    3 0 10
    1 0 11

### Példa kimenet
    2 6

### A példa magyarázata
Az 1-es alkalmazott 1-es időbélyegnél lépett be az irodába, és 5-ös időbélyegnél távozott, így 4 egységnyi időt töltött bent, majd még egyszer belépett és 3 egységnyi időtt töltött bent a 8-as és 11-es időbélyeg között.

A 2-es alkalmazott 2-es időbélyegnél lépett be, és 8-as időbélyegnél távozott, így 6 egységnyi időt töltött bent.

A 3-as alkalmazott 7-es időbélyegnél lépett be, és 10-es időbélyegnél távozott, így 3 egységnyi időt töltött bent.  
