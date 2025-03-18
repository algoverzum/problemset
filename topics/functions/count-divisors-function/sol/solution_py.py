#!/usr/bin/env python3
# @check-accepted: *

# Create a count_lower function here
def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


# Do not change anything below!!!
num = int(input())
print(count_divisors(num))
