#!/usr/bin/env python3
# coding:utf-8
n = int(input())
etalon = [x for x in range(1, n + 1)]
sh = [int(x) for x in input()]
used = {}
res = []
for i, x in enumerate(sh):
    print(etalon.pop(x), end='')
print()
