## Legrövidebb útfelújítás

Egy $N$ kilométer hosszú utat rossz állapota miatt szakaszonként újraaszfaltoznak. Az aszfaltozást $M$ alkalommal végzik. Minden alkalomról tudjuk, hogy melyik kilométertől ($K_i$) melyik kilométerig ($V_i$) terjedő szakaszt aszfaltoznak.

Írj programot, amely megadja a legrövidebb felújítás hosszát!  Ha több ilyen is van, akkor az összeset meg kell adnod!

### Bemenet

A standard bemenet első sorában az út hossza ($N$) és a felújítások száma ($M$) van, alatta soronként egy-egy felújítás adatai ($K_i$, $V_i$).

### Kimenet

A standard kimenet első sorába egyetlen egész számot kell írni, a legrövidebb felújítás hosszát!  

A következő sor(ok)ba pedig a felújítás sorszámát! Ha több azonos legrövidebb van, akkor ezek sorszámát külön sorokba kell írnod, növekvő sorrendben!

### Korlátok

- $1 \le N \le 100000$
- $1 \le M \le 100$
- $0 \le K_i \le V_i \le N$

### Példa bemenet

    100 5
    0 1
    0 5
    75 95
    12 17
    13 14

### Példa kimenet

    2
    1
    5

### A példa magyarázata

Mivel a 0–1 és a 13–14 is 2 kilométer hosszú felújítást jelent, ezért ez van az első sorban. A következő két sorban pedig ezek sorszámai, 1 és 5.
