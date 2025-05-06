## Pénzérme ellenőrzés
A Zorblax bolygón a kormány egy új pénzérmékből álló rendszert vezetett be. Ez $N$ különböző érmetípust jelent, amelyeket nagy mennyiségben fognak kiállítani. A feladatod az, hogy ellenőrizd ezt a rendszert azáltal, hogy meghatározod, bizonyos összegek kifizethetők-e a rendelkezésre álló érmékkel (bármennyi darabot felhasználva az egyes típusokból).

### Bemenet
Az első sor tartalmazza $N$ és $Q$ értékét — az érmetípusok számát és az ellenőrizendő összegek számát.  
A második sor $N$ egész számot tartalmaz, amelyek az érmetípusok értékeit ($C_i$) adják meg.  
A következő $Q$ sor mindegyike egy-egy egész számot tartalmaz ($X_j$), amelyek az ellenőrizendő összegeket jelölik.

### Kimenet
Az egyes kérdésekre írd ki, hogy `YES`, ha az adott $X_i$ összeg kifizethető a rendelkezésre álló érmékkel, különben pedig azt, hogy `NO`.

### Korlátok
* $1 \le N \le 100$
* $1 \le Q \le 100\,000$
* $1 \le C_i \le 100\,000$ minden $i=1 \dots N$ esetén
* $1 \le X_j \le 100\,000$ minden $j=1 \dots Q$ esetén

### Példa bemenet
    2 4
    2 4
    6
    7
    8
    10

### Példa kimenet
    YES
    NO
    YES
    YES

### A példa magyarázata
A rendelkezésre álló pénzérmék: 2 és 4.  
- $X = 6$ kifizethető $2 + 4$ formában.  
- $X = 7$ nem fizethető ki az érmék semmilyen kombinációjával sem.  
- $X = 8$ kifizethető $4 + 4$ formában.  
- $X = 10$ kifizethető $2 + 4 + 4$ formában.
