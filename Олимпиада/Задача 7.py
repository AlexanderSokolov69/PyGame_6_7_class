#!/usr/bin/env python3
# coding:utf-8
alph = 'ABCEHKMOPTXY'
len_alph = len(alph)

n = int(input())
p1 = ((n - 1) % 999) + 1
p2 = (n - 1) // 999
p3, p2 = p2 // len_alph, p2 % len_alph
p4, p3 = p3 // len_alph, p3 % len_alph

print(f"{alph[p4]}{p1:03}{alph[p3]}{alph[p2]}")
