## Legrövidebb kör
A Kuklos bolygón a városokat utak kötik össze. Mi az egyik ilyen városban élünk, és hogy biztosítsuk a napi testmozgást, szeretnénk egy sétát tenni. Azonban nem szeretnénk unatkozni, ezért egy úton csak egyszer haladhatunk át. A sétát úgy tervezzük, hogy a kiindulási városunkba visszatérve fejeződjön be. Mivel ma fáradtak vagyunk, a lehető legrövidebb ilyen sétát keressük. Határozzuk meg, milyen hosszú a legrövidebb séta, és mely városokat érinti! Ha több azonos hosszúságú séta is létezik, bármelyik megadható.

### Bemenet
A bemenet első sorában három egész szám van: $N$ a városok száma, $M$ az utak száma és $P$ a város ahol élünk. <br>
A következő $M$ sor mindegyike két számot tartalmaz, amelyek egy-egy összekötött várost jelölnek.

### Kimenet
A kimenet első sorába egyetlen számot kell kiírnod a $P$ városon átmenő legrövidebb kör $K$ hosszát kell írni! . Ha nincs ilyen kör akkor $-1$-et.<br>
A második sor $K$ darab különböző pont sorszámát tartalmazza, amelyek ebben a sorrendben a bemeneti gráf egy $K$
hosszú körét alkotják, ha hozzávesszük az utolsó pontból az elsőbe vezető élet is!
Több megoldás esetén bármelyik megadható.

### Korlátok
* $1 \le N \le 100000$
* $1 \le M \le 200000$
* $1 \le P \le N$

### Példa bemenet
    8 10 2
    1 3
    3 6
    3 2
    2 4
    2 5
    6 7
    6 8
    1 8
    5 3
    4 7


### Példa kimenet
    3
    2 5 3

### A példa magyarázata
    A legrövidebb kör az alábbi utakból áll: 2–5, 5–3 és 3–2.
    A városokat bármilyen sorrendben megadhatjuk, amíg a megadott lista továbbra is egy kört alkot.
    Például az 5 2 3 szintén egy érvényes megoldás.
