## Űrjelzések
Egy űrállomás jelzéseket fogad az univerzum minden részéről. De sajnos elromlott az ehhez használt műszerük, így nem tudják fogadni az 500-nál kisebb frekvenciájú jelzéseket. Írd ki hány jelzést tud fogadni az űrállomás és a fogadott jelzések forrásait.

### Bemenet
A bemenetben első sorában a jelzések száma egy egész szám van: $N$  <br> 
Ezután $N$ db jelzés, minden jelzés 2 sor. Első sorban egy $S$ szó a jelzés forrása(angol kis és nagy betűkből áll), második sor egy $F$ szám, a jelzés frekvenciája.

### Kimenet
Egy sorban a fogadott jelzések számát kell kiírni, majd a jelzések forrásait(a bemenet sorrendjében) szóközzel elválasztva.

### Korlátok
* $1 \le N \le 1000$
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
    200
    pluto
    800

### Példa kimenet
    3 venus jupiter pluto

### A példa magyarázata
    earth
    200<500     nem tudjuk fogadni
    mars
    100<500     nem tudjuk fogadni
    venus  
    600>=500        tudjuk fogadni
    jupiter
    500>=500        tudjuk fogadni
    saturn
    200<500     nem tudjuk fogadni
    pluto
    800>=500        tudjuk fogadni