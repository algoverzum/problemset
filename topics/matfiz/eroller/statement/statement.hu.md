## Elektromos rollerek
A RollEScooter cég $N$ különböző városokban üzemeltet elektromos rollereket.
Minden olyan városban, ahol jelen vannak, pontosan $M$ darab rollerrel rendelkeznek. Az i. városban lévő j. sorszámú roller aktuális töltöttségi szintje ($P_{i,j}$). Írj olyan programot, amely megadja annak a városnak a sorszámát, ahol a legtöbb olyan roller van, melynek töltöttségi szintje $L$-tól kisebb, és azt is, hogy hány ilyen van! Ha több ilyen is van, akkor az összes város sorszámát ki kell írni, növekvő sorrendben!

### Bemenet
Az első sorban $N$ és $M$ és $L$ értéke van. A következő N sorban M darab szám van, az egyes rollerek töltöttségi szintje ($P_{i,j}$ százalékos érték, egész szám). 

### Kimenet
A kimenet első sorába írasd ki azt, hogy hány roller van egy adott városban, amelynek a töltöttségi szintje $L$ alatti. A legnagyobbat kell megtalálnod. A következő sorban annak a városnak vagy városoknak a sorszámát írasd ki, ahol pontosan ennyi $L$ töltöttségi szint alatti roller van, pontosan egy szóközzel elválasztva őket! Ha egyetlen ilyen roller sincs, akkor 0-t kell kiíratni, alá pedig a NINCS üzenetet.

### Korlátok
* $2 \leq N \leq 100.$
* $2 \leq M \leq 50.$
* $0 \leq L \leq 100.$
* $0 \leq P_{i,j} \leq 100.$

### 1. példa bemenet
    5 4 30
    45 30 12 15
    70 80 90 50
    10 5 80 90
    70 80 91 51
    70 80 91 51

### 1. példa kimenet
    2
    1 3

### Az 1. példa magyarázata
Az 1. és a 3. városban is 2 olyan roller van, amelynek a töltöttsége ($L$)=30 alatti. 

### 2. példa bemenet
    5 4 10
    45 30 12 15
    70 80 90 50
    10 11 80 90
    70 80 91 51
    70 80 91 51

### 2. példa kimenet
    0
    NINCS

### A 2. példa magyarázata
Nincs 10% alatti töltöttségű roller.