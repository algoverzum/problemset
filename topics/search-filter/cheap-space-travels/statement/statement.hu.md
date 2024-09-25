## Olcsó űrutazások
A barátom, Akikó $N$ darab űrutazás közül választhat. Mindegyik utazásra ismert a cél távolsága fényévekben és az utazás ára tallérokban. Akikót az olyan utazások érdeklik, amelyekben az egy fényévnyi távolságra eső ár nem több, mint 100 tallér. Meg tudod adni neki, hogy melyik utazások közül választhat?

### Bemenet
A bemenetben első sorában az utazások $N$ száma van. Ezt követően $N$ sorban egy-egy utazást jellemző két egész szám szerepel: $D_i$ és $P_i$, a távolsága és az ára ($i = 1, 2, \ldots, N$).

### Kimenet
A kimenet első sorába azon utazások darabszámát írd ki, amelyeknél az egy fényévre eső ár legfeljebb 100 tallér. A második sorban sorold fel ezeknek az utazásoknak a sorszámait szóközzel elválasztva.  

### Korlátok
* $1 \le N \le 100$
* $1 \le D_i \le 100$
* $1 \le P_i \le 100\,000$

### Példa bemenet
    5
    6 600
    30 2001
    2 500
    100 4242
    10 1001

### Példa kimenet
    3
    1 2 4

### A példa magyarázata
3 jó utazás van, az első esetében az egy fényévre eső ár pont 100 tallér, a második esetében 66,7 tallér, a negyedik esetében pedig 42,42 tallér. 

### 2. példa bemenet
    2
    5 600
    13 1337

### 2. példa kimenet
    0

### A példa magyarázata
Amennyiben nincs jó utazás, a második sorba nem kell semmit sem írni.