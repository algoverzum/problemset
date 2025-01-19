#!/usr/bin/env python3
# @check-accepted: *
# warning: this is exponential!!!


def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Do not change anything below
for i in range(1, 31):
    print(fibonacci(i))
