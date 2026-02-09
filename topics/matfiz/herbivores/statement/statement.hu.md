## Növényevő állatok

A Yukka bolygón felmérést készítettünk arról, hogy az egyes állatok mit esznek. Megfigyelték, hogy vannak olyan állatok, amelyek csak növényeket esznek, de vannak olyanok is, amelyek más állatokat is esznek. A növények nem esznek semmit. Készíts programot, amely kiválasztja azokat az állatokat, amelyek csak növényeket esznek!

### Bemenet

A bemenet első sorában egy egész szám van: $N$ &ndash; az állatpárok száma. Az állatpárokat pontosan egy szóköz választja el egymástól. Jelentésük: az első megeszi a másodikat.

### Kimenet

A kimenet első sorába a csak növényeket evő állatok számot kell írni, a következő sorokba ezen állatok nevét.

### Korlátok

- $1 \le N \le 100$
- A nevek angol kisbetűkből állnak, legfeljebb 10 karakter hosszúak.

### Példa bemenet

    7
    roka fogoly
    roka galamb
    fogoly foldigiliszta
    csiga uborka
    galamb csiga
    foldigiliszta falevel
    sargarigó mag

### Példa kimenet

    3
    csiga
    foldigiliszta
    sargarigo

### A példa magyarázata

A csiga csak uborkát eszik, amely növény, mivel nem szerepel a párok első helyén, hasonlóan a foldigilisztához, amely falevelet eszik, ami növény, valamint a sárgarigóhoz, amely magot eszik. A róka, a fogoly és a galamb olyanokat is eszik, amelyek a párok elején szerepelnek, tehát állatok.
