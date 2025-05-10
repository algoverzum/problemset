## Utolsó előfordulás 
A bolygóközi flottának egy régi, sérült adatbázist kell helyreállítania, amely fontos navigációs adatokat tartalmaz. Az adatbázis elemzése közben rájöttek, hogy egy kulcsbetű mindig elárulja az adott adatcsomag utolsó érvényes jelzésének helyét. A mérnökcsapat most téged kért meg arra, hogy találj meg egy szóból egy adott betű utolsó előfordulásának helyét, hogy helyre tudják állítani a megfelelő adatokat. Ha a betű hiányzik, az adatcsomag sajnos használhatatlan.

### Bemenet
A bemenet első sorában egy $S$ szó van, az üzenet tartalma.
A bemenet második sorában egy $C$ betű van, a kulcsbetű.

### Kimenet
Egyetlen számot kell kiírnod, a kulcsbetű utolsó előfordulásának helyét. Ha nem tartalmazza az $S$ szó a $C$ kulcsbetűt akkor -1-et kell kiírnod.

### Korlátok
Az $S$ szó az angol ábécé kisbetűiből áll és legfeljebb 1000 betű hosszú.
A $C$ kulcsbetű egy kisbetű az angol ábécéből.

### Példa bemenet
    incomprehensibilities 
    i

### Példa kimenet
    19

### A példa magyarázata
`incomprehensibilities` 21 betű hosszú. Az `i` karakter a 19. helyen fordul elő utoljára.
