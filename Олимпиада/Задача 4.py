#!/usr/bin/env python3
# coding:utf-8
a, b = input(), input()
tstart = [int(x) for x in input().split(':')]
tend = [int(x) for x in input().split(':')]
rad = 0
happy = 0
dlit = (tend[0] - tstart[0]) * 60 + (tend[1] - tstart[1]) + 1
for time in range(dlit):
    min = (tstart[1] + time) % 60
    hr = tstart[0] + (tstart[1] + time) // 60
    st = f"{hr:02}{min:02}"
    if a in st and b in st:
        happy += 1
    elif a in st or b in st:
        rad += 1
print(rad)
print(happy)
