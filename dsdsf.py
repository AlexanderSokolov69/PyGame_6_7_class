s1 = [int(n) for n in input().split()]
s2 = [int(n) for n in input().split()]
s3 = [n1 - n2 for n1, n2 in zip(s1, s2)]
print(*s3)
