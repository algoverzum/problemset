## Legnagyobb mennyiségű teavásárlás
Egy élelmiszerdiszkontban nyilvántartást vezetnek a teavásárlásról. Minden vásárlásnál feljegyzik, hogy milyen cég teájából milyen mennyiséget vettek.

A feladat: Készíts programot, amely **megadja a legnagyobb mennyiségű vásárlás sorszámát**!

Ha több vásárlás is rendelkezik a legnagyobb mennyiséggel, akkor a **legkisebb sorszámút** kell kiírni.

### Bemenet
A bemenet első sora tartalmazza $N$ értékét, az árusító helyek számát, majd $N$ darab **sorpár**, mindegyik tartalmazza:  

1. a teafajta neve (szöveg)
2. a vásárolt mennyiség $M$

### Kimenet
A standard kimenet **első sorába** a legnagyobb mennyiségű vásárlás sorszámát kell kiírni!
Több azonos maximum esetén a **legkisebb sorszámú** ilyen vásárlást kell kiírni.

### Korlátok

- $1 \le N \le 100$
- $1 \le M \le 20000$

### Példa bemenet
    6
    Lipton
    200
    Teekanne
    100
    Lipton
    600
    Lipton
    800
    Pickwick
    200
    Greenfield
    800

### Példa kimenet
    4

### Magyarázat
Két 800-as van, de a 4. van előbb (Lipton), nem pedig a 6. (Greenfield)
