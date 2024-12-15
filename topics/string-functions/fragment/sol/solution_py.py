#!/usr/bin/env python3
# @check-accepted: *

uzenet = input()
betu = input()
elso = uzenet.find(betu)
utolso = uzenet.rfind(betu)
if elso != -1 and elso != utolso:
    reszlet = uzenet[elso : utolso + 1]
    print(reszlet)
else:
    print(-1)
