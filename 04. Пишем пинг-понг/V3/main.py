from sys import stdin
import datetime as dt


d = input().split('.')
d_begin = dt.date(int(d[2]), int(d[1]), int(d[0]))
step = dt.timedelta(days=1)
order = {3: 'cleaning', 0: 'washing', 2: 'ironing', 1: '--', 4: '--', 5: '--', 6: '--'}
dela = {x[0]: [int(x[1]), int(x[2])] for x in map(str.split, stdin.readlines())}
while True:
    day = d_begin.weekday()
    data = dela.get(order[day], [0, 0])
    if data[0] > 0:
        print(f'{d_begin.day:02}.{d_begin.month:02}.{d_begin.year}', order[day], min(data[0], data[1]))
        ost = max(0, data[0] - data[1])
        dela[order[day]][0] = ost
    d_begin = d_begin + step
    s = 0
    for d in dela.values():
        s += d[0]
    if s == 0:
        break
