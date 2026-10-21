#!/usr/bin/env python3
# @check-accepted: *


def main():
    # Beolvassuk a teljes sort
    sor = input().strip()

    # Szétbontjuk szóközök mentén
    tokenek = sor.split()

    # Verem (stack) létrehozása
    verem = []

    for token in tokenek:
        # Operátor?
        if token in "+-*/":
            b = verem.pop()
            a = verem.pop()

            if token == "+":
                verem.append(a + b)
            elif token == "-":
                verem.append(a - b)
            elif token == "*":
                verem.append(a * b)
            else:  # token == "/"
                verem.append(a // b)  # egész osztás
        else:
            # Szám - int-é alakítjuk
            verem.append(int(token))

    # Az eredmény a verem tetején van
    print(verem.pop())


if __name__ == "__main__":
    main()
