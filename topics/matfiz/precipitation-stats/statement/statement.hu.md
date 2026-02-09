## Csapadék statisztika

Az elmúlt $N$ hétben minden nap megmértük a lehullott csapadék mennyiségét, milliméterben. Írj programot, amely megadja a legcsapadékosabb hetet!

### Bemenet
A standard bemenet első sora a hetek számát tartalmazza ($N$). A következő $N$ sorban egy-egy hét 7 csapadékmennyisége található ($C$).

### Kimenet
A standard kimenet egyetlen sorába a legcsapadékosabb hét sorszámát kell kiírni (több megoldás esetén a legkisebb sorszámút)!

## Korlátok
- $2 \le N \le 1000$
- $0 \le C_{i,j} \le 1000$

### Példa

#### 1. példa bemenet

    6
    5 10 15 20 25 30 35
    0 2 0 0 0 0 0
    0 0 0 1 0 3 0
    0 1 2 3 4 5 6
    5 1 0 0 2 1 0
    0 0 0 0 0 0 0

#### 1. példa kimenet

    1

#### 2. példa bemenet

    2
    1 0 1 0 0 0 1
    0 1 0 1 1 0 0

#### 2. példa kimenet

    1
