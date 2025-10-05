#!/usr/bin/env python3
# @check-accepted: *

tipp1 = input()
tipp2 = input()

if tipp1 == tipp2:
    print(0)
elif (
    (tipp1 == "ko" and tipp2 == "ollo")
    or (tipp1 == "ollo" and tipp2 == "papir")
    or (tipp1 == "papir" and tipp2 == "ko")
):
    print(1)
else:
    print(2)
