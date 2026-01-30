#!/usr/bin/env python3
# @check-accepted: *

string = input()
x = string.count("x")
print(min(2 * x - 1, len(string)))
