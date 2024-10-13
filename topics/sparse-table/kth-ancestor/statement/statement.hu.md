## K-adik ős
Susan szeret grafikonokkal játszani, és a Tree adatszerkezet az egyik kedvence. Megtervezett egy problémát, és szeretné tudni, hogy valaki meg tudja-e oldani. Az 1. csomóponttal, mint gyökérrel kezdi, és néha hozzáad vagy eltávolít egy-egy levélcsomópontot. A feladata az, hogy kitalálja, melyik csomópontnak mi a K-edik szülője bármelyik pillanatban.
Ha A csomópont L távolságra van a Gyökér csomóponttól, B pedig L + K távolságra van a Gyökér csomóponttól, és van egy K hosszúságú út A-tól B-ig, akkor A-t nevezzük B K-edik szülőjének.

### Bemenet
A bemenet első sora $N$ a fa csomópontjainak számát tartalmazza.
A bemenet második sora $Q$ a lekérdezések számát tartalmazza.
sorok következnek, amelyek mindegyike egy-egy lekérdezést tartalmaz.
    0 $Y$ $X$ : $X$ új levélcsomópontként kerül be, amelynek szülője $Y$ . $X$ nincs a fában, míg $Y$ benne van.
    1 $X$$ : Ez azt jelenti, hogy a $X$ levélcsomópontot eltávolítjuk a fából. $X$ egy levél a fában.
    2 $X$ $K$ : Ebben a lekérdezésben a $X$ $K$-adik szülője $X$ . $X$ egy csomópont a fában.

### Kimenet
Minden 2. típusú lekérdezéshez adja ki X$$ K-edik szülőjét. Ha a K-edik szülő nem létezik, akkor 0-t, ha pedig a csomópont nem létezik, akkor 0-t adunk ki.

### Korlátok
* $1 \le N \le 200000$
* $1 \le Q \le 200000$

### Példa bemenet
    20
    16
    0 1 5
    0 5 3
    0 5 7
    0 1 8
    0 8 9
    0 8 6
    0 5 15
    2 15 2
    1 3
    0 15 20
    0 20 13
    2 13 4
    2 13 3
    2 6 10
    2 11 1
    2 9 1


### Példa kimenet
    1
    1
    5
    0
    0
    8

### A példa magyarázata
    0 1 5 -> Az 5 az 1-hez levélcsomópontként hozzáadódik.
    0 5 3 -> 3 levélcsomópontként hozzáadódik az 5-höz.
    0 5 7 -> 7 levélcsomópontként hozzáadódik az 5-höz.
    0 1 8 -> 8 levélcsomópontként hozzáadódik az 1. csomóponthoz.
    0 8 9 -> 9 levélcsomópontként hozzáadva a 8-hoz.
    0 8 6 -> 6 levélcsomópontként hozzáadva a 8-hoz.
    0 5 15 -> 15 levélcsomópontként hozzáadva az 5-höz.
    2 15 2 -> a 15 második szülője 15->5->1 az 1.
    1 3 -> a 3-as levélcsomópontot eltávolítjuk a fából.
    0 15 20 -> 20 levélcsomópontként hozzáadódik a 15-öshöz.
    0 20 13 -> a 20-hoz 13 levélcsomópontot adunk.
    2 13 4 -> 13 4. szülője 1.
    2 13 3 -> a 13 3. szülője az 5.
    2 6 10 -> a 6-osnak nincs 10. szülője, tehát 0.
    2 11 1 -> 11 nem csomópont a fán, tehát 0.
    2 9 1 -> 9 szülője a 8-as.

