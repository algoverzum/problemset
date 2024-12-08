## Első előfordulás
Az űrkutató Gammos flottaparancsnok egy rejtélyes rádióüzenetet fogott a távoli Végtelen Szektor pereméről. Az üzenet egyetlen szóból áll, és egy fontos koordinátát rejt. Gammosnak meg kell találnia, hogy a megadott kulcsbetű először hol jelenik meg az üzenetben, hogy megfejthesse az irányt, amerre az expedíciót vezetnie kell. Ha a kulcsbetű nem szerepel az üzenetben, akkor az üzenet téves.

### Bemenet
Egy $S$ szó, amely az üzenet tartalmát jelöli.
Egy $C$ betű, amely a kulcsbetűt jelöli.

### Kimenet
Egyetlen számot kell kiírnod, a kulcsbetű utolsó előfordulásának helyét. Ha nem tartalmazza az $S$ szó a $C$ kulcsbetűt akkor -1-et kell kiírnod.

### Korlátok
Az $S$ szó az angol ábécé betűiből áll és legfeljebb 1000 betű hosszú. A betűk lehetnek kicsik és nagyok is.
A $C$ kulcsbetű egy kis- vagy nagybetű az angol ábécéből.

### Példa bemenet
    Surreptitious  
    u

### Példa kimenet
    2

### A példa magyarázata
    Surreptitious 13 betű hosszú. az 'u' karakter a 2. helyen fordul elő először.
