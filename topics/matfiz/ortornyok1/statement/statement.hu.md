# Feladat I. – A király őrtornyai

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
