### Hint 1
Az osztás operátora a C++-ban a `/`. Ha a két operandus egész szám, az eredmény is egész lesz, ami azt jelenti, hogy a törtrészt eldobja. (Ennél a feladatnál ez nagyon hasznos.) Az osztási maradék a `%` operátorral számolható ki, amit modulo operátornak is hívnak. Például `13 / 5 = 2` (nem 2.6), és `13 % 5 = 3`, mivel `13 = 2 * 5 + 3`.

### Hint 2
A két szám közé szóközt kell tennünk, amikor kiírjuk őket. Szöveget úgy lehet kiírni, ha idézőjelek közé tesszük, így egy szóközt a `cout << " ";` paranccsal tudunk kiírni. A teljes kötél hossza 1337cm. Ezt el kell osztanunk 42-vel, hogy megkapjuk az első választ, és vennünk kell a maradékot 42-vel, hogy megkapjuk a második választ.

### Hint 3
    cout << 1337 / 42;
    cout << " ";
    cout << 1337 % 42;
