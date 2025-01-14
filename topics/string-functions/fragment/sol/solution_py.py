#!/usr/bin/env python3
# @check-accepted: *

message = input()
letter = input()
first = message.find(letter)
last = message.rfind(letter)
if first != -1:
    print(message[first : last + 1])
else:
    print(-1)
