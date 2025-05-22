## Birodalmi örökség
A Galaktikus Birodalom uralkodója váratlanul eltűnt egy fekete lyuk peremén zajló diplomáciai küldetés során. Trónörökös nélkül, a Birodalmi Tanács úgy döntött, hogy a két törvényes örökös, Seran és Kaela, megosztva örökli a birodalom legértékesebb erőforrásait: a bolygókat.

Minden bolygónak ismert az értéke, amit egy pozitív egész számmal jellemeznek. A testvérek igazságos örökségre törekednek, tehát olyan elosztást keresnek, ahol mindketten ugyanakkora összértékű bolygót birtokolnak.

Hamar rájöttek azonban, hogy ez nem mindig lehetséges – ezért elfogadják azt is, ha néhány bolygó egyelőre közös felügyelet alatt marad. Segíts a trónörökösöknek igazságosan szétosztani a bolygókat, hogy a közös felügyelet alatt maradó bolygók összértéke minimális legyen.


### Bemenet
A standard bemenet első sorában egy egész szám szerepel: $N$ a bolygók száma.  
A második sor pontosan $N$ darab pozitív egész számot tartalmaz: $B_i$.  
A bolygók összértéke legfeljebb 10000.

### Kimenet
A standard kimenet első sorába írd ki a közösben maradó (nem elosztott) bolygók összértékét.  
A második és harmadik sorba írd ki azoknak a bolygóknak a sorszámát (1-től kezdve), amelyeket az egyik, illetve a másik örökös kapott. Több megfelelő megoldás is létezhet — bármelyik elfogadható.


### Korlátok
* $1 \le N \le 300$
* $\sum B_i \le 10\,000$

### Példa bemenet
    7  
    16 3 11 38 1 4 2

### Példa kimenet
    39
    1 7
    3 2 6

### A példa magyarázata
<span style="color:red">16 </span><span style="color:aqua">3 11 </span>38 1 <span style="color:aqua">4 </span> <span style="color:red">2 </span><br>
A 38 és 1 értékű bolygót nem tudták elosztani igazságosan, ezek összértéke 39. A két trónörökös egyaránt 18 értékű bolygót kapott.