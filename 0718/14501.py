import sys
input = sys.stdin.readline

n = int(input())

d = [0] * (n+1)
sch = []
for i in range(n):
    t,p = map(int, input().split())
    sch.append([t,p])


for i in range(n-1, -1, -1):
    if i + sch[i][0] > n:
        d[i] = d[i+1]

    else:
        d[i] = max(d[i+1], sch[i][1] + d[i+ sch[i][0]])

print(d[0])