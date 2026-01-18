#!/usr/bin/env python3
# @check-accepted: *

cim = input()
i = 0
postafiok = ""
while cim[i] != "@":
    postafiok += cim[i]
    i += 1
print(postafiok)
i += 1
postahivatal = ""
while i < len(cim):
    postahivatal += cim[i]
    i += 1
print(postahivatal)
