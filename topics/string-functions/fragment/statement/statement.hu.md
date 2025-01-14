## Töredék
A "Mars Explorer" nevű űrhajó fedélzetén található egy adatgyűjtő rendszer, amely különböző titkos üzeneteket fogad az űrből. Az űrhajó szoftverének feladata, hogy egy adott üzenetből kinyerjen egy részletet, ami egy adott betű első és utolsó előfordulása közé esik, a betű első és utolsó előfordulását is beleértve. Ha a megadott betű nem szerepel az üzenetben, akkor -1 kiírással kell jelezni a hibát. Tudsz segíteni ehhez a program megírásában?

### Bemenet
A bemenet első sorában egy $S$ string van, az üzenet. Nincsenek benne szóközök.
A második sorban pedig egy $C$ karakter.

### Kimenet
A $C$ karakter első és utolsó előfordulása közötti részét írjuk ki az $S$ stringnek, a karakter első és utolsó előfordulását is beleértve. Ha a $C$ karakter nem szerepel $S$-ben, akkor a kimenet legyen -1.

### Korlátok
* Az $S$ szó az angol ábécé kisbetűiből áll és maximum 1000 karakter hosszú.
* A $C$ karakter az angol ábécé egy kisbetűje.

### Példa bemenet
    fragmented
    e

### Példa kimenet
    ente

### 2. példa bemenet
    message
    m

### 2. példa kimenet
    m

### 3. példa bemenet
    hello
    x

### 3. példa kimenet
    -1
