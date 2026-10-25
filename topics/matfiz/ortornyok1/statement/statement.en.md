# Feladat I. – A király őrtornyai (Python)

A Számok Királyságának határán $N$ őrtorony áll. A király minden toronyba szeretne őrt állítani, azonban bizonyos tornyok egyszerre nem őrizhetők, mert jelzőtüzeik megzavarnák egymást.

Egy *őrbeosztás* a tornyok egy olyan részhalmaza, amelyben egyetlen tiltott toronypár sem szerepel egyszerre.

Feladatod az összes lehetséges őrbeosztás előállítása.

## Bemenet

Az első sor két egész számot tartalmaz: $N$ és $M$, ahol

- $N$ az őrtornyok száma,

- $M$ a tiltott toronypárok száma.

A következő $M$ sor mindegyike két egész számot tartalmaz: $a$ és $b$, ami azt jelenti, hogy az $a$ és $b$ sorszámú torony egyszerre nem őrizhető.

**Korlátok**

- $1 \le N \le 20$

- $0 \le M \le 100$

## Kimenet

Első sor:

Az érvényes őrbeosztások száma.

Ezután minden őrbeosztást külön sorba kell kiírni.

A tornyok sorszámai minden sorban növekvő sorrendben szerepeljenek.

Az üres őrbeosztást (egy üres sort) elsőként kell kiírni. A nem üres őrbeosztásokat ezután lexikografikus sorrendben kell megjeleníteni.

## Példa

### Bemenet

``` text
4 2
1 2
2 3
```

### Kimenet

``` text
10

1
1 3
1 3 4
1 4
2
2 4
3
3 4
4
```

## Hint 1

Használj egy logikai értékeket tartalmazó kétdimenziós listát (`tiltott = [[False] * (N + 1) for _ in range(N + 1)]`), amely tárolja, hogy mely tornyok nem lehetnek együtt! Az aktuális őrbeosztás tornyainak sorszámait az `aktualis`, a kész őrbeosztásokat a `megoldasok` lista tárolja.

## Hint 2

Írj egy függvényt (`lehet`), amely ellenőrzi, hogy az `idx` torony felvehető-e a jelenlegi részhalmazba! Ehhez az `aktualis` elemein kell végigmenned, és megnézned, hogy valamelyik `t` elemre igaz-e a `tiltott[idx][t]`.

## Hint 3

A backtrack eljárásban minden toronyról döntünk, hogy bekerül-e. Két ág van: az `idx` tornyot vagy bevesszük (ha lehet), vagy kihagyjuk. Ha `idx > N`, akkor már minden toronyról döntöttünk, tehát az aktuális részhalmaz egy kész őrbeosztás. Ilyenkor másolatot ments (`aktualis[:]`), mert az `aktualis` lista később tovább változik!

## Hint 4

Az 1. ágon: `if lehet(idx):`, azaz megnézzük, hogy az `idx` kiválasztható-e. Ha igen, betesszük (`append`), meghívjuk a `backtrack(idx + 1)`-et, majd kivesszük (`pop`). A 2. ágon az `idx` tornyot NEM választjuk ki: `backtrack(idx + 1)`.

## Hint 5

Ez a bejárási sorrend nem lexikografikus (például az `1 3` előbb készül el, mint az `1`), ezért a végén rendezd a megoldásokat (`megoldasok.sort()`)! Pythonban a listák rendezése lexikografikus, és az üres lista automatikusan az első lesz.

## Hint 6 (Python)

$N = 20$ és $M = 0$ esetén $2^{20} = 1\,048\,576$ őrbeosztást kell kiírni. A sorokat gyűjtsd egy listába, és a végén egyetlen `print("\n".join(kimenet))` hívással írd ki, mert a sok külön `print()` hívás lassú.
