## Karakter törlés
A "NOVA" űrprogram keretében egy távoli bolygóról érkező titkosított üzenetet fogtunk. Az üzenetben van egy szó, ami egy különleges kód, és dekódolás előtt meg kell tisztítani a zajtól. A zajforrás egy konkrét betű, ami többször előfordulhat az üzenetben, és minden előfordulását el kell távolítani, hogy a dekódoló algoritmus megkezdhesse a munkát. Tudsz erre a feladatra programot írni?

### Bemenet
A bemenet első sorában egy $S$ szó van.
A második sorában pedig egy $C$ karakter.

### Kimenet
Írjuk ki az $S$ stringet, miután a $C$ karakter összes előfordulását töröltük. Lehet, hogy üres string lesz belőle, ekkor egy üres sor legyen a kimenet.

### Korlátok
* Az $S$ szó az angol ábécé kisbetűiből áll és maximum 1000 karakter hosszú.
* A $C$ karakter az angol ábécé egy kisbetűje.

### Példa bemenet
    delete
    e

### Példa kimenet
    dlt
