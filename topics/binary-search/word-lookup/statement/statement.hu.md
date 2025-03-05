## Szókeresés

Bátor űrhajósaink egy furcsa bolygóra zuhantak le. A mogorva idegenek elvették a telefonjaikat, de szerencsére egy űrhajós titokban megtartott egy apró szótárt! Most szükségük van a segítségedre, hogy lefordítsanak egy üzenetet és meggyőzzék az idegeneket, hogy barátságosak. Fordítsd le az üzenetet gyorsan, mielőtt az idegenek mérgesek és gyanakvóak lesznek!

### Bemenet

Az első sor megadja, hány szópár van az űrhajósok szótárában. Ezt a számot nevezzük $N$-nek.
A következő $N$ sor mindegyike egy szópárt mutat: először az angol szót, majd egy szóköz után az idegen szót. A sorok ábécé sorrendben vannak az angol szavak szerint.
A következő sor megadja, hány szó van az üzenetben, amit az űrhajósoknak le kell fordítaniuk. Ezt a számot nevezzük $M$-nek.
A következő $M$ sor az üzenet angol szavait adja meg, egy szót soronként.

Minden angol szó az üzenetből benne lesz a szótárban.

### Kimenet

Írj ki $M$ sort, mindegyik az üzenet megfelelő angol szavának idegen fordításával.

### Korlátok

* $1 \le N \le 100\,000$
* $1 \le M \le 50\,000$
* Minden szó az angol ábécé kisbetűiből áll.
* Minden szó hossza 1 és 10 betű közt van.

### Példa bemenet
    5
    are borp
    friend zortan
    hello aloha
    planet kryton
    we glorp
    3
    we
    are
    friend

### Példa kimenet
    glorp
    borp
    zortan
