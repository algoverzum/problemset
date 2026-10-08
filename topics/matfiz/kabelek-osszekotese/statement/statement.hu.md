## Kabelek Osszekotese
Adott $n$ darab kábel. Két kábel összekötésének költsége a két kábel hosszának összege. Mindig pontosan két kábelt kapcsolhatunk össze, amelyekből egy új, hosszabb kábel keletkezik. Az új kábel hossza a két eredeti kábel hosszának összege.
Határozzuk meg, hogy mekkora a legkisebb összköltség, amellyel az összes kábelt egyetlen kábellé egyesíthetjük!

### Bemenet
A standard bemenet első sora egyetlen egész számot tartalmaz, a kábelek számát: $n$

A második sor $n$ darab pozitív egész számot tartalmaz, a kábelek hosszát ($h_1, \dots, h_n$) . 

### Kimenet
A minimális összköltséget kell kiírni.

### Korlátok
*  $1 \le n \le 100$
*  $1 \le h_i \le 1000$

### Példa bemenet
    4
    4 3 2 6

### Példa kimenet
    29

### A példa magyarázata
A legjobb stratégia:
2 + 3 = 5, költség: 5
4 + 5 = 9, költség: 9
6 + 9 = 15, költség: 15
Az összköltség: 5 + 9 + 15 = 29.

### Hint 1
Minden lépésben a két legrövidebb kábelt érdemes összekötni.

### Hint 2
Gondold végig, hogyan lehet gyorsan megtalálni a két legkisebb elemet!

### Hint 3
Az új kábel hosszát vissza kell helyezni az adatok közé.
