## Űrjelzések
Egy űrállomás jelzéseket fogad az univerzum minden részéről. De sajnos elromlott az ehhez használt műszerük, így nem tudják fogadni az 500-nál kisebb frekvenciáju jelzéseket. Írd ki hány jelzést tud fogadni az űrállomás és a fogadott jelzések forrásait.

### Bemenet
A bemenetben első sorában a jelzések száma egy egész szám van: $N$  <br> 
Ezután $N$ db jelzés, minden jelzés 2 sor. Első sorban egy $S$ szó a jelzés forrása(angol kis és nagy betűkből áll), második sor egy $F$ szám, a jelzés frekvenciája.

### Kimenet
Egy sorban a fogadott jelzések számát kell kiírni, majd a jelzések forrásait(a bemenet sorrendjében) szóközzel elválasztva.

### Korlátok
* $1 \le N \le 1000$
* $1 \le N \le 1000$
* $1 \le S.size() \le 100$
### Példa bemenet
    6
    Earth
    200
    Mars
    100
    Venus
    600
    Jupiter
    500
    Saturn
    200
    Pluto
    800

### Példa kimenet
    3 Venus Jupiter Pluto

### A példa magyarázata
    Earth
    200<500     nem tudjuk fogadni
    Mars
    100<500     nem tudjuk fogadni
    Venus  
    600>=500        tudjuk fogadni
    Jupiter
    500>=500        tudjuk fogadni
    Saturn
    200<500     nem tudjuk fogadni
    Pluto
    800>=500        tudjuk fogadni