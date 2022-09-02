import sys

input = sys.stdin.readline

n = int(input())

d = [[0 for i in range(3)] for i in range(n+1)]
costs = [[0, 0, 0]]

for i in range(n):
    cost = list(map(int, input().split()))
    costs.append(cost)

for i in range(3):
    d[1][i] = costs[1][i]


for i in range(2, n+1):
    for j in range(3):
        d[i][j] = costs[i][j] + min(d[i-1][:j] + d[i-1][j+1:])

print(min(d[n]))
