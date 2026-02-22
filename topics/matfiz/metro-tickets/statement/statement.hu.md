## Tom és a metrójegyek – érmepárok összege

Tom meglátogatja Jennyt, és úgy döntött, hogy metróval megy hozzá.  
A jegyet csak egy olyan automatánál lehet megvenni, amely **pontosan két érmét** fogad el, amelyek összege nem haladja meg $k$-t.

Tomnak két zsebében vannak érmék.  
A bal zsebében $n$ érme van: értékeik $b_1, b_2, \dots, b_n$.  
A jobb zsebében $m$ érme van: értékeik $c_1, c_2, \dots, c_m$.

Pontosan **egy** érmét akar választani a bal zsebéből és **egy** érmét a jobb zsebéből.  
Segíts Tomnak meghatározni, hogy hányféleképpen lehet úgy kiválasztani az $f$ és $s$ indexeket, hogy:

\[
b_f + c_s \le k
\]

### Bemenet
Az első sor: egy egész szám $t$ &ndash; a tesztesetek száma.

Minden teszteset első sora három egész számot tartalmaz:  $n$, $m$ és $k$ &ndash; a bal és a jobb zsebben lévő érmék száma, valamint a pénztárnál a jegy kifizetéséhez szükséges két érme maximális összege.

Minden teszteset második sora $n$ db egész számot tartalmaz, ahol $b_1, \dots, b_n$ a bal zsebben lévő érmék címletei.

Minden teszteset harmadik sora $m$ db egész számot tartalmaz: a jobb zseb érméit: $c_1, \dots, c_m$.

### Kimenet
Minden tesztesethez egy sort kell kiírni:  
a két választott érmére vonatkozó **érvényes indexpárok száma**, ahol a feltétel teljesül:
\[b[i] + c[j] \le k \].

Azaz, hányféleképpen választhat ki két érmét Tom úgy, hogy mindkét zsebéből kivesz egyet és az érmék összege nem haladja meg $k$ értékét.


### Korlátok
- $1 \le t \le 100$
- $1 \le n, m \le 100$
- $1 \le k \le 2000$
- $1 \le b_i \le 1000$
- $1 \le c_i \le 1000$

### Példa bemenet
    4
    4 4 8
    1 5 10 14
    2 1 8 1
    2 3 4
    4 8
    1 2 3
    4 2 7
    1 1 1 1
    2 7
    3 4 2000
    1 1 1
    1 1 1 1

### Példa kimenet
    6
    0
    4
    12


### A példa magyarázata

Vegyük észre, hogy a párok az érmék **indexeit** jelölik a tömbben, nem pedig a címletüket!

#### 1. teszteset
Az első tesztesetben Tom a következő érmepárokat választhatja ki: $[1,1], [1,2], [1,4], [2,1], [2,2], [2,4]$, összesen **6** darabot.

#### 2. teszteset
Nincs olyan pár, amelyre $b[i] + c[j] \le 4$ → **0**.

#### 3. teszteset
Érvényesek: $[1,1], [2,1], [3,1], [4,1]$ → **4**.

#### 4. teszteset
Minden bal oldali érme kombinálható mind a 4 jobb oldali érmével → 3×4 = **12**.
