## Nem túl sok kéz
A bolygónkon sokféle intelligens lény él, változatos számú kezekkel. Nagyon népszerű sport a birkózás, és a birkózó világbajnokságon $N$ lény szeretne indulni. Őket 1-től $N$-ig sorszámozzuk, és mindegyiküknek ismert a kezeik száma: $H_1, H_2, \ldots, H_N$. Az igazságosság érdekében a versenybizottság úgy döntött, hogy csak azok a birkózók indulhatnak, akiknek legfeljebb 4 kezük van. Meg tudod adni, hogy hányan és kik indulhatnak?

### Bemenet
A bemenetben első sorában egy egész szám van: $N$ - a versenyre nevezők száma. A második sorban $N$ egész szám van szóközzel elválasztva, az egyes nevezők kezeinek száma ($H_1, H_2, \ldots, H_N$)

### Kimenet
A kimenet első sorába írd azon versenyzők számát, akik elindulhatnak. A második sorban sorold fel a sorszámaikat, növekvő sorrendben, szóközzel elválasztva. 

### Korlátok
* $1 \le N \le 100$
* $0 \le H_i \le 10$

### Példa bemenet
    9
    4 7 3 5 5 7 2 0 10

### Példa kimenet
    4
    1 3 7 8

### A példa magyarázata
4 versenyző van, akiknek legfeljebb 4 keze van, az 1., 3., 7. és 8. versenyző (a kezeik száma sorrendben 4, 3, 2, 0).
