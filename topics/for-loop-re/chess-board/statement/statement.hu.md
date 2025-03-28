## Sakktábla
Elvesztettem a repülő beszálló kártyámat. Kiderült, hogy egy négyzetben voltak `X` és `Y` karakterek rajta, sakktábla szerűen. Segítenél egy újat nyomtatni?

### Bemenet
A bemenet egyetlen sorában egy egész szám van: $N$ - a sakktábla oldalának a hossza.

### Kimenet
$N$ sort kell kiírni. Minden sorban pontosan $N$ darab `X` vagy `Y` karakter legyen úgy, hogy a szomszédosak különbözőek.
A bal felső sarokban legyen `X`, azaz az első sor első karaktere legyen `X`!

### Korlátok
* $1 \le N \le 20$

### 1. Példa bemenet
    4

### 1. Példa kimenet
    XYXY
    YXYX
    XYXY
    YXYX

### Az 1. példa magyarázata
Egy $4 \times 4$-es sakktáblát kell kiírnunk.

### 2. Példa bemenet
    5

### 2. Példa kimenet
    XYXYX
    YXYXY
    XYXYX
    YXYXY
    XYXYX
