## Legtöbb-legkevesebb csere
Egy osztályban $N$ diák van, akiket $1$-től $N$-ig sorszámozunk. A tanár azt a játékot játssza a diákjaival, hogy a tanári asztalon van egy halom cukorka, minden diák sorban elvehet belőle amennyit szeretne, de nem szabad ugyanannyit elvenni, mint amennyit egy másik diák vett el. A végén a diáknak aki a legtöbb cukorkát vette el, cserélnie kell azzal, aki a legkevesebb cukorkát vette el.

### Bemenet
A bemenet első sorában a diákok száma van: $N$.
A bemenet második sorában a diákok által elvett cukorkák száma van: $A_1, A_2, \ldots, A_{N}$.

### Kimenet
Írd ki sorban, hogy melyik diáknak hány cukorkája lesz a csere után, szóközökkel elválasztva.

### Korlátok
* $1 \le N \le 1000$
* $1 \le A \le 1000$

### Példa bemenet
    5
    3 4 5 2 1

### Példa kimenet
    3 4 1 2 5

### A példa magyarázata
    A legtöbb cukorkát a harmadik diák vette el, ötöt. A legkevesebbet pedig az ötödik diák, egyet. Nekik kell cserélni, ezért a végén a harmadik diáknak lesz egy, az ötödiknek öt.

