#!/usr/bin/env python3
# coding:utf-8
n = int(input())
chislo = input()
k = int(input())
for _ in range(k):
    if chislo[1:2] > "0":
        if chislo[:1] > chislo[1:2]:
            chislo = chislo[1:]
        else:
            chislo = chislo[0] + chislo[2:]
    else:
        i = 2
        while i < len(chislo):
            if chislo[i] > "0":
                chislo = chislo[:i] + chislo[i + 1:]
                break
            i += 1
        else:
            chislo = chislo[:-1]

print(int(chislo))

