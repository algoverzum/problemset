## Űrjelzések
Egy űrállomás jelzéseket fogad az univerzum minden részéről. Ismerjük minden jelzés forrásának nevét és a jelzés frekvenciáját. De sajnos elromlott az ehhez használt műszerük, így nem tudják fogadni az 500-nál kisebb frekvenciájú jelzéseket. Írd ki, hogy hány jelzést tud fogadni az űrállomás, és a fogadott jelzések forrásait.

### Bemenet
A bemenetben első sorában egy egész szám van, a jelzések száma: $N$  <br> 
Ezután $N$ jelzés következik, minden jelzés 2 sorban van leírva. Az első sorban egy $S$ karaktersorozat van, a jelzés forrása (angol kisbetűkből áll), második sorban pedig egy $F$ szám, a jelzés frekvenciája.

### Kimenet
Egy sorban a fogadott jelzések számát kell kiírni, majd a jelzések forrásait (a bemenet sorrendjében) szóközzel elválasztva.

### Korlátok
* $1 \le N \le 1000$
A szavak az angol ábécé kisbetűiből állnak és legfeljebb 100 betű hosszúak. 

### Példa bemenet
    6
    earth
    200
    mars
    100
    venus
    600
    jupiter
    500
    saturn
    499
    pluto
    800

### Példa kimenet
    3 venus jupiter pluto

### A példa magyarázata
Három jelzést tudunk fogadni, amelyek forrása a venus, jupiter és pluto (frekvenciáik rendre 600, 500 és 800). Nem tudjuk fogadni az earth, mars és saturn forrásról érkező jelzéseket, mert a frekvenciájuk kisebb 500-nál (200, 100, illetve 499).