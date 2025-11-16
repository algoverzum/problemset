#!/usr/bin/env python3
# @check-accepted: *

speed = int(input())
altitude = int(input())
while speed > 1 and altitude > 0:
    print(speed, altitude)
    speed -= 10
    altitude -= 2
