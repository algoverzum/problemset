#!/usr/bin/env python3
# @check-accepted: *


def main():
    D, K, N = map(int, input().split())

    # Igények (végnap, kezdőnap) alakban; a végnap = t + h,
    # ezen a napon a faház már újra kiadható
    igenyek = []
    for _ in range(N):
        t, h = map(int, input().split())
        igenyek.append((t + h, t))

    # 1. Rendezés végnap szerint (egyenlőség esetén kezdőnap szerint)
    igenyek.sort()

    # 2. A már használt faházak felszabadulási napjai egy listában.
    #    Mivel az igényeket végnap szerint növekvő sorrendben dolgozzuk fel,
    #    az új végnap mindig a lista végére kerül, így a lista mindig rendezett.
    fahazak = []
    ures = K  # még egyszer sem használt faházak száma

    elfogadott_db = 0

    for veg, kezdet in igenyek:
        # Bináris kereséssel megkeressük az utolsó olyan faházat,
        # amelyik legkésőbb a kezdőnapon szabadul fel (érték <= kezdet).
        bal, jobb = 0, len(fahazak)  # keressük az első > kezdet elemet
        while bal < jobb:
            kozep = (bal + jobb) // 2
            if fahazak[kozep] <= kezdet:
                bal = kozep + 1
            else:
                jobb = kozep
        # bal = az első olyan index, ahol a faház még foglalt

        if bal > 0:
            # Van szabad használt faház: a LEGKÉSŐBB felszabadulót foglaljuk el
            fahazak.pop(bal - 1)
            fahazak.append(veg)
            elfogadott_db += 1
        elif ures > 0:
            # Nincs szabad használt faház, de van még érintetlen
            ures -= 1
            fahazak.append(veg)
            elfogadott_db += 1
        # különben az igényt elutasítjuk

    print(elfogadott_db)


main()
