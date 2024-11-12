#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
itemCodes = input().split()
for i in range(len(itemCodes)):
    unique = True
    for j in range(len(itemCodes)):
        if i != j and int(itemCodes[i]) == int(itemCodes[j]):
            unique = False
    if unique:
        print(itemCodes[i], end=" ")
print()
