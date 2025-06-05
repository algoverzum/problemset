## Terraformálási ajánlatok
Az Ereus Kolónia új terraformáló állomásokat kíván építeni különböző bolygókon és holdakon. Ennek érdekében a Kolóniai Tanács nyilvános licitet hirdetett meg vállalatok számára.

Minden pályázó vállalat megadta a nevét, valamint a kivitelezéshez szükséges becsült költséget. A Tanács a beérkezett ajánlatokat költség szerint növekvő sorrendbe kívánja rendezni. Ha több cég azonos költséget adott meg, akkor  közöttük a vállalatok nevét ábécé sorrendbe kell rendezni.

### Bemenet
A bemenet első sorában egy egész szám szerepel: $N$ – az ajánlatok száma.  
A következő $N$ sor mindegyikében két adat van:  
* egy legfeljebb 10 karakter hosszú $C_i$ szó – a cég neve,  
* és egy $B_i$ pozitív egész szám – az adott cég árajánlata.


### Kimenet
Írj ki $N$ sort, mindegyik sorba egy cég nevét!  
A cégeket az ajánlatuk szerint növekvő sorrendben kell kiírni.  
Azonos ajánlat esetén a név szerinti ábécérend dönt.

### Korlátok
* $1 \le N \le 100\,000$  
* $1 \le B_i \le 100\,000$  minden $i=1 \dots N$ esetén
* $C_i$ minden $i=1 \dots N$ esetén legfeljebb 10 kisbetűs angol karakterből álló szó.  
Minden cég neve csak egyszer szerepelhet.

### Példa bemenet
    5
    oriontech 12000
    aerodyne 8000
    cosmotek 12000
    zenicorp 9000
    novastar 8000

### Példa kimenet
    aerodyne
    novastar
    zenicorp
    cosmotek
    oriontech

### A példa magyarázata
Az `aerodyne` és a `novastar` cégek egyaránt 8000-es ajánlatot tettek. Mivel az `a` betű előrébb áll az ábécében, az `aerodyne` kerül az első helyre, míg a `novastar` a másodikra.  
Harmadik helyen szerepel a `zenicorp` 9000-es ajánlatával.  
A 12000-es ajánlatot adó `cosmotek` és `oriontech` közül a cosmotek áll előrébb, mert a `c` betű az `o` betűnél előbbre van az ábécében.
