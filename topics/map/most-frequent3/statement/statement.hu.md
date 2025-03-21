## Leggyakoribb
Moseyslee űrkikötője szokatlanul nagy forgalmat tapasztal. A Lázadók Szövetsége egy titkos üzenetet kapott egy beépített ügynökétől: a Birodalom rejtett tevékenységet folytat a kikötőben.

R2-D2 és C-3PO hozzáférnek az állomás érkezési adataihoz - egy hosszú listához, amely az elmúlt időszakban dokkolt űrhajók neveit tartalmazza. Ha sikerül meghatározni azt az űrhajót, amely a legtöbbször jelent meg, az kulcsfontosságú lehet a rejtély megoldásában.

### Bemenet
A bemenet első sora $N$, a listán szereplő nevek száma.
Ezt követi $N$ sor, az űrhajók nevei.

### Kimenet
Az első sorba írd ki, hogy a listán szereplő leggyakoribb név hányszor szerepel a listán.
Az ezt követő sorokba pedig ábécé sorrendben az összes leggyakrabban szereplő űrhajó nevét (soronként egyet).

### Korlátok
* $1 \le N \le 10^5$
* minden űrhajó neve az angol ábécé kisbetűit tartalmazza, és legfeljebb 25-öt
* különböző űrhajók neve is garantáltan különböző 

### Példa bemenet
    8
    naboostarfighter
    millenniumfalcon
    ghost
    naboostarfighter
    millenniumfalcon
    ghost
    naboostarfighter
    millenniumfalcon 

### Példa kimenet
    3
    millenniumfalcon
    naboostarfighter

### A példa magyarázata
A naboostarfighter és a millenniumfalcon is háromszor szerepel a listán.
