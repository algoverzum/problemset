## Kő-papír-olló
Az ismert játékot most ketten játszák, valaminek az eldöntésére (például ki rúgja a szabadrúgást).  
Háromféle tippet mutathatnak: kő, papír, olló. Szabályok: A kő legyőzi az ollót, az olló a papírt, a papír a követ. A programunk a beolvasott két tippet összehasonlítva döntse el, hogy melyik játékos nyert! A lehetséges kimenetek: 1 (első játékos nyer), 2 (második játékos nyer), 0 (döntetlen).

### Bemenet
A bemenetben első sorából olvashatjuk be, hogy mit mutatott az első játékos.  
A bemenetben második sorából olvashatjuk be, hogy mit mutatott a második játékos.  
Ékezetes betűket nem használunk, azaz "ko", "papir", "ollo" szerepelhet a sorokban.

### Kimenet
Egyetlen számot kell kiírnod, 1-et ha az első játékos nyer, 2-t ha a második és 0-t ha döntetlen.

### Korlátok
A bemeneti két sorban csak a "ko", "papir", "ollo" szerepelhet (idézőjelek nélkül).

### 1. Példa bemenet
    ko
    papir

### 1. Példa kimenet
    2
    
### 2. Példa bemenet
    ollo
    papir

### 2. Példa kimenet
    1

### 3. Példa bemenet
    ollo
    ollo

### 3. Példa kimenet
    0
