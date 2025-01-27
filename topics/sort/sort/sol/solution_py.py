#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
elements = [int(x) for x in input().split()]
elements.sort()
print(*elements)
elements.sort(reverse=True)
print(*elements)
