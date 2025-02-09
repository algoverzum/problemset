## Csillagkapuk
Egy eldugott csillagrendszerben egy lelkes kutatócsapat rábukkant egy ősi csillagkapu hálózatra. Ezek a kapuk kétirányú utazást tesznek lehetővé, azonban minden használat után egy hosszabb ideig bezárulnak. A csapat célja egyszerű volt: biztosra akar menni, hogy minden kapu hibátlanul működik, ezért úgy döntöttek, hogy végigutaznak az egész hálózaton. Ugyanakkor tudják, hogy a csapdába esés elkerülése érdekében az utolsó kapun keresztül kell hazajutniuk. Szerencsére van egy listájuk, hogy melyik csillagkapu a csillagrendszer melyik két bolygóját köti össze. Segíts a kutatócsapatnak a lista alapján eldönteni, hogy lehetséges-e ilyen módon bejárniuk a csillagkapu hálózatot.

### Bemenet
A bemenetben első sorában két egész szám van: $N$ a rendszerben lévő bolygók száma és $R$ a csillagkapuk száma. <br>
Ezt követi $R$ sor, minden sorban két különböző szám $V1$ és $V2$ a két bolygó amiket az él összeköt

### Kimenet
Egyetlen szót kell kiírnod. $YES$, ha van ilyen bejárás, $NO$, ha nincs.

### Korlátok
* $1 \le N \le 200$
* $1 \le R \le 10000$
* $1 \le V1,V2 \le N$

### Példa bemenet
    5 6
    2 1
    1 3
    2 5
    1 4
    3 4
    5 1

### Példa kimenet
    YES

### A példa magyarázata
Egy lehetséges bejárás például az:<br>
1->2->5->1->4->3->1
