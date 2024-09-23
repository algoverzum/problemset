#!/usr/bin/env python3
# @check-accepted: *

numbers = list(map(int, input().split()))
print(*numbers)
print(*numbers[::-1])
