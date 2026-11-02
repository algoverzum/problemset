# Feladat II. – A király őrtornyai (C++)

A király átnézte az összes lehetséges őrbeosztást, és azt szeretné kiválasztani, amelyben a lehető legtöbb toronyban áll őr.

Feladatod meghatározni azt az őrbeosztást,

- amelyben egyetlen tiltott toronypár sem szerepel egyszerre;

- amely a lehető legtöbb tornyot tartalmaz.

Ha több maximális őrbeosztás is létezik, akkor a **lexikografikusan legkisebbet** kell kiírni.

Két őrbeosztás összehasonlításakor a kisebb első eltérő toronyszámot tartalmazó tekintendő lexikografikusan kisebbnek. Ha az egyik a másik prefixe (előtagja), akkor a rövidebb tekintendő kisebbnek.

## Bemenet

A standard input első sorában két egész szám található: $N$ és $M$, ahol

- $N$ az őrtornyok száma,

- $M$ a tiltott toronypárok száma.

A következő $M$ sor mindegyike két egész számot tartalmaz: $a$ és $b$, ami azt jelenti, hogy az $a$ és $b$ sorszámú torony egyszerre nem őrizhető.

**Korlátok**

- $1 \le N \le 25$

- $0 \le M \le 100$

## Kimenet

Az első sorba írd ki a maximális őrbeosztás méretét!

A második sorba írd ki a kiválasztott tornyok sorszámait növekvő sorrendben.

## Példa

### Bemenet

``` text
6 5
1 2
1 4
2 3
3 6
5 6
```

### Kimenet

``` text
3
1 3 5
```

## Magyarázat

A példában három toronynál nagyobb érvényes őrbeosztás nem létezik. Háromelemű érvényes őrbeosztásból négy is van: $\{1, 3, 5\}$, $\{2, 4, 5\}$, $\{2, 4, 6\}$ és $\{3, 4, 5\}$. Ezek közül az $\{1, 3, 5\}$ a lexikografikusan legkisebb, ezért ezt kell kiírni.

## Hint 1

Ismét három vector kellene: `forbidden` a tiltott párokra (minden toronyhoz a vele ütköző tornyok listája), valamint kettő az aktuális és a legjobb tornyokra: `current`, `best`.

## Hint 2

Mielőtt kiválasztasz egy új tornyot, ellenőrizd, hogy nem ütközik-e valamelyik korábban kiválasztott toronnyal.

## Hint 3

Alkalmazz **pruning** technikát!

Ha az aktuális részmegoldásban eddig $x$ tornyot választottál ki, még legfeljebb $r$ torony választható, és már ismert egy $k$ méretű megoldás, akkor

$$x+r < k$$

esetén ezen az ágon már biztosan nem található jobb megoldás.

## Hint 4

Ha

$$x+r = k,$$

akkor is elhagyható az ág, amennyiben a belőle előállítható legjobb megoldás sem lehet lexikografikusan kisebb a már megtaláltnál. (Ez egy további vágási lehetőség; a lenti megoldás csak a Hint 3-ban leírt vágást alkalmazza, egyenlőség esetén tovább keres.)

## Hint 5

A lexikografikus összehasonlításhoz érdemes egy külön függvényt írni! Pl.

``` text
bool lexicographicallySmaller(const vector<int> &a,
                              const vector<int> &b) {
    return a < b;
}
```

A `vector`-ok `<` operátora éppen lexikografikusan hasonlít.
