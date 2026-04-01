## Legszmogosabb hét
Az elmúlt N héten minden nap megmértük a légyszennyezettség mértékét, mg/Nm³-ben. Írj programot, amely megadja annak a hétnek a sorszámát, amelyik a legszennyezettebb volt, azaz a hét nap alatt a szennyezőanyagok mennyiségének az összege a legnagyobb volt! Ha több ilyen hét is van, akkor a legnagyobb sorszámút kell megadnod!

### Bemenet
A standard bemenet első sora a hetek számát tartalmazza. A következő N sorban egy-egy hét 7 légszennyezettsége található: $C_{i,j}$.

### Kimenet
A standard kimenet egyetlen sorába a legszennyezettebb hét sorszámát kell kiírni (több megoldás esetén a legnagyobb sorszámút)!

### Korlátok
* $2 \leq N \leq 1000.$
* $0 \leq  C_{i,j} \leq 2000.$

### Példa bemenet
    6
    50 100 150 200 250 300 350
    10 20 200 200 200 300 120
    50 100 150 200 250 300 350
    100 200 200 200 200 300 120
    400 400 400 450 450 400 400
    400 400 400 400 500 400 400

### Példa kimenet
    6

### A példa magyarázata
Az 5. és a 6 héten is a számok összege 2900, de a legnagyobb sorszámút kell kiíratni!