#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
egyesek = ["", "egy", "ketto", "harom", "negy", "ot", "hat", "het", "nyolc", "kilenc"]
tizesek = ["", "tizen", "huszon", "harminc", "negyven", "otven", "hatvan", "hetven", "nyolcvan", "kilencven"]

if n == 10:
    print("tiz")
elif n == 20:
    print("husz")
else:
    print(tizesek[n // 10] + egyesek[n % 10])
