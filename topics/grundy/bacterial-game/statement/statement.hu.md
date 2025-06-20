## Baktérium Játék
Becca és Terry mikrobiológusok, akik baráti versengést folytatnak. Amikor szünetet tartanak a kutatásban, szeretnek együtt játszani egy játékot. A játékot egy egységcellákból álló mátrixon (táblázaton) játsszák, amely $R$ sorból és $C$ oszlopból áll. Kezdetben minden cella vagy üres, vagy radioaktív anyagot tartalmaz.

Minden játékos a saját körében, ha nincs több üres cella a mátrixon, elveszíti a játékot. Ellenkező esetben kiválaszt egy üres cellát, és oda baktériumkolóniát helyez el. A baktériumkolóniák kétféle típusúak lehetnek: $H$ (vízszintes) és $V$ (függőleges).

* Amikor egy $H$ típusú kolóniát helyeznek el egy üres cellába, az elfoglalja azt a cellát (így az nem üres többé), és megpróbál terjedni a közvetlenül nyugatra (ha van ilyen) és keletre lévő cellákba (ha van ilyen).
* Amikor egy $V$ típusú kolóniát helyeznek el egy üres cellába, az elfoglalja azt a cellát (így az nem üres többé), és megpróbál terjedni a közvetlenül délre (ha van ilyen) és északra lévő cellákba (ha van ilyen).

Amikor egy kolónia (bármely típusú) megpróbál terjedni egy cellába:

* Ha a cella **radioaktív anyagot** tartalmaz, a kolónia mutálódik, és az azt elhelyező játékos **elveszíti** a játékot.
* Ha a cella üres, a kolónia elfoglalja azt (így az nem üres többé), majd a fenti szabály újra érvénybe lép (vagyis a kolónia tovább próbál terjedni).
* Ha a cella már baktériumot tartalmaz (bármilyen típusút), a kolónia nem terjed be oda.

Fontos megjegyezni, hogy előfordulhat, hogy egy játékos számára az összes elérhető lépés vesztéssel jár, így menthetetlenül vesztésre van ítélve. Lásd az alábbi példákat a játék működésére.

Becca kezd, majd a két játékos felváltva lép, amíg egyikük el nem veszti a játékot. Ha mindketten optimálisan játszanak, ki fog nyerni?

### Bemenet
A bemenet első sora két egész számot tartalmaz: $R$ és $C$ – a mátrix (táblázat) sorainak és oszlopainak számát.

Ezután $R$ további sor következik, mindegyik $C$ karakterből áll. Az $i$-edik sor $j$-edik karaktere a mátrix $i$-edik sorának $j$-edik oszlopát jelöli. Minden karakter vagy '.' (üres cella), vagy '#' (radioaktív anyagot tartalmazó cella).

### Kimenet
Írd ki a nyertes nevét (Becca/Terry), feltételezve, hogy mindketten optimálisan játszanak, és Becca kezd.

### Korlátok
* $1 \le R,C \le 15$

### 1. Példa bemenet
    2 2
    ..
    .#

### 1. Példa kimenet
    Terry

### 1. Példa magyarázat
Becca nem tud $H$ kolóniát elhelyezni a délnyugati üres cellába vagy $V$ kolóniát az északkeleti cellába, mert ezek a kolóniák radioaktív cellákra terjednének, és Becca veszítene. Négy induló lépése van, amelyek nem okoznak azonnali vereséget:

* $H$ kolóniát helyez el az északnyugati vagy északkeleti cellába. A kolónia átterjed a másik cellára is.
* $V$ kolóniát helyez el az északnyugati vagy délnyugati cellába. A kolónia átterjed a másik cellára is.

Ha Becca az első lehetőséget ($H$) választja, Terry elhelyezhet egy $V$ kolóniát a délnyugati cellába.
Ha a másodikat ($V$), akkor Terry elhelyezhet egy $H$ kolóniát az északkeleti cellába.
Mindkét esetben Beccának nem marad üres cella, így veszít, azaz Terry nyer.

### 2. Példa bemenet
    4 4
    .#..
    ..#.
    #...
    ...#

### 2. Példa kimenet
    Terry

### 2. Példa magyarázat
Becca bármelyik kezdő lépése mutációt okozna.

### 3. Példa bemenet
    3 4
    #.##
    ....
    #.##

### 3. Példa kimenet
    Becca

### 3. Példa magyarázat
Becca nyitó lépéseinek öt változata mutációhoz vezet, de hét másik nyerő. Elhelyezhet $H$ kolóniát a második sor bármely cellájában, vagy $V$ kolóniát a második oszlop bármely cellájában. Mindkét esetben két különálló cellahalmaz jön létre. Ezekben csak egyfajta kolónia helyezhető el, és az összes cellát elfoglalja. Bárhogy is dönt Terry, Becca ki tudja használni a másik halmazt, így Terrynek nem marad lépése.

### 4. Példa bemenet
    1 1
    .

### 4. Példa kimenet
    Becca

### 4. Példa magyarázat
Becca mindkét nyitó lépése (akár $H$, akár $V$) nyerő.

### 5. Példa bemenet
    1 2
    ##

### 5. Példa kimenet
    Terry

### 5. Példa magyarázat
Becca nem tud lépni az elején.
