import sys
input = sys.stdin.readline

n = int(input())

ans = []
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2:
        if r1 == r2 and r1 != 0:
            ans.append(-1)
        if r1 != r2:
            ans.append(0)
        if r1 == 0 and r2 == 0:
            ans.append(1)
        continue

    c_dist = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    dist = r1 + r2

    if c_dist < dist:
        ans.append(2)
    if c_dist == dist:
        ans.append(1)
    if c_dist > dist:
        ans.append(0)

[print(i) for i in ans]
