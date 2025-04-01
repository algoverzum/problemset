#!/usr/bin/env python3
# @check-accepted: *


def count_lower(lista, hatar):
    count = 0
    for szam in lista:
        if szam < hatar:
            count += 1

    return count


# Do not change anything below.
n, k = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
print(count_lower(numbers, k))
