## Első szó
Coruscanon egy droid összeszerelősor meghibásodott, a memóriamagja megzavarodott. Összefüggő utasítások helyett galaktikus kifejezések véletlenszerű sorozatait kezdi generálni. A droidgyár működésének helyreállítása érdekében a lázadó szeletelőnek meg kell találnia a memóriamagból az ábécé szerint első kifejezést a kódolt szavak listáján.
Adott a droid által előállított szavak listája, határozd meg az ábécé szerint első szót.

### Bemenet
A bemenet első sora $N$ - a szavak számát tartalmazza.
A második sor $N$ szóközzel elválasztott szavakat tartalmaz. Minden szó csak kisbetűket tartalmaz.

### Kimenet
Egyetlen szót kell kiírnod, az első szó ábécé sorrendben.

### Korlátok
* $1 \le N \le 100$
* minden szó csak kisbetűket tartalmaz

### 1. Példa bemenet
    5
    how preach coarse at descent

### 1. Példa kimenet
    at

### 1. példa magyarázata
Csak egy "a" betűvel kezdődő szó van.

### 2. Példa bemenet
    6    
    who wise whose western weekend would

### 2. Példa kimenet
    weekend

### 2. példa magyarázata
Minden szó "w"-vel kezdődik, a második betűt kell megnéznünk. Kettő közülük "we"-vel kezdődik, tehát még a harmadik betűt is figyelembe kell vennünk.
