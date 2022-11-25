import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
res = []


def bfs(x, y):
    graph[x][y] = 0
    q = deque([[x, y]])
    count = 0

    while q:
        start = q.popleft()
        count += 1
        for i in range(len(d)):
            dx = start[0] + d[i][0]
            dy = start[1] + d[i][1]

            if dx < 0 or dy < 0 or dx >= n or dy >= m:
                continue

            if graph[dx][dy] == 1:
                graph[dx][dy] = 0
                q.append([dx, dy])

    res.append(count)


for i in range(n):
    graph.append(list(map(int, input().split())))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)
        else:
            continue
if res:
    print(len(res))
    print(max(res))
else:
    print(0)
    print(0)
