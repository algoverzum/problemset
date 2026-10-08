## Fordított lengyel jelölés
A matematikai kifejezéseket általában infix alakban írjuk fel:
(3 + 4) * 2

**Megjegyzés**: Infix esetében a műveleti jel (operátor, mint a +, -, ×, ÷) a két szám (operandus) között helyezkedik el.

Létezik azonban egy másik forma is, az úgynevezett **fordított lengyel jelölés** (Reverse Polish Notation, RPN), ahol az operátor az operandusok után szerepel:

3 4 + 2 *


A fenti kifejezés jelentése:

$(3+4)\cdot 2$

amelynek értéke:

**14**

Írjunk programot, amely egy fordított lengyel jelöléssel megadott kifejezés értékét számolja ki!

### Bemenet
- A standard bemenet egyetlen sorában egy fordított lengyel jelölésű kifejezés található.
- A kifejezés elemei szóközzel vannak elválasztva.
- Az operandusok nemnegatív egész számok.
- Az operátorok a következők lehetnek: `+ - * /`
- Feltételezhetjük, hogy a kifejezés helyes.

### Kimenet
A kifejezés értékét kell kiírni.

### Korlátok
- A kifejezés legfeljebb 100 elemből (számból vagy operátorból) áll.
- Az eredmény belefér egy 32 bites előjeles egész számba.
- Az osztás egész osztás.

### Példa bemenet
    3 4 + 2 *

### Példa kimenet
    14

### A példa magyarázata
$3+4=7$, majd $7\cdot 2=14$

### Második példa
    5 1 2 + 4 * + 3 -

### Kimenet
    14

### A példa magyarázata

Először: $1+2=3$, majd $3\cdot 4=12$.
Ezután: $5+12=17$, végül $17-3=14$

### Hint 1
Ha számot olvasunk, tegyük el későbbre.

### Hint 2
Ha operátort olvasunk, szükségünk lesz a két legutóbb eltárolt számra.

### Hint 3
Melyik adatszerkezet tudja hatékonyan kezelni a "legutóbb betett elem legyen az elsőként kivett" működést?

### Hint 4
Az operátor feldolgozásakor:
- vegyük ki a legfelső elemet,
- majd a következőt,
- végezzük el a műveletet,
- az eredményt tegyük vissza.