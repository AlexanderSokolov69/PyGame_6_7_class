#!/usr/bin/env python3
# coding:utf-8
alph = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
s1 = list(input())
s2 = list(input())
x = int(input())
y = int(input())
count = 0
for i in range(n):
    if s1[i] != s2[i]:
        dist = abs(ord(s1[i]) - ord(s2[i]))
        pr1 = dist * x
        pr2 = dist * y
        pr3 = (26 - dist) * x
        pr4 = (26 - dist) * y
        count += min(pr1, pr2, pr3, pr4)
print(count)
