#!/usr/bin/env python3
# coding:utf-8
n = int(input())
k = int(input())
ost = n - k if (n - k) % 2 == 0 else n - k - 1
k = n - ost
print(k, ost // 2, ost // 2, sep='\n')
