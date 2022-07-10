import sys
input = sys.stdin.readline

idx = [0]*1001
idy = [0]*1001
xs = []
ys = []

for i in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    idx[x] += 1
    ys.append(y)
    idy[y] += 1

set_x = set(xs)
set_y = set(ys)

ans = []
for x in set_x:
    if idx[x] != 2:
        ans.append(x)

for y in set_y:
    if idy[y] != 2:
        ans.append(y)

[print(i, end=' ') for i in ans]