#!/usr/bin/env python3
# @check-accepted: *


def intersection(lista1, lista2):
    metszet = []
    for num in lista1:
        if num in lista2:
            metszet.append(num)
    return metszet


# Do not change anything below!!!
input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*intersection(A, B))
