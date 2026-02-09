## Könyvtári katalógus rendezés

Egy könyvtárban $N$ könyv van, mindegyiknek ismert a címe és a kiadási éve. A könyvtáros szeretné a könyveket úgy elrendezni a polcon, hogy:
1. kiadási év szerint növekvő sorrendben legyenek,
2. ha az év megegyezik, akkor cím szerint ábécérendben.

### Bemenet
Az első sorban egy egész szám szerepel, $N$ &ndash; a könyvek száma.

Ezután $N$ sor következik, mindegyikben egy könyv adatai: a könyv címe és a kiadási éve. A könyvcím szóköz nélküli szöveg, a kiadási év pedig egy egész szám.

### Korlátok
- $1 \le N \le 1000$
- $1000 \le év \le 2024$

### Kimenet
A könyvek rendezve a megadott sorrendben.

### Példa bemenet

    5
    Algoritmusok 2010
    Adatszerkezetek 2010
    Python_kezdoknek 2018
    Mesterseges_intelligencia 2020
    Programozas_alapjai 2010

### Példa kimenet

    Adatszerkezetek 2010
    Algoritmusok 2010
    Programozas_alapjai 2010
    Python_kezdoknek 2018
    Mesterseges_intelligencia 2020
