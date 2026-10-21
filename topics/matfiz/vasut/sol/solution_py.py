#!/usr/bin/env python3
# @check-accepted: *
def main():
    n = int(input())

    # A kivett számok beolvasása
    kivettek = list(map(int, input().split()))

    verem = []
    akt = 1

    for x in kivettek:
        # Addig töltjük a vermet, amíg a teteje nem egyezik x-szel
        # vagy amíg el nem fogytak a számok
        while akt <= n and (not verem or verem[-1] != x):
            verem.append(akt)
            akt += 1

        # Ha a verem teteje megegyezik x-szel, kivesszük
        if verem and verem[-1] == x:
            verem.pop()
        else:
            print("NEM")
            return

    print("IGEN")


if __name__ == "__main__":
    main()
