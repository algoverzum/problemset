## Kereskedők
Egy távoli bolygón két gyümölcskereskedő árul különleges intergalaktikus gyümölcsöket. Mindketten különböző világokról szállítják portékáikat, így kínálatuk részben eltérő. A feladatod, hogy készíts egy programot, amely megmutatja, mely gyümölcsök találhatók meg kizárólag az egyik, de nem a másik kereskedőnél.

### Bemenet
A standard bemenet első sorában az első kereskedő által árult gyümölcsök száma van: $N$. A következő $N$ sorban egy-egy általa árult gyümölcs neve található. A következő sorban a második kereskedő által árult gyümölcsök száma van: $M$. Ezt követi $M$ sorban egy-egy általa árult gyümölcs neve. Ha valamelyik árus egy gyümölcsből többfélét is árul, akkor a neve a bemenetben többször jelenik meg.


### Kimenet
A standard kimenet első sorába azon gyümölcsök $K$ számát kell kiírni, amelyek csak az egyik kereskedőnél kaphatók! A következő $K$ sorba egy-egy ilyen gyümölcs nevét kell kiírni, **ábécé sorrendben**! Minden nevet csak egyszer szabad kiírni!

### Korlátok
* $1 \le N,M \le 10^6$ <br>
* A gyümölcsök nevei az angol ábécé kisbetűiből állnak és legfeljebb 100 karakter hosszúak.

### Példa bemenet
    6
    apple
    apple
    peach
    peach
    strawberry
    plum
    4
    peach
    strawberry
    almond
    blackberry


### Példa kimenet
    4
    almond
    apple
    blackberry
    plum



### A példa magyarázata
Csak az első árulja: apple, plum
Csak a masodik: blackberry, plum
