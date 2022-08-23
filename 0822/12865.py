import sys
input = sys.stdin.readline
# https://hongcoding.tistory.com/50
n, k = map(int, input().split())

l = [[0, 0]]

for i in range(1, n+1):
    l.append(list(map(int, input().split())))

d = [[0 for i in range(k+1)] for j in range(n+1)]


for i in range(1, n+1):
    for j in range(1, k+1):
        w = l[i][0]
        v = l[i][1]

        if j < w:
            d[i][j] = d[i-1][j]

        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w] + v)

print(d[n][k])
