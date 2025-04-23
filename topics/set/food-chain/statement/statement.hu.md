## Tápláléklánc
A Zorgatron–7 bolygón vagyunk. Élőlényeket vizsgálunk, és azt, hogy mit esznek. Vannak, amik növényeket esznek. Vannak, amik más állatokat. És vannak, amik mindkettőt.

Minden adat, amit találtunk, egy **táplálkozási pár**: az első lény **megeszi** a másodikat. Például:  

- `nebbi slug` azt jelenti, hogy a **nebbi** megeszi a **slug**-ot.  
- `slug moss` azt jelenti, hogy a **slug** megeszi a **moss**-t (ami egy növény).  


Minden lényt, aki **eszik valamit**, **állatnak** nevezünk. Ami **nem eszik semmit**, az egy **növény**.

Vannak állatok, amik más állatokat esznek. Őket **ragadozóknak** nevezzük. A feladatod: keresd meg az összes **ragadozót**!

### Bemenet
Az első sorban egy szám van, $N$: a táplálkozási párok száma.  A következő $N$ sor mindegyike egy párt tartalmaz: két szót, szóközzel elválasztva: az első szó az **evő**, a második szó az **étel** (amit megesznek).

### Kimenet
Az első sorban írd ki a ragadozók számát. Utána minden ragadozó nevét külön sorba, a nevek **ábécérendben** legyenek. Ha nincs egy ragadozó sem, akkor csak egy `0`-t írj ki.

### Korlátok
* $1 \le N \le 100$
* A nevek angol kisbetűkből állnak, legfeljebb 10 karakter hosszúak.

### Példa bemenet
    7
    drak puffin
    drak nebbi
    puffin grub
    slug moss
    nebbi slug
    grub root
    nebbi seed

### Példa kimenet
    3
    drak
    nebbi
    puffin

### A példa magyarázata
- **moss**, **root** és **seed** nevű lényeket senki sem eszi meg → ők **növények**.  
- **slug** megeszi a **moss**-t → növényt eszik → **állat**.  
- **grub** megeszi a **root**-ot → növényt eszik → **állat**.  
- **puffin** megeszi a **grub**-ot → állatot eszik → **ragadozó**.  
- **nebbi** megeszi a **slug**-ot és a **seed**-et → eszik egy állatot → **ragadozó**.  
- **drak** megeszi a **puffin**-t és a **nebbi**-t → mindkettő állat → **ragadozó**.

A ragadozók tehát:  
**drak**, **nebbi**, **puffin**.
