## Yukkai jegyek
Yukkában most zárult a félév, és a tanárnő értékelni szeretné a diákokat. A diákok egy listáját kapjukm a nevükkel és a pontszámukkal. A tanárnő az alábbi statisztikákat szeretné látni:

1. Hány diák bukott meg (**kevesebb mint 50 pontot ért el**).
2. Ki szerezte a **legtöbb** és a **legkevesebb** pontot (név és pontszám).
3. Az összes diák pontjait **növekvő sorrendben**.
4. Azon diákok neveit, akik **átmentek** (**legalább 50 pontot** értek el). Ha mindenki megbukott, akkor
egy kötőjelet írass ki az "Átmentek: " után. Azaz: "`Átmentek: -`"

Segíts a tanárnőnek kiszámolni ezeket az értékeket!

### Bemenet
A bemenet első sora egy egész számot tartalmaz: $N$: a diákok száma ($1 \le N \le 100$).

A következő $N$ sor mindegyike két adatot tartalmaz: $név pont$, ahol $név$ egy szó, az angol ábécé betűiből, és $pont$ egy egész szám ($0 \le pont \le 100$).

### Kimenet
Írj ki öt sort az alábbi formátumban:

    Megbuktak: X
    Legjobb: <név> (<pont>)
    Legrosszabb: <név> (<pont>)
    Rendezett pontok: p1 p2 p3 ... pn
    Átmentek: név1 név2 név3 ...

### Példa bemenet
    5
    anna 60
    bela 45
    cili 90
    dani 50
    emil 30

### Példa kimenet
    Megbuktak: 2
    Legjobb: cili (90)
    Legrosszabb: emil (30)
    Rendezett pontok: 30 45 50 60 90
    Átmentek: anna cili dani

