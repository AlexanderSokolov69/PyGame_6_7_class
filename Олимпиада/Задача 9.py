#!/usr/bin/env python3
# coding:utf-8
n = int(input())
chislo = input()
res = []
svch = chislo
k = int(input())
for it in range(k):
    if it <= k - 2:
        el = min(chislo[0:1], chislo[1:2], chislo[2:3])
        if chislo[0:1] == el:
            chislo = chislo[1:]
        elif chislo[1:2] == el:
            chislo = chislo[:1] + chislo[2:]
        elif chislo[2:3] == el:
            chislo = chislo[:2] + chislo[3:]
    elif chislo[1:2] != "0":
        if chislo[:1] > chislo[1:2]:
            chislo = chislo[1:]
        else:
            chislo = chislo[0] + chislo[2:]
    else:
        i = 1
        while i < len(chislo):
            if chislo[i] != "0":
                chislo = chislo[:i] + chislo[i + 1:]
                break
            i += 1
        else:
            chislo = chislo[:-1]
if int(chislo) > 0:
    res.append(int(chislo))
chislo = svch

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
res.append(int(chislo))
chislo = svch
for it in range(k):
    if it <= k - 2:
        el = max(chislo[0:1], chislo[1:2], chislo[2:3])
        if chislo[0:1] == el and chislo[1:2] != '0':
            chislo = chislo[1:]
        elif chislo[1:2] == el:
            chislo = chislo[:1] + chislo[2:]
        elif chislo[2:3] == el:
            chislo = chislo[:2] + chislo[3:]
        else:
            chislo = chislo[:1] + chislo[2:]
    elif chislo[1:2] != "0":
        if chislo[:1] > chislo[1:2]:
            chislo = chislo[1:]
        else:
            chislo = chislo[0] + chislo[2:]
    else:
        i = 1
        while i < len(chislo):
            if chislo[i] != "0":
                chislo = chislo[:i] + chislo[i + 1:]
                break
            i += 1
        else:
            chislo = chislo[:-1]
if int(chislo) > 0:
    res.append(int(chislo))

chislo = svch
cnt = 0
while cnt < k:
    ost = chislo[k - cnt:]
    test = [int(x) for x in chislo[:k - cnt]]
    mx = max(test)
    if test.index(mx) != 0:
        test.remove(mx)
    else:
        if len(test) > 1 and test[1] == 0:
            test.remove(0)
        else:
            test.remove(mx)
    chislo = ''.join([str(x) for x in test]) + ost
    cnt += 1
if int(chislo) > 0:
    res.append(int(chislo))

print(min(res))
