#!/usr/bin/env python3
# coding:utf-8
h = int(input())
cubs = []
for _ in range(int(input())):
    cub = int(input())
    if cub <= h:
        cubs.append(cub)
cubs.sort()
les = cubs[:1]
current = les[0]
for el in cubs[1:]:
    current += el
    if el == les[-1] and current <= h:
        les.append(el)
    elif el != les[-1]:
        les.append(el)
        current = el
print(sum(les))
