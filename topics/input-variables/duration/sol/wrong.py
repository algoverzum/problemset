#!/usr/bin/env python3
# @check-wrong-answer: *

n = int(input())
s = n % 60
n //= 60
m = n % 60
n //= 60
h = n % 60
n //= 60
d = n
print(d, h, m, s)
