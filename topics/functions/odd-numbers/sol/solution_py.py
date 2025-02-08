#!/usr/bin/env python3
# @check-accepted: *


def odd_numbers(lista):
    odd = []
    for szam in lista:
        if szam % 2 == 1:
            odd.append(szam)
    return odd


# Do not change anything below!!!
input()
A = list(map(int, input().split()))
print(*odd_numbers(A))
