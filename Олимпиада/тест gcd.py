#!/usr/bin/env python3
# coding:utf-8
from math import gcd


print(gcd(24, 60))


def find_gcd(a, b):
    a, b = (a, b) if a > b else (b, a)
    while b:
        b, a = b, a % b
        return a


a = 24
b = 60
num = find_gcd(a, b)

print(num)
