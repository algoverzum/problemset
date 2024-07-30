#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
s = n % 60
n //= 60
m = n % 60
n //= 60
h = n % 24
n //= 24
d = n
print(d, h, m, s)
