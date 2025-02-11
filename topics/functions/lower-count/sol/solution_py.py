#!/usr/bin/env python3
# @check-accepted: *


def count_lower(lista, hatar):
    count = 0
    for szam in lista:
        if szam < hatar:
            count += 1

    return count


# Do not change anything below!!!
N, K = [int(x) for x in input().split()]
A = list(map(int, input().split()))
print(count_lower(A, K))
