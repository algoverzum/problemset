## Második előfordulás
Egy távoli expedíción lévő űrhajó kódolt üzeneteket küld vissza egy űrállomásra azonos időközönként. Ezek az üzenetek egy-egy angol kisbetűből állnak, amiket egy stringbe fűztünk. Az üzeneteket 0-tól kezdve sorszámozzuk. Készíts egy programot, ami megállapítja, hogy hányadik üzenet volt a második előfordulása az `x` kódnak. Ha csak egyszer fordult elő `x` kód, akkor a kimenet -1, ha pedig egyszer sem, akkor pedig -2.

### Bemenet
A bemenetben egyetlen string van, a kódok egybe fűzve: $S$

### Kimenet
Egyetlen számot kell kiírnod, a második `x` karakter pozícióját, ha van legalább kettő. Ha csak egy van, akkor a kiírandó szám a -1, ha egy sincsen, akkor pedig a -2.

### Korlátok
* $1 \le S$ $hossza \le 256$
* S csak az angol ábécé kisbetűit tartalmazza

### Példa bemenet
    aqwaxgxd

### Példa kimenet
    6

### A példa magyarázata
A második `x` karakter indexe a 6.
